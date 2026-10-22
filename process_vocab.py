from copy import copy
import json
import os
import time
from openai import OpenAI
import openpyxl

api_key = os.environ.get("DASHSCOPE_API_KEY")
base_url = os.environ.get(
    "QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
)
model_name = os.environ.get("QWEN_MODEL", "qwen-plus")

client = OpenAI(api_key=api_key, base_url=base_url, timeout=60.0)

input_dir = "scripts/data"
output_dir = "scripts/data_copy"
os.makedirs(output_dir, exist_ok=True)


def generate_batch_sentences(batch_items, chu_diem, chu_de):
  words_list_str = "\n".join([
      f"- ID: {idx}, Từ Trung: {item['zh']}, Nghĩa Việt: {item['vi']}"
      for idx, item in enumerate(batch_items)
  ])

  prompt = f"""Bạn là một chuyên gia quản lý sản xuất và trợ lý văn phòng giỏi tiếng Trung.
Chủ đề công việc: {chu_diem} - {chu_de}.

Hãy đặt 01 câu giao tiếp tự nhiên, chuẩn văn phong nhà xưởng/công sở cho TỪNG từ vựng trong danh sách sau:
{words_list_str}

Yêu cầu BẮT BUỘC:
1. Mỗi câu phải độc nhất, mang tính thực tế cao (báo cáo, kiểm tra, giải quyết sự cố, nhắc tiến độ, phân công...).
2. Tuyệt đối KHÔNG lặp lại cấu trúc câu rập khuôn.
3. Trả về đúng định dạng JSON là một mảng (array) chứa các object tương ứng theo đúng ID:
[
  {{
    "id": 0,
    "zh": "Câu tiếng Trung tự nhiên",
    "py": "Pinyin đầy đủ có dấu",
    "vi": "Bản dịch tiếng Việt tự nhiên"
  }},
  ...
]
"""
  max_retries = 5
  wait_time = 5

  for attempt in range(max_retries):
    try:
      response = client.chat.completions.create(
          model=model_name,
          messages=[{"role": "user", "content": prompt}],
          temperature=0.8,
          response_format={"type": "json_object"},
      )
      content = response.choices[0].message.content
      data = json.loads(content)
      if isinstance(data, dict):
        for k, v in data.items():
          if isinstance(v, list):
            data = v
            break
      return data
    except Exception as e:
      if "429" in str(e) or "rate limit" in str(e).lower():
        print(
            f"   [⏳ 429] Vượt giới hạn RPM. Đang đợi {wait_time}s thử lại (lần"
            f" {attempt + 1}/{max_retries})..."
        )
        time.sleep(wait_time)
        wait_time *= 2
      else:
        print(f"   [❌ Lỗi API Batch]: {e}")
        break

  fallback_results = []
  for idx, item in enumerate(batch_items):
    fallback_results.append({
        "id": idx,
        "vi": f"Xử lý vấn đề {item['vi']} này cần báo lại cho quản lý.",
        "zh": f"处理这个{item['zh']}问题需要向主管汇报。",
        "py": f"Chǔlǐ zhè ge {item['zh']} wèntí xūyào xiàng zhǔguǎn huìbào.",
    })
  return fallback_results


excel_files = [f for f in os.listdir(input_dir) if f.endswith(".xlsx")]

if not excel_files:
  print(f"⚠️ Không tìm thấy file Excel nào trong thư mục {input_dir}")

print("==================================================")
print(f"📂 TỔNG SỐ FILE CẦN XỬ LÝ: {len(excel_files)} file")
print("==================================================\n")

for file_idx, filename in enumerate(excel_files, start=1):
  file_input = os.path.join(input_dir, filename)
  file_output = os.path.join(output_dir, filename)

  print(
      f"🚀 [{file_idx}/{len(excel_files)}] ĐANG XỬ LÝ FILE: {filename}..."
  )

  start_time = time.time()
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

  rows_data = []
  for r in range(2, src_sheet.max_row + 1):
    hsk = src_sheet.cell(row=r, column=2).value
    chu_diem = src_sheet.cell(row=r, column=3).value
    chu_de = src_sheet.cell(row=r, column=4).value
    vi = src_sheet.cell(row=r, column=5).value
    zh = src_sheet.cell(row=r, column=6).value
    py = src_sheet.cell(row=r, column=7).value

    if not zh or not vi:
      continue
    rows_data.append({
        "row_idx": r,
        "hsk": hsk,
        "chu_diem": chu_diem,
        "chu_de": chu_de,
        "vi": vi,
        "zh": zh,
        "py": py,
        "need_ai": len(str(zh)) <= 12,
    })

  batch_size = 8
  ai_results = {}
  total_ai_items = sum(1 for item in rows_data if item["need_ai"])

  print(
      f"   📊 Số từ vựng gốc: {len(rows_data)} | Số từ cần sinh câu AI:"
      f" {total_ai_items}"
  )

  ai_data_list = [item for item in rows_data if item["need_ai"]]

  for i in range(0, len(ai_data_list), batch_size):
    chunk = ai_data_list[i : i + batch_size]
    ai_items = [{"zh": item["zh"], "vi": item["vi"]} for item in chunk]

    c_diem = chunk[0]["chu_diem"]
    c_de = chunk[0]["chu_de"]

    batch_num = (i // batch_size) + 1
    total_batches = (len(ai_data_list) + batch_size - 1) // batch_size
    print(
        f"   📦 Đang sinh câu Batch {batch_num}/{total_batches} ({len(ai_items)}"
        " từ)..."
    )

    res_list = generate_batch_sentences(ai_items, c_diem, c_de)

    for res in res_list:
      res_id = res.get("id")
      if res_id is not None and res_id < len(ai_items):
        target_row_data = chunk[res_id]
        ai_results[target_row_data["row_idx"]] = (
            res.get("vi"),
            res.get("zh"),
            res.get("py"),
        )

    time.sleep(1.0)

  # Ghi dữ liệu vào file đích
  current_dst_row = 2
  new_stt = 1

  for item in rows_data:
    r = item["row_idx"]
    # 1. Ghi dòng từ vựng gốc
    dst_sheet.cell(row=current_dst_row, column=1, value=new_stt)
    dst_sheet.cell(row=current_dst_row, column=2, value=item["hsk"])
    dst_sheet.cell(row=current_dst_row, column=3, value=item["chu_diem"])
    dst_sheet.cell(row=current_dst_row, column=4, value=item["chu_de"])
    dst_sheet.cell(row=current_dst_row, column=5, value=item["vi"])
    dst_sheet.cell(row=current_dst_row, column=6, value=item["zh"])
    dst_sheet.cell(row=current_dst_row, column=7, value=item["py"])
    current_dst_row += 1
    new_stt += 1

    # 2. Ghi dòng câu mở rộng AI (nếu có)
    if item["need_ai"] and r in ai_results:
      ex_vi, ex_zh, ex_py = ai_results[r]
      dst_sheet.cell(row=current_dst_row, column=1, value=new_stt)
      dst_sheet.cell(row=current_dst_row, column=2, value=item["hsk"])
      dst_sheet.cell(row=current_dst_row, column=3, value=item["chu_diem"])
      dst_sheet.cell(row=current_dst_row, column=4, value=item["chu_de"])
      dst_sheet.cell(row=current_dst_row, column=5, value=ex_vi)
      dst_sheet.cell(row=current_dst_row, column=6, value=ex_zh)
      dst_sheet.cell(row=current_dst_row, column=7, value=ex_py)
      current_dst_row += 1
      new_stt += 1

  dst_wb.save(file_output)
  elapsed_time = time.time() - start_time

  # LOG THÀNH CÔNG RÕ RÀNG VÀO CONSOLE
  print(f"==================================================")
  print(f"✅ THÀNH CÔNG: {filename}")
  print(f"📍 Đã lưu tại: {file_output}")
  print(
      f"⏱️ Thời gian xử lý: {elapsed_time:.1f}s | Tổng dòng sau mở rộng:"
      f" {current_dst_row - 1}"
  )
  print(f"==================================================\n")

print("🎉 HOÀN THÀNH TẤT CẢ CÁC FILE EXCEL!")
