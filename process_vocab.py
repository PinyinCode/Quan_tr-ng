import json
import os
import re
import time
from openai import OpenAI
import openpyxl
from pypinyin import Style, pypinyin

# Lấy thông tin cấu hình từ biến môi trường
api_key = os.environ.get("DASHSCOPE_API_KEY")
base_url = os.environ.get(
    "QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
)
model_name = os.environ.get("QWEN_MODEL", "qwen-plus")

client = OpenAI(api_key=api_key, base_url=base_url, timeout=60.0)

# Định nghĩa thư mục nguồn và thư mục lưu bản sao
input_dir = "scripts/data"
output_dir = "scripts/data_copy"

# Tự động tạo thư mục data_copy nếu chưa có
os.makedirs(output_dir, exist_ok=True)

# Nhận tên file được truyền từ GitHub Workflow (mặc định 'ALL' nếu chạy cục bộ)
SELECTED_FILE = os.environ.get("TARGET_FILE", "ALL")

if SELECTED_FILE == "ALL":
  excel_files = [
      f
      for f in os.listdir(input_dir)
      if f.endswith(".xlsx") and not f.startswith("~$")
  ]
  print(
      f"📂 ĐÃ CHỌN: Xử lý TẤT CẢ các file từ thư mục '{input_dir}' (Tổng số:"
      f" {len(excel_files)} file)"
  )
else:
  target_path = os.path.join(input_dir, SELECTED_FILE)
  if os.path.exists(target_path):
    excel_files = [SELECTED_FILE]
    print(f"🎯 ĐÃ CHỌN CỤ THỂ 1 FILE ĐỂ XỬ LÝ: {SELECTED_FILE}")
  else:
    print(f"❌ Không tìm thấy file '{SELECTED_FILE}' tại đường dẫn {target_path}!")
    excel_files = []


def clean_pinyin(zh_text, py_text):
  """Hàm làm sạch và chuẩn hóa Pinyin:

  - Nếu Pinyin rỗng hoặc dính chữ Hán, dùng pypinyin tự tạo Pinyin chuẩn.
  - Loại bỏ hoàn toàn ký tự tiếng Trung còn sót lại.
  """
  has_chinese = re.search(r"[\u4e00-\u9fff]", str(py_text or ""))

  if not py_text or has_chinese:
    py_list = pypinyin(zh_text, style=Style.TONE)
    clean_py = " ".join([item[0] for item in py_list])
    return clean_py.strip()

  cleaned = re.sub(r"[\u4e00-\u9fff]", "", str(py_text)).strip()
  cleaned = re.sub(r"\s+", " ", cleaned)
  return cleaned


def generate_example_sentence(vi, zh):
  prompt = f"""Bạn là chuyên gia ngôn ngữ giỏi tiếng Trung.
Hãy đặt 01 câu giao tiếp ngắn gọn, tự nhiên có chứa từ vựng '{zh}' (nghĩa là: '{vi}').

YÊU CẦU BẮT BUỘC:
- Câu tiếng Trung KHÔNG ĐƯỢC VƯỢT QUÁ 12 KÝ TỰ chữ Hán.
- Pinyin (py) BẮT BUỘC chỉ là chữ cái Latinh kèm dấu thanh, KHÔNG ĐƯỢC CHỨA BẤT KỲ KÝ TỰ CHỮ HÁN NÀO.
- Tự nhiên, ngắn gọn, dễ nhớ.

Trả về đúng định dạng JSON:
{{
  "zh": "Câu tiếng Trung ngắn dưới 12 ký tự",
  "py": "Pinyin đầy đủ có dấu của câu",
  "vi": "Bản dịch tiếng Việt hoàn chỉnh của câu"
}}
"""
  try:
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        response_format={"type": "json_object"},
    )
    data = json.loads(response.choices[0].message.content)
    ex_vi = data.get("vi", f"Cần chú ý {vi}.")
    ex_zh = data.get("zh", f"要注意{zh}。")
    ex_py = clean_pinyin(ex_zh, data.get("py", ""))
    return ex_vi, ex_zh, ex_py
  except Exception:
    fallback_zh = f"要注意{zh}。"
    return (
        f"Cần chú ý {vi}.",
        fallback_zh,
        clean_pinyin(fallback_zh, ""),
    )


# Vòng lặp xử lý từng file được chọn
for index, file_name in enumerate(excel_files, 1):
  src_file_path = os.path.join(input_dir, file_name)
  dest_file_path = os.path.join(output_dir, file_name)

  print(
      f"\n=============================================================="
  )
  print(f"🚀 [{index}/{len(excel_files)}] ĐANG XỬ LÝ FILE: {file_name}")
  print(
      f"=============================================================="
  )

  wb = openpyxl.load_workbook(src_file_path)
  sheet = wb.active

  # Đọc toàn bộ dữ liệu cũ của file ra một danh sách (bỏ qua dòng tiêu đề hàng 1)
  old_rows = []
  for row in range(2, sheet.max_row + 1):
    hsk = sheet.cell(row=row, column=2).value
    chu_diem = sheet.cell(row=row, column=3).value
    chu_de = sheet.cell(row=row, column=4).value
    vi = sheet.cell(row=row, column=5).value
    zh = sheet.cell(row=row, column=6).value
    py = sheet.cell(row=row, column=7).value

    # Nếu dòng hợp lệ thì lưu lại
    if zh and vi:
      old_rows.append({
          "hsk": hsk,
          "chu_diem": chu_diem,
          "chu_de": chu_de,
          "vi": vi,
          "zh": zh,
          "py": py,
      })

  print(
      f"📊 Tổng số từ vựng gốc trong file {file_name}: {len(old_rows)} từ."
  )
  print(
      "🔄 Đang tiến hành tạo câu ví dụ ngắn gọn (<= 12 ký tự) và viết lại cấu"
      " trúc file Excel..."
  )

  # Xóa sạch dữ liệu cũ trong sheet (trừ hàng tiêu đề)
  sheet.delete_rows(2, sheet.max_row + 1)

  current_row = 2
  global_stt = 1
  count = 0

  for item in old_rows:
    hsk = item["hsk"]
    c_diem = item["chu_diem"]
    c_de = item["chu_de"]
    vi = item["vi"]
    zh = item["zh"]
    raw_py = item["py"]

    # Chuẩn hóa Pinyin của từ vựng gốc
    py = clean_pinyin(zh, raw_py)

    # --- HÀNG 1: TỪ VỰNG GỐC ---
    sheet.cell(row=current_row, column=1, value=global_stt)
    sheet.cell(row=current_row, column=2, value=hsk)
    sheet.cell(row=current_row, column=3, value=c_diem)
    sheet.cell(row=current_row, column=4, value=c_de)
    sheet.cell(row=current_row, column=5, value=vi)
    sheet.cell(row=current_row, column=6, value=zh)
    sheet.cell(row=current_row, column=7, value=py)
    current_row += 1
    global_stt += 1

    # --- HÀNG 2: CÂU NGẮN CHỨA TỪ ĐÓ (Chỉ với từ/cụm ngắn <= 12 ký tự) ---
    if len(str(zh)) <= 12:
      ex_vi, ex_zh, ex_py = generate_example_sentence(vi, zh)

      sheet.cell(row=current_row, column=1, value=global_stt)
      sheet.cell(row=current_row, column=2, value=hsk)
      sheet.cell(row=current_row, column=3, value=c_diem)
      sheet.cell(row=current_row, column=4, value=c_de)
      sheet.cell(row=current_row, column=5, value=ex_vi)  # Câu tiếng Việt ngắn
      sheet.cell(row=current_row, column=6, value=ex_zh)  # Câu tiếng Trung ngắn (<= 12 ký tự)
      sheet.cell(row=current_row, column=7, value=ex_py)  # Pinyin chuẩn hóa
      current_row += 1
      global_stt += 1

      count += 1
      if count % 10 == 0:
        print(f"   ⏳ Đã tạo câu ví dụ ngắn cho {count} từ...")
        wb.save(dest_file_path)  # Lưu tạm vào thư mục data_copy định kỳ
      time.sleep(0.3)

  # Lưu file hoàn tất vào thư mục data_copy
  wb.save(dest_file_path)
  print(
      f"✅ LƯU BẢN SAO THÀNH CÔNG TẠI: {dest_file_path} (Đã thêm {count} dòng"
      " câu ví dụ ngắn)."
  )

print("\n🎉 TẤT CẢ CÁC FILE ĐÃ XỬ LÝ VÀ LƯU VÀO THƯ MỤC `scripts/data_copy/`!")
