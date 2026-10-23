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

# Lấy nhóm ngành từ biến môi trường (Ví dụ: Cơ Khí & Chế Tạo hoặc Điện Tử & SMT)
TARGET_INDUSTRY = os.environ.get("TARGET_INDUSTRY", "Cơ Khí & Chế Tạo")

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
# 2. BẢN ĐỒ CHỦ ĐIỂM & CHỦ ĐỀ CHUYÊN SÂU (2-4 TỪ, KỸ THUẬT CAO)
# ---------------------------------------------------------------------------
INDUSTRY_TOPICS_MAP = {
    "Cơ Khí & Chế Tạo": [
        {
            "chu_diem": "Trung tâm CNC",
            "chu_de": "Tiện phay CNC",
        },
        {
            "chu_diem": "Cắt dây xung",
            "chu_de": "Gia công EDM",
        },
        {
            "chu_diem": "Dao cụ cắt",
            "chu_de": "Mũi khoan taro",
        },
        {
            "chu_diem": "Dung sai kích",
            "chu_de": "Đo kiểm bản vẽ",
        },
        {
            "chu_diem": "Hàn xì kết cấu",
            "chu_de": "Hàn TIG MIG",
        },
        {
            "chu_diem": "Đúc khuôn kim",
            "chu_de": "Khuôn ép nhựa",
        },
        {
            "chu_diem": "Bảo trì máy",
            "chu_de": "Hệ thống thủy lực",
        },
        {
            "chu_diem": "Động cơ điện",
            "chu_de": "Máy nén khí",
        },
    ],
    "Điện Tử & SMT": [
        {
            "chu_diem": "In thiếc hàn",
            "chu_de": "Dao gạt mỏ hàn",
        },
        {
            "chu_diem": "Máy gắp linh",
            "chu_de": "Feed chỉ định",
        },
        {
            "chu_diem": "Hàn lưu lượng",
            "chu_de": "Lò hàn đối lưu",
        },
        {
            "chu_diem": "Kiểm tra AOI",
            "chu_de": "Soi lỗi mối hàn",
        },
        {
            "chu_diem": "Kiểm tra SPI",
            "chu_de": "Đo lượng thiếc",
        },
        {
            "chu_diem": "Kiểm tra XRay",
            "chu_de": "Soi chân BGA",
        },
        {
            "chu_diem": "Bảng mạch PCB",
            "chu_de": "Lớp mạch đồng",
        },
        {
            "chu_diem": "Linh kiện dán",
            "chu_de": "Chip tụ điện",
        },
    ],
    "May Mặc": [
        {
            "chu_diem": "Cắt rập mẫu",
            "chu_de": "Trải sơ đồ cắt",
        },
        {
            "chu_diem": "Ép keo dựng",
            "chu_de": "Ép keo cổ vạt",
        },
        {
            "chu_diem": "May mổ túi",
            "chu_de": "Mổ túi cơi viền",
        },
        {
            "chu_diem": "Ráp thân áo",
            "chu_de": "Chắp sườn diễu",
        },
        {
            "chu_diem": "Tra tay áo",
            "chu_de": "Vòng nách tay",
        },
        {
            "chu_diem": "May tra cổ",
            "chu_de": "Ráp cổ bẻ trụ",
        },
        {
            "chu_diem": "Cuốn gấu lai",
            "chu_de": "Gấp lai cuốn gấu",
        },
        {
            "chu_diem": "Kiểm lỗi KCS",
            "chu_de": "Soi chỉ lỗi đường",
        },
    ],
    "Đầu Tư & Tài Chính": [
        {
            "chu_diem": "Sàn giao dịch",
            "chu_de": "Hệ thống niêm",
        },
        {
            "chu_diem": "Cổ đông lớn",
            "chu_de": "Cổ đông sáng",
        },
        {
            "chu_diem": "Nhà tạo lập",
            "chu_de": "Đội lái thao",
        },
        {
            "chu_diem": "Lệnh giao dịch",
            "chu_de": "Khớp lệnh ATO",
        },
        {
            "chu_diem": "Đòn bẩy margin",
            "chu_de": "Cho vay ký",
        },
        {
            "chu_diem": "Thị trường Forex",
            "chu_de": "Tỷ giá ngoại",
        },
        {
            "chu_diem": "Tiền mã hóa",
            "chu_de": "Ví sàn crypto",
        },
        {
            "chu_diem": "Thị trường vàng",
            "chu_de": "Lạm phát trú",
        },
        {
            "chu_diem": "Lãi suất FED",
            "chu_de": "Chính sách tiền",
        },
    ],
}

default_topics = [
    {
        "chu_diem": "Kỹ thuật chuyên",
        "chu_de": "Vận hành máy",
    }
]

industry_topics = INDUSTRY_TOPICS_MAP.get(TARGET_INDUSTRY, default_topics)


# ---------------------------------------------------------------------------
# 3. HÀM LÀM SẠCH VÀ CHUẨN HÓA DỮ LIỆU TUYỆT ĐỐI
# ---------------------------------------------------------------------------
def clean_vietnamese(vi_text):
  """Bắt buộc loại bỏ 100% chữ Hán xuất hiện trong cột Tiếng Việt."""
  if not vi_text:
    return ""
  cleaned = re.sub(r"[\u4e00-\u9fff]", "", str(vi_text)).strip()
  return re.sub(r"\s+", " ", cleaned)


def clean_chinese(zh_text):
  """Đảm bảo ô Tiếng Trung chỉ chứa chữ Hán và dấu câu, loại bỏ hoàn toàn ký tự Latinh/tiếng Việt."""
  if not zh_text:
    return ""
  cleaned = re.sub(r"[a-zA-Zà-ỹÀ-Ỹ]", "", str(zh_text))
  return cleaned.strip()


def clean_pinyin(zh_text, py_text):
  """Làm sạch Pinyin, đảm bảo 100% Latinh kèm dấu, không dính chữ Hán."""
  has_chinese = re.search(r"[\u4e00-\u9fff]", str(py_text or ""))
  if not py_text or has_chinese:
    py_list = lazy_pinyin(zh_text, style=Style.TONE)
    return " ".join(py_list).strip()
  cleaned = re.sub(r"[\u4e00-\u9fff]", "", str(py_text)).strip()
  return re.sub(r"\s+", " ", cleaned)


def generate_vocabulary_batch(chu_diem, chu_de):
  """Sinh từ vựng chuyên sâu tập trung kỹ thuật vận hành máy & xưởng."""
  prompt = f"""Bạn là kỹ sư trưởng và chuyên gia kỹ thuật công nghiệp hàng đầu trong lĩnh vực: {TARGET_INDUSTRY}.
Hãy cung cấp danh sách từ vựng và thuật ngữ chuyên ngành **thật sự cốt lõi, chuyên sâu và có tính thực chiến cao về quy trình vận hành, máy móc, dung sai, lỗi kỹ thuật và thao tác xưởng** thuộc:
- Chủ điểm: {chu_diem}
- Chủ đề: {chu_de}

YÊU CẦU BẮT BUỘC:
1. Trường "vi": CHỈ DÙNG TIẾNG VIỆT CÓ DẤU, TUYỆT ĐỐI KHÔNG CHỨA CHỮ HÁN.
2. Trường "zh": CHỈ CHỨA CHỮ HÁN VÀ DẤU CÂU, KHÔNG CHỨA CHỮ CÁI LATINH (a-z) HAY KÝ TỰ KHÁC.
3. Trường "py": Chỉ chứa chữ cái Latinh có dấu thanh, KHÔNG CHỨA CHỮ HÁN.

Trả về đúng định dạng JSON mảng (array):
[
  {{
    "hsk": "HSK 4",
    "vi": "Thuật ngữ chuyên ngành kỹ thuật",
    "zh": "Thuật ngữ tiếng Trung",
    "py": "Pinyin có dấu"
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
  """Tạo câu ví dụ chỉ đạo kỹ thuật/vận hành máy ngắn gọn (<= 12 ký tự chữ Hán)."""
  prompt = f"""Bạn là kỹ sư trưởng chuyền sản xuất thực chiến trong ngành {industry_name}.
Hãy đặt 01 câu chỉ đạo kỹ thuật hoặc giao tiếp vận hành ngắn gọn có chứa thuật ngữ '{zh}' (nghĩa là: '{vi}').

YÊU CẦU BẮT BUỘC:
1. Trường "vi": Hoàn toàn bằng tiếng Việt, không dính chữ Hán.
2. Trường "zh": Chỉ chứa chữ Hán và dấu câu, tối đa 12 ký tự chữ Hán, không chứa chữ cái Latinh.
3. Trường "py": Chỉ chứa chữ cái Latinh kèm dấu thanh.

Trả về đúng định dạng JSON:
{{
  "zh": "Câu tiếng Trung dưới 12 ký tự",
  "py": "Pinyin đầy đủ có dấu",
  "vi": "Bản dịch tiếng Việt"
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
    ex_vi = clean_vietnamese(data.get("vi", f"Kiểm tra {vi}."))
    if not ex_vi:
      ex_vi = f"Kiểm tra {vi}."

    ex_zh = clean_chinese(data.get("zh", f"注意{zh}。"))
    if not ex_zh:
      ex_zh = f"注意{zh}。"

    ex_py = clean_pinyin(ex_zh, data.get("py", ""))
    return ex_vi, ex_zh, ex_py
  except Exception:
    fallback_zh = f"注意{zh}。"
    return (f"Kiểm tra {vi}.", fallback_zh, clean_pinyin(fallback_zh, ""))


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

print(f"🚀 BẮT ĐẦU TẠO DỮ LIỆU KỸ THUẬT CHUYÊN SÂU: [{TARGET_INDUSTRY}]...")

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

    vi = clean_vietnamese(vi_raw)
    zh = clean_chinese(zh_raw)

    if not vi or not zh:
      continue

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

    # --- HÀNG 2: CÂU VÍ DỤ (<= 12 KÝ TỰ) ---
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

  print(f"   ✅ Đã lưu {added_count} từ vựng kỹ thuật chuẩn xác.")

wb.save(file_output)
print(f"🎉 HOÀN TẤT! File lưu tại: {file_output}")
