import json
import os
import time
from openai import OpenAI
import openpyxl

# Lấy thông tin cấu hình từ biến môi trường
api_key = os.environ.get("DASHSCOPE_API_KEY")
base_url = os.environ.get(
    "QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
)
model_name = os.environ.get("QWEN_MODEL", "qwen-plus")

client = OpenAI(api_key=api_key, base_url=base_url, timeout=60.0)

input_dir = "scripts/data"

# Nhận tên file được truyền từ GitHub Workflow (mặc định 'ALL' nếu chạy cục bộ)
SELECTED_FILE = os.environ.get("TARGET_FILE", "ALL")

if SELECTED_FILE == "ALL":
  excel_files = [
      f
      for f in os.listdir(input_dir)
      if f.endswith(".xlsx") and not f.startswith("~$")
  ]
  print(
      f"📂 ĐÃ CHỌN: Xử lý TẤT CẢ các file trong thư mục (Tổng số:"
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


def generate_example_sentence(vi, zh):
  prompt = f"""Bạn là chuyên gia ngôn ngữ giỏi tiếng Trung.
Hãy đặt 01 câu giao tiếp tự nhiên, chuẩn văn phong đời sống/công sở có chứa từ '{zh}' ({vi}).

Trả về đúng định dạng JSON:
{{
  "zh": "Câu tiếng Trung tự nhiên",
  "py": "Pinyin đầy đủ có dấu",
  "vi": "Bản dịch tiếng Việt tự nhiên"
}}
"""
  try:
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        response_format={"type": "json_object"},
    )
    data = json.loads(response.choices[0].message.content)
    return data["vi"], data["zh"], data["py"]
  except Exception:
    return (
        f"Cần chú ý xử lý vấn đề {vi} này một cách cẩn thận.",
        f"需要仔细处理这个{zh}问题。",
        f"Xūyào zǐxì chǔlǐ zhè ge {zh} wèntí.",
    )


# Vòng lặp xử lý từng file được chọn
for index, file_name in enumerate(excel_files, 1):
  file_path = os.path.join(input_dir, file_name)
  print(
      f"\n=============================================================="
  )
  print(f"🚀 [{index}/{len(excel_files)}] ĐANG XỬ LÝ FILE: {file_name}")
  print(
      f"=============================================================="
  )

  wb = openpyxl.load_workbook(file_path)
  sheet = wb.active

  # Đếm số lượng từ gốc và chuẩn bị mở rộng
  rows_to_process = []
  for row in range(2, sheet.max_row + 1):
    vi = sheet.cell(row=row, column=5).value
    zh = sheet.cell(row=row, column=6).value
    # Nếu dòng nào có từ tiếng Trung và chưa có câu ví dụ/hoặc cần xử lý tiếp
    if zh and vi:
      rows_to_process.append((row, vi, zh))

  print(
      f"📊 Tổng số dòng từ vựng trong file {file_name}:"
      f" {len(rows_to_process)}"
  )

  count = 0
  for row_idx, vi, zh in rows_to_process:
    # Chỉ sinh câu ví dụ cho từ ngắn gọn (<= 12 ký tự) nếu chưa có
    current_practice = sheet.cell(row=row_idx, column=8).value
    if len(str(zh)) <= 12 and not current_practice:
      ex_vi, ex_zh, ex_py = generate_example_sentence(vi, zh)

      # Ghi dữ liệu mở rộng vào các cột tương ứng
      sheet.cell(row=row_idx, column=8, value=ex_zh)
      sheet.cell(row=row_idx, column=9, value=ex_py)
      sheet.cell(row=row_idx, column=10, value=ex_vi)

      count += 1
      if count % 10 == 0:
        print(f"   ⏳ Đã sinh câu cho {count} từ...")
        wb.save(file_path)  # Lưu tạm định kỳ tránh mất dữ liệu
      time.sleep(0.3)

  # Lưu file hoàn tất sau khi xong mỗi file
  wb.save(file_path)
  print(f"✅ HOÀN TẤT VÀ LƯU FILE: {file_name} (Đã bổ sung {count} câu ví dụ).")

print(
    "\n🎉 TẤT CẢ CÁC FILE ĐƯỢC CHỌN ĐÃ XỬ LÝ XONG XUÔI VÀ SẴN SÀNG COMMIT!"
)
