import json
import os
import re
import time
from openai import OpenAI
import openpyxl
from pypinyin import Style, lazy_pinyin

# Lấy thông tin cấu hình từ biến môi trường
api_key = os.environ.get("DASHSCOPE_API_KEY")
base_url = os.environ.get(
    "QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
)
model_name = os.environ.get("QWEN_MODEL", "qwen-plus")

client = OpenAI(api_key=api_key, base_url=base_url, timeout=60.0)

input_dir = "scripts/data"
output_dir = "scripts/data_copy"

os.makedirs(output_dir, exist_ok=True)

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
  """Hàm làm sạch và chuẩn hóa Pinyin."""
  has_chinese = re.search(r"[\u4e00-\u9fff]", str(py_text or ""))

  if not py_text or has_chinese:
    py_list = lazy_pinyin(zh_text, style=Style.TONE)
    return " ".join(py_list).strip()

  cleaned = re.sub(r"[\u4e00-\u9fff]", "", str(py_text)).strip()
  return re.sub(r"\s+", " ", cleaned)


def generate_example_sentence(vi, zh, context_info="công xưởng / nhà máy"):
  """Tạo câu ví dụ giao tiếp thực tế trong công xưởng/công ty theo từng ngành nghề."""
  prompt = f"""Bạn là chuyên gia ngôn ngữ tiếng Trung làm việc trong môi trường nhà máy, công xưởng sản xuất.
Hãy đặt 01 câu giao tiếp công việc ngắn gọn, thực tế trong nhà máy/công ty (liên quan đến {context_info}) có chứa từ vựng '{zh}' (nghĩa là: '{vi}').

YÊU CẦU BẮT BUỘC:
1. NỘI DUNG: Bắt buộc là câu nói/mệnh lệnh/trao đổi công việc thực tế trong nhà xưởng, máy móc thiết bị, quy trình sản xuất, công đoạn làm việc, báo cáo hoặc trao đổi với quản lý/đồng nghiệp.
2. ĐỘ DÀI: Câu tiếng Trung KHÔNG ĐƯỢC VƯỢT QUÁ 12 KÝ TỰ chữ Hán.
3. PINYIN: Pinyin (py) BẮT BUỘC chỉ là chữ cái Latinh kèm dấu thanh, KHÔNG ĐƯỢC CHỨA BẤT KỲ KÝ TỰ CHỮ HÁN NÀO.
4. TỰ NHIÊN, DỄ NÓI, ỨNG DỤNG CAO.

Trả về đúng định dạng JSON:
{{
  "zh": "Câu tiếng Trung công xưởng ngắn dưới 12 ký tự",
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
    ex_vi = data.get("vi", f"Cần kiểm tra {vi}.")
    ex_zh = data.get("zh", f"检查一下{zh}。")
    ex_py = clean_pinyin(ex_zh, data.get("py", ""))
    return ex_vi, ex_zh, ex_py
  except Exception:
    fallback_zh = f"检查一下{zh}。"
    return (
        f"Cần kiểm tra {vi}.",
        fallback_zh,
        clean_pinyin(fallback_zh, ""),
    )


# Vòng lặp xử lý từng file được chọn
for index, file_name in enumerate(excel_files, 1):
  src_file_path = os.path.join(input_dir, file_name)
  dest_file_path = os.path.join(output_dir, file_name)

  # Xác định tên ngành/chủ đề chính dựa trên tên file
  industry_context = file_name.replace(".xlsx", "").replace("_", " ")

  print(
      f"\n=============================================================="
  )
  print(
      f"🚀 [{index}/{len(excel_files)}] ĐANG XỬ LÝ FILE: {file_name} (Ngành:"
      f" {industry_context})"
  )
  print(
      f"=============================================================="
  )

  wb = openpyxl.load_workbook(src_file_path)
  sheet = wb.active

  old_rows = []
  for row in range(2, sheet.max_row + 1):
    hsk = sheet.cell(row=row, column=2).value
    chu_diem = sheet.cell(row=row, column=3).value
    chu_de = sheet.cell(row=row, column=4).value
    vi = sheet.cell(row=row, column=5).value
    zh = sheet.cell(row=row, column=6).value
    py = sheet.cell(row=row, column=7).value

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
      "🔄 Đang tiến hành tạo câu ví dụ công xưởng ngắn gọn (<= 12 ký tự) và"
      " viết lại cấu trúc file Excel..."
  )

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

    # --- HÀNG 2: CÂU NGẮN CHỨA TỪ ĐÓ (<= 12 ký tự) ---
    if len(str(zh)) <= 12:
      # Kết hợp ngữ cảnh từ tên file, chủ điểm, chủ đề
      item_context = (
          f"ngành {industry_context}, chủ điểm '{c_diem}', chủ đề '{c_de}',"
          " môi trường công xưởng / xưởng sản xuất / máy móc"
      )
      ex_vi, ex_zh, ex_py = generate_example_sentence(
          vi, zh, context_info=item_context
      )

      sheet.cell(row=current_row, column=1, value=global_stt)
      sheet.cell(row=current_row, column=2, value=hsk)
      sheet.cell(row=current_row, column=3, value=c_diem)
      sheet.cell(row=current_row, column=4, value=c_de)
      sheet.cell(row=current_row, column=5, value=ex_vi)
      sheet.cell(row=current_row, column=6, value=ex_zh)
      sheet.cell(row=current_row, column=7, value=ex_py)
      current_row += 1
      global_stt += 1

      count += 1
      if count % 10 == 0:
        print(f"   ⏳ Đã tạo câu ví dụ công xưởng cho {count} từ...")
        wb.save(dest_file_path)
      time.sleep(0.3)

  wb.save(dest_file_path)
  print(
      f"✅ LƯU BẢN SAO THÀNH CÔNG TẠI: {dest_file_path} (Đã thêm {count} dòng"
      " câu ví dụ công xưởng)."
  )

print("\n🎉 TẤT CẢ CÁC FILE ĐÃ XỬ LÝ VÀ LƯU VÀO THƯ MỤC `scripts/data_copy/`!")
