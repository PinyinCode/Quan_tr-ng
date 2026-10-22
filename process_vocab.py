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

# Lấy nhóm ngành từ biến môi trường (Mặc định: Đầu Tư & Tài Chính)
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
# 2. BẢN ĐỒ CHỦ ĐIỂM & CHỦ ĐỀ CHUYÊN SÂU (2-4 TỪ TIẾNG VIỆT CÓ DẤU)
# ---------------------------------------------------------------------------
INDUSTRY_TOPICS_MAP = {
    # === MẢNG 1: TÀI CHÍNH, ĐẦU TƯ & VĨ MÔ ===
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
        {
            "chu_diem": "Tiền mã hóa Crypto",
            "chu_de": "Ví điện tử sàn",
        },
        {
            "chu_diem": "Ngoại hối Forex",
            "chu_de": "Tỷ giá đòn bẩy",
        },
    ],
    # === MẢNG 2: CÔNG XƯỞNG, KỸ THUẬT & CHẾ TẠO ===
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
            "chu_diem": "Dụng cụ cắt",
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
    "Điện Tử & SMT": [
        {
            "chu_diem": "Dây chuyền SMT",
            "chu_de": "Hàn bo mạch chip",
        },
        {
            "chu_diem": "Kiểm tra soi lỗi",
            "chu_de": "Kính hiển vi quang",
        },
        {
            "chu_diem": "Sửa chữa bo mạch",
            "chu_de": "Thay thế linh kiện",
        },
    ],
    # === MẢNG 3: ĐỜI SỐNG, VĂN HÓA, GIAO THÔNG & Y TẾ ===
    "Đời Sống & Du Lịch": [
        {
            "chu_diem": "Phương tiện đi",
            "chu_de": "Xe buýt tàu điện",
        },
        {
            "chu_diem": "Hỏi đường đi lại",
            "chu_de": "Chỉ đường bến xe",
        },
        {
            "chu_diem": "Thuê nhà ở",
            "chu_de": "Phòng trọ ký túc",
        },
        {
            "chu_diem": "Thủ tục xuất cảnh",
            "chu_de": "Hải quan visa hộ chiếu",
        },
        {
            "chu_diem": "Tham quan thắng cảnh",
            "chu_de": "Mua vé khách sạn",
        },
    ],
    "Văn Hóa & Ngày Lễ": [
        {
            "chu_diem": "Tết Nguyên Đán",
            "chu_de": "Lì xì chúc tết",
        },
        {
            "chu_diem": "Tết Trung Thu",
            "chu_de": "Bánh trung thu đèn",
        },
        {
            "chu_diem": "Ngày lễ lớn",
            "chu_de": "Quốc khánh lao động",
        },
        {
            "chu_diem": "Phong tục tập quán",
            "chu_de": "Cưới hỏi giỗ chạp",
        },
    ],
    "Y Tế & Sức Khỏe": [
        {
            "chu_diem": "Khám chữa bệnh",
            "chu_de": "Hỏi thăm triệu chứng",
        },
        {
            "chu_diem": "Mua thuốc tây",
            "chu_de": "Liều dùng hướng dẫn",
        },
        {
            "chu_diem": "Bệnh viện phòng khám",
            "chu_de": "Đăng ký sổ khám",
        },
    ],
}

# Các chủ đề mặc định nếu không khớp nhóm ngành
default_topics = [
    {
        "chu_diem": "Kỹ thuật chuyên môn",
        "chu_de": "Vận hành thiết bị",
    },
    {
        "chu_diem": "Thực hành thực tế",
        "chu_de": "Xử lý công việc",
    },
]

industry_topics = INDUSTRY_TOPICS_MAP.get(TARGET_INDUSTRY, default_topics)


# ---------------------------------------------------------------------------
# 3. CÁC HÀM XỬ LÝ VÀ CHUẨN HÓA DỮ LIỆU
# ---------------------------------------------------------------------------
def clean_pinyin(zh_text, py_text):
  """Hàm làm sạch Pinyin, đảm bảo 100% Latinh kèm dấu, không dính chữ Hán."""
  has_chinese = re.search(r"[\u4e00-\u9fff]", str(py_text or ""))
  if not py_text or has_chinese:
    py_list = lazy_pinyin(zh_text, style=Style.TONE)
    return " ".join(py_list).strip()
  cleaned = re.sub(r"[\u4e00-\u9fff]", "", str(py_text)).strip()
  return re.sub(r"\s+", " ", cleaned)


def generate_vocabulary_batch(chu_diem, chu_de):
  """Sinh từ vựng chuyên sâu. Ưu tiên chất lượng tối đa, không ép số lượng rác."""
  prompt = f"""Bạn là chuyên gia hàng đầu và cố vấn cao cấp trong lĩnh vực: {TARGET_INDUSTRY}.
Hãy cung cấp danh sách từ vựng và thuật ngữ chuyên ngành **thật sự cốt lõi, chuyên sâu và có tính thực chiến cao nhất** thuộc:
- Chủ điểm: {chu_diem}
- Chủ đề: {chu_de}

YÊU CẦU CHẤT LƯỢNG KHẮT KHE:
1. Tập trung tuyệt đối vào thuật ngữ chuyên môn thực sự (Ví dụ: vĩ mô -> CPI, FED, thắt chặt tiền tệ; tài chính -> bán khống, đòn bẩy; cơ khí -> máy CNC, xung điện EDM, dung sai...).
2. TUYỆT ĐỐI KHÔNG sinh từ vựng chung chung, lan man hoặc cố làm cho đủ số lượng lớn. Chỉ lấy những từ thực sự chất lượng nhất (khoảng 15-25 từ chuẩn).
3. Pinyin (py) BẮT BUỘC chỉ chứa chữ cái Latinh có dấu thanh, KHÔNG ĐƯỢC CHỨA CHỮ HÁN.
4. Trả về đúng định dạng JSON mảng (array) như sau:
[
  {{
    "hsk": "HSK 4",
    "vi": "Thuật ngữ tiếng Việt",
    "zh": "Thuật ngữ tiếng Trung",
    "py": "Pinyin Latinh đầy đủ có dấu"
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
  """Tạo câu ví dụ giao tiếp công việc/thao tác/đầu tư ngắn gọn (<= 12 ký tự chữ Hán)."""
  prompt = f"""Bạn là chuyên gia thực chiến trong lĩnh vực {industry_name}.
Hãy đặt 01 câu giao tiếp hoặc nhận định ngắn gọn, thực tế có chứa từ vựng '{zh}' (nghĩa là: '{vi}').

YÊU CẦU BẮT BUỘC:
1. Ngữ cảnh: Câu nói thực tế, súc tích (trong thao tác xưởng, nhận định thị trường, giao dịch hoặc sinh hoạt).
2. Độ dài: Câu tiếng Trung (zh) KHÔNG ĐƯỢC VƯỢT QUÁ 12 KÝ TỰ chữ Hán.
3. Pinyin: Chỉ chứa chữ cái Latinh kèm dấu thanh, tuyệt đối không lẫn chữ Hán.

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
    ex_vi = data.get("vi", f"Cần theo dõi {vi}.")
    ex_zh = data.get("zh", f"注意{zh}。")
    ex_py = clean_pinyin(ex_zh, data.get("py", ""))
    return ex_vi, ex_zh, ex_py
  except Exception:
    fallback_zh = f"注意{zh}。"
    return (f"Cần theo dõi {vi}.", fallback_zh, clean_pinyin(fallback_zh, ""))


# ---------------------------------------------------------------------------
# 4. CHƯƠNG TRÌNH CHÍNH XUẤT FILE EXCEL
# ---------------------------------------------------------------------------
file_output = os.path.join(output_dir, f"{filename_prefix}.xlsx")
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Vocabulary"

# Tiêu đề cột chuẩn
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

# Tập hợp (Set) dùng để lọc bỏ từ trùng lặp
seen_chinese_words = set()

print(
    f"🚀 BẮT ĐẦU TẠO DỮ LIỆU CỰC CHUYÊN SÂU CHO NGÀNH: [{TARGET_INDUSTRY}]..."
)
print(f"📁 File đầu ra: {file_output}\n" + "=" * 60)

for topic in industry_topics:
  c_diem = topic["chu_diem"]
  c_de = topic["chu_de"]

  print(f"📦 Đang xử lý: Chủ điểm [{c_diem}] | Chủ đề [{c_de}]...")
  vocab_list = generate_vocabulary_batch(c_diem, c_de)
  print(f"   -> AI trả về {len(vocab_list)} thuật ngữ chọn lọc.")

  added_count = 0
  for item in vocab_list:
    hsk = item.get("hsk", "HSK 4")
    vi = item.get("vi")
    zh = item.get("zh")
    raw_py = item.get("py", "")

    if not zh or not vi:
      continue

    zh_clean = str(zh).strip()

    # Bỏ qua nếu từ đã từng xuất hiện để tránh trùng lặp
    if zh_clean in seen_chinese_words:
      continue
    seen_chinese_words.add(zh_clean)

    py = clean_pinyin(zh_clean, raw_py)

    # 1. HÀNG TỪ VỰNG CHUYÊN SÂU GỐC
    sheet.cell(row=current_row, column=1, value=global_stt)
    sheet.cell(row=current_row, column=2, value=hsk)
    sheet.cell(row=current_row, column=3, value=c_diem)
    sheet.cell(row=current_row, column=4, value=c_de)
    sheet.cell(row=current_row, column=5, value=vi)
    sheet.cell(row=current_row, column=6, value=zh_clean)
    sheet.cell(row=current_row, column=7, value=py)
    current_row += 1
    global_stt += 1

    # 2. HÀNG CÂU VÍ DỤ GIAO TIẾP / THAO TÁC / NHẬN ĐỊNH (<= 12 KÝ TỰ)
    if len(zh_clean) <= 12:
      ex_vi, ex_zh, ex_py = generate_example_sentence(
          vi, zh_clean, TARGET_INDUSTRY
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

    added_count += 1
    time.sleep(0.3)

  print(f"   ✅ Đã lọc và lưu {added_count} từ vựng chất lượng cao.")

wb.save(file_output)
print("=" * 60)
print(
    f"🎉 HOÀN TẤT THÀNH CÔNG! File đã được lưu tại: {file_output}\n📊 Tổng số"
    f" dòng dữ liệu (từ vựng + câu ví dụ): {current_row - 1}"
)
