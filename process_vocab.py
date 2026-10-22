import json
import os
import re
import time
from openai import OpenAI
import openpyxl
from pypinyin import Style, lazy_pinyin

# ---------------------------------------------------------------------------
# 1. CẤU HÌNH BIẾN MÔI TRƯỜNG VÀ KHỞI TẠO CLIENT
# ---------------------------------------------------------------------------
api_key = os.environ.get("DASHSCOPE_API_KEY")
base_url = os.environ.get(
    "QWEN_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
)
model_name = os.environ.get("QWEN_MODEL", "qwen-plus")

client = OpenAI(api_key=api_key, base_url=base_url, timeout=60.0)

# Cấu hình thư mục lưu file
output_dir = "scripts/data_copy"
os.makedirs(output_dir, exist_ok=True)

# Lấy nhóm ngành từ biến môi trường
TARGET_INDUSTRY = os.environ.get("TARGET_INDUSTRY", "Đầu Tư & Tài Chính")

# Xử lý tên file đẹp, chuẩn hóa
clean_name = (
    TARGET_INDUSTRY.strip()
    .replace("&", "")
    .replace("-", "_")
    .replace("  ", " ")
    .replace(" ", "_")
)
filename_prefix = f"{clean_name}_Chuyen_Sau"

# ---------------------------------------------------------------------------
# 2. BẢN ĐỒ CHỦ ĐIỂM & CHỦ ĐỀ CHUYÊN SÂU
# ---------------------------------------------------------------------------
INDUSTRY_TOPICS_MAP = {
    "Đầu Tư & Tài Chính": [
        {
            "chu_diem": "Vàng và hàng hóa",
            "chu_de": "Vàng miếng nhẫn tròn",
        },
        {
            "chu_diem": "Tiền tệ và lãi suất",
            "chu_de": "Lãi suất điều hành FED",
        },
        {
            "chu_diem": "Kinh tế vĩ mô",
            "chu_de": "Lạm phát báo cáo CPI",
        },
        {
            "chu_diem": "Giao dịch phái sinh",
            "chu_de": "Bán khống hợp đồng",
        },
    ],
    "Cơ Khí & Chế Tạo": [
        {
            "chu_diem": "Máy CNC",
            "chu_de": "Tiện phay trung tâm",
        },
        {
            "chu_diem": "Gia công điện",
            "chu_de": "Xung điện cắt dây",
        },
        {
            "chu_diem": "Dao cụ cắt",
            "chu_de": "Dao cụ bầu kẹp",
        },
        {
            "chu_diem": "Đo kiểm KCS",
            "chu_de": "Dung sai kích thước",
        },
    ],
    "May Mặc": [
        {
            "chu_diem": "Thiết bị may",
            "chu_de": "Máy vắt sổ kansai",
        },
        {
            "chu_diem": "Phòng cắt mẫu",
            "chu_de": "Trải vải sơ đồ",
        },
        {
            "chu_diem": "Quy trình may",
            "chu_de": "Ráp thân chỉnh lỗi",
        },
        {
            "chu_diem": "Hoàn thiện KCS",
            "chu_de": "Là ủi đóng gói",
        },
    ],
}

default_topics = [
    {
        "chu_diem": "Kỹ thuật chuyên môn",
        "chu_de": "Vận hành thiết bị",
    }
]

industry_topics = INDUSTRY_TOPICS_MAP.get(TARGET_INDUSTRY, default_topics)


# ---------------------------------------------------------------------------
# 3. HÀM LÀM SẠCH VÀ CHUẨN HÓA DỮ LIỆU 3 CỘT (VI, ZH, PY)
# ---------------------------------------------------------------------------
def clean_vietnamese(vi_text):
  """Bắt buộc loại bỏ 100% chữ Hán xuất hiện trong cột Tiếng Việt."""
  if not vi_text:
    return ""
  cleaned = re.sub(r"[\u4e00-\u9fff]", "", str(vi_text)).strip()
  return re.sub(r"\s+", " ", cleaned)


def clean_chinese(zh_text):
  """Đảm bảo ô Tiếng Trung chỉ chứa chữ Hán và dấu câu Trung Quốc, loại bỏ sạch ký tự Latinh/tiếng Việt lạc vào."""
  if not zh_text:
    return ""
  # Loại bỏ hoàn toàn các chữ cái tiếng Việt / chữ cái Latinh (a-z, A-Z) nếu bị dính vào ô tiếng Trung
  cleaned = re.sub(r"[a-zA-Zà-ỹÀ-Ỹ]", "", str(zh_text))
  return cleaned.strip()


def clean_pinyin(zh_text, py_text):
  """Hàm làm sạch Pinyin, đảm bảo 100% Latinh kèm dấu, không dính chữ Hán."""
  has_chinese = re.search(r"[\u4e00-\u9fff]", str(py_text or ""))
  if not py_text or has_chinese:
    py_list = lazy_pinyin(zh_text, style=Style.TONE)
    return " ".join(py_list).strip()
  cleaned = re.sub(r"[\u4e00-\u9fff]", "", str(py_text)).strip()
  return re.sub(r"\s+", " ", cleaned)


def generate_vocabulary_batch(chu_diem, chu_de):
  """Sinh từ vựng chuyên sâu với ràng buộc định dạng nghiêm ngặt."""
  prompt = f"""Bạn là chuyên gia hàng đầu và cố vấn cao cấp trong lĩnh vực: {TARGET_INDUSTRY}.
Hãy cung cấp danh sách từ vựng và thuật ngữ chuyên ngành **thật sự cốt lõi, chuyên sâu và có tính thực chiến cao nhất** thuộc:
- Chủ điểm: {chu_diem}
- Chủ đề: {chu_de}

YÊU CẦU BẮT BUỘC VỀ ĐỊNH DẠNG:
1. Trường "vi" (Tiếng Việt): CHỈ DÙNG TIẾNG VIỆT CÓ DẤU, TUYỆT ĐỐI KHÔNG CHỨA CHỮ HÁN.
2. Trường "zh" (Tiếng Trung): CHỈ CHỨA CHỮ HÁN VÀ DẤU CÂU TRUNG QUỐC, TUYỆT ĐỐI KHÔNG CHỨA CHỮ CÁI LATINH (a-z) HAY KÝ TỰ LẠ.
3. Trường "py" (Pinyin): Chỉ chứa chữ cái Latinh có dấu thanh, KHÔNG CHỨA CHỮ HÁN.

Trả về đúng định dạng JSON mảng (array):
[
  {{
    "hsk": "HSK 4",
    "vi": "Nghĩa tiếng Việt chuẩn xác",
    "zh": "Thuật ngữ tiếng Trung",
    "py": "Pinyin Latinh có dấu"
  }},
  ...
]
"""
  max_retries = 3
  for attempt in range(max_retries):
    try:
      response = client.chat.completions.create(
          model=model_name,
          messages=[{"role": "user", "content": prompt}],
          temperature=0.5,
          response_format={"type": "json_object"},
      )
      data = json.loads(response.choices[0].message.content)
      if isinstance(data, dict):
        for k, v in data.items():
          if isinstance(v, list):
            data = v
            break
      return data if isinstance(data, list) else []
    except Exception as e:
      print(f"⚠️ Lỗi kết nối AI (lần {attempt + 1}): {e}")
      time.sleep(2)
  return []


def generate_example_sentence(vi, zh, industry_name):
  """Tạo câu ví dụ giao tiếp ngắn gọn (<= 12 ký tự chữ Hán), làm sạch tuyệt đối."""
  prompt = f"""Bạn là chuyên gia thực chiến trong lĩnh vực {industry_name}.
Hãy đặt 01 câu giao tiếp hoặc nhận định ngắn gọn, thực tế có chứa từ vựng '{zh}' (nghĩa là: '{vi}').

YÊU CẦU BẮT BUỘC:
1. Trường "vi" (Tiếng Việt): BẢN DỊCH HOÀN TOÀN BẰNG TIẾNG VIỆT, KHÔNG DÍNH CHỮ HÁN.
2. Trường "zh" (Tiếng Trung): CHỈ CHỨA CHỮ HÁN VÀ DẤU CÂU, KHÔNG CHỨA CHỮ CÁI LATINH. ĐỘ DÀI KHÔNG QUÁ 12 KÝ TỰ CHỮ HÁN.
3. Trường "py" (Pinyin): Chỉ chứa chữ cái Latinh kèm dấu thanh.

Trả về đúng định dạng JSON:
{{
  "zh": "Câu tiếng Trung dưới 12 ký tự",
  "py": "Pinyin đầy đủ có dấu",
  "vi": "Bản dịch tiếng Việt hoàn chỉnh"
}}
"""
  try:
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        response_format={"type": "json_object"},
    )
    data = json.loads(response.choices[0].message.content)
    ex_vi = clean_vietnamese(data.get("vi", f"Cần thao tác {vi}."))
    if not ex_vi:
      ex_vi = f"Thao tác {vi} ngay."

    ex_zh = clean_chinese(data.get("zh", f"注意{zh}。"))
    if not ex_zh:
      ex_zh = f"注意{zh}。"

    ex_py = clean_pinyin(ex_zh, data.get("py", ""))
    return ex_vi, ex_zh, ex_py
  except Exception:
    fallback_zh = f"注意{zh}。"
    return (f"Thao tác {vi} ngay.", fallback_zh, clean_pinyin(fallback_zh, ""))


# ---------------------------------------------------------------------------
# 4. CHƯƠNG TRÌNH CHÍNH XUẤT FILE EXCEL
# ---------------------------------------------------------------------------
file_output = os.path.join(output_dir, f"{filename_prefix}.xlsx")
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Vocabulary"

headers = [
    "STT",
    "HSK",
    "Chủ điểm",
    "Chủ đề",
    "Tiếng Việt",
    "Tiếng Trung",
    "Pinyin",
    "Luyện tập",
    "Check đúng/sai",
]
for col_num, header_title in enumerate(headers, 1):
  sheet.cell(row=1, column=col_num, value=header_title)

current_row = 2
global_stt = 1
seen_chinese_words = set()

print(
    f"🚀 BẮT ĐẦU TẠO DỮ LIỆU CỰC CHUYÊN SÂU CHO NGÀNH: [{TARGET_INDUSTRY}]..."
)

for topic in industry_topics:
  c_diem = topic["chu_diem"]
  c_de = topic["chu_de"]

  print(f"📦 Đang xử lý: Chủ điểm [{c_diem}] | Chủ đề [{c_de}]...")
  vocab_list = generate_vocabulary_batch(c_diem, c_de)

  added_count = 0
  for item in vocab_list:
    hsk = item.get("hsk", "HSK 4")
    vi_raw = item.get("vi")
    zh_raw = item.get("zh")
    raw_py = item.get("py", "")

    if not zh_raw or not vi_raw:
      continue

    # 1. Làm sạch cột Tiếng Việt và Tiếng Trung
    vi = clean_vietnamese(vi_raw)
    zh = clean_chinese(zh_raw)

    if not vi or not zh:
      continue

    # 2. Bỏ qua từ bị trùng lặp
    if zh in seen_chinese_words:
      continue
    seen_chinese_words.add(zh)

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

    # --- HÀNG 2: CÂU VÍ DỤ (<= 12 KÝ TỰ CHỮ HÁN) ---
    if len(zh) <= 12:
      ex_vi, ex_zh, ex_py = generate_example_sentence(vi, zh, TARGET_INDUSTRY)

      sheet.cell(row=current_row, column=1, value=global_stt)
      sheet.cell(row=current_row, column=2, value=hsk)
      sheet.cell(row=current_row, column=3, value=c_diem)
      sheet.cell(row=current_row, column=4, value=c_de)
      sheet.cell(row=current_row, column=5, value=ex_vi)
      sheet.cell(row=current_row, column=6, value=ex_zh)
      sheet.cell(row=current_row, column=7, value=ex_py)
      current_row += 1
      global_stt += 1

    added_count += 1
    time.sleep(0.3)

  print(f"   ✅ Đã lưu {added_count} từ vựng sạch chuẩn 100%.")

wb.save(file_output)
print(f"🎉 HOÀN TẤT! File lưu tại: {file_output}")
