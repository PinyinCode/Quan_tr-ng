from copy import copy
import json
import os
import time
from openai import OpenAI
import openpyxl

# Lấy cấu hình từ GitHub Secrets
api_key = os.environ.get("DASHSCOPE_API_KEY")
base_url = os.environ.get(
    "QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
)
model_name = os.environ.get("QWEN_MODEL", "qwen-plus")

client = OpenAI(api_key=api_key, base_url=base_url, timeout=30.0)

input_dir = "scripts/data"
output_dir = "scripts/data_copy"
os.makedirs(output_dir, exist_ok=True)


def generate_unique_sentence_via_ai(word_vi, word_zh, chu_diem, chu_de):
  prompt = f"""Bạn là một chuyên gia quản lý sản xuất và trợ lý văn phòng giỏi tiếng Trung.
Hãy đặt 01 câu giao tiếp tự nhiên, chuẩn văn phong nhà xưởng/công sở có chứa từ '{word_zh}' ({word_vi}).
Chủ đề công việc: {chu_diem} - {chu_de}.

Yêu cầu BẮT BUỘC:
1. Câu phải độc nhất, mang tính thực tế cao (báo cáo, kiểm tra, giải quyết sự cố, nhắc tiến độ, phân công...).
2. Tuyệt đối KHÔNG lặp lại cấu trúc câu rập khuôn như "Phiền bạn...", "Xin hãy...", "Đối với hạng mục...".
3. Trả về đúng định dạng JSON:
{{
  "zh": "Câu tiếng Trung tự nhiên",
  "py": "Pinyin đầy đủ có dấu",
  "vi": "Bản dịch tiếng Việt tự nhiên"
}}
"""
  max_retries = 5
  wait_time = 5  # Thời gian chờ ban đầu khi dính lỗi 429 (tăng dần mỗi lần thử lại)

  for attempt in range(max_retries):
    try:
      response = client.chat.completions.create(
          model=model_name,
          messages=[{"role": "user", "content": prompt}],
          temperature=0.8,
          response_format={"type": "json_object"},
      )
      data = json.loads(response.choices[0].message.content)
      return data["vi"], data["zh"], data["py"]
    except Exception as e:
      if "429" in str(e) or "rate limit" in str(e).lower():
        print(
            f"⚠️ Gặp giới hạn 429 ở từ '{word_zh}'. Đang đợi {wait_time}s để thử"
            f" lại (lần {attempt + 1}/{max_retries})..."
        )
        time.sleep(wait_time)
        wait_time *= 2  # Tăng thời gian chờ gấp đôi nếu vẫn bị lỗi
      else:
        print(f"⚠️ Lỗi API khác cho từ '{word_zh}': {e}")
        break

  # Fallback nếu thử lại hết số lần vẫn lỗi
  return (
      f"Xử lý vấn đề {word_vi} này cần báo lại cho quản lý.",
      f"处理这个{word_zh}问题需要向主管汇报。",
      f"Chǔlǐ zhè ge {word_zh} wèntí xūyào xiàng zhǔguǎn huìbào.",
  )


excel_files = [f for f in os.listdir(input_dir) if f.endswith(".xlsx")]

for filename in excel_files:
  file_input = os.path.join(input_dir, filename)
  file_output = os.path.join(output_dir, filename)

  print(
      f"🚀 Bắt đầu xử lý file: {filename} (Chế độ tuần tự + Tự động thử lại khi"
      " quá tải)..."
  )

  src_wb = openpyxl.load_workbook(file_input)
  src_sheet = src_wb.active

  dst_wb = openpyxl.Workbook()
  dst_sheet = dst_wb.active
  dst_sheet.title = src_sheet.title

  for col in src_sheet.column_dimensions:
    dst_sheet.column_dimensions[col].width = src_sheet.column_dimensions[
        col
    ].width

  for col in range(1, src_sheet.max_column + 1):
    src_cell = src_sheet.cell(row=1, column=col)
    dst_cell = dst_sheet.cell(row=1, column=col, value=src_cell.value)
    if src_cell.has_style:
      dst_cell.font = copy(src_cell.font)
      dst_cell.border = copy(src_cell.border)
      dst_cell.fill = copy(src_cell.fill)
      dst_cell.alignment = copy(src_cell.alignment)

  current_dst_row = 2
  new_stt = 1

  for r in range(2, src_sheet.max_row + 1):
    hsk = src_sheet.cell(row=r, column=2).value
    chu_diem = src_sheet.cell(row=r, column=3).value
    chu_de = src_sheet.cell(row=r, column=4).value
    vi = src_sheet.cell(row=r, column=5).value
    zh = src_sheet.cell(row=r, column=6).value
    py = src_sheet.cell(row=r, column=7).value

    if not zh or not vi:
      continue

    # 1. Ghi dòng từ vựng gốc
    dst_sheet.cell(row=current_dst_row, column=1, value=new_stt)
    dst_sheet.cell(row=current_dst_row, column=2, value=hsk)
    dst_sheet.cell(row=current_dst_row, column=3, value=chu_diem)
    dst_sheet.cell(row=current_dst_row, column=4, value=chu_de)
    dst_sheet.cell(row=current_dst_row, column=5, value=vi)
    dst_sheet.cell(row=current_dst_row, column=6, value=zh)
    dst_sheet.cell(row=current_dst_row, column=7, value=py)
    current_dst_row += 1
    new_stt += 1

    # 2. Ghi dòng câu mở rộng AI (với từ ngắn <= 12 ký tự)
    if len(str(zh)) <= 12:
      print(f"Đang tạo câu AI cho từ: {zh} ({vi})...")
      ex_vi, ex_zh, ex_py = generate_unique_sentence_via_ai(
          str(vi), str(zh), str(chu_diem), str(chu_de)
      )

      dst_sheet.cell(row=current_dst_row, column=1, value=new_stt)
      dst_sheet.cell(row=current_dst_row, column=2, value=hsk)
      dst_sheet.cell(row=current_dst_row, column=3, value=chu_diem)
      dst_sheet.cell(row=current_dst_row, column=4, value=chu_de)
      dst_sheet.cell(row=current_dst_row, column=5, value=ex_vi)
      dst_sheet.cell(row=current_dst_row, column=6, value=ex_zh)
      dst_sheet.cell(row=current_dst_row, column=7, value=ex_py)
      current_dst_row += 1
      new_stt += 1

      # Nghỉ 1.5 giây giữa mỗi request để đảm bảo an toàn tuyệt đối với hạn mức miễn phí
      time.sleep(1.5)

  dst_wb.save(file_output)
  print(f"✅ Đã xử lý xong và lưu thành công tại: {file_output}")
