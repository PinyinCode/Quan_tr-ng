# -*- coding: utf-8 -*-
r"""
Script CẬP NHẬT TỐI ƯU Âm thanh & Câu chuyện (Chơi chữ, bắt vần, không lặp dòng).
Tự động commit và push sau mỗi 100 từ lên GitHub.
"""
import os
import sys
import json
import time
import re
import subprocess
from openai import OpenAI

# ═══════════════════════════════════════════════════════════════════
#  CONFIG
# ═══════════════════════════════════════════════════════════════════
API_KEY = os.getenv("DASHSCOPE_API_KEY")
BASE_URL = os.getenv(
    "QWEN_BASE_URL",
    "https://ws-8lcqaxwxdv0h9xzy.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
)
MODEL_ID = os.getenv("QWEN_MODEL", "qwen-plus-character")

LIMIT_WORDS = int(os.getenv("LIMIT_WORDS", "20"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "ai_mnemonics.json")
DELAY_BETWEEN = float(os.getenv("DELAY_BETWEEN", "1.2"))

# ═══════════════════════════════════════════════════════════════════
#  GIT AUTOMATION (Đã sửa lỗi exit code 128)
# ═══════════════════════════════════════════════════════════════════
def git_commit_and_push(count):
    try:
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
        subprocess.run(["git", "add", OUTPUT_FILE], check=True)
        
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            msg = f"🔄 Auto-commit: Đã cập nhật {count} từ vựng mới [skip ci]"
            
            # 1. Commit trước
            subprocess.run(["git", "commit", "-m", msg], check=True)
            # 2. Pull rebase sau khi index đã sạch
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)
            # 3. Push
            subprocess.run(["git", "push"], check=True)
            print(f"   🚀 [GIT] Đã push tiến trình ({count} từ) lên GitHub!")
    except Exception as e:
        print(f"   ⚠️ Lỗi git commit/push: {e}")

# ═══════════════════════════════════════════════════════════════════
#  PROMPT TINH CHỈNH: TẠO MẸO CỰC KỲ NGẮN GỌN & BẮT VẦN
# ═══════════════════════════════════════════════════════════════════
def build_story_prompt(zh, pinyin, vi):
    vi_str = vi if vi else "Không rõ"
    return f"""Bạn là một chuyên gia giảng dạy tiếng Trung, chuyên tạo ra các mẹo nhớ (mnemonic) cực kỳ thông minh, ngắn gọn và hài hước cho người Việt.

Nhiệm vụ: Tạo mẹo nhớ cho từ **{zh}** (Pinyin: {pinyin} | Nghĩa: {vi_str}).

Hãy tư duy theo 2 bước:
- Bước 1: Tìm một từ/cụm từ tiếng Việt có âm thanh GẦN GIỐNG NHẤT với "{pinyin}" (Ví dụ: pinyin "bā" -> "ba", "bá", "bà").
- Bước 2: Dệt từ vừa tìm được vào một câu chuyện ngắn (1 câu) có liên quan trực tiếp đến nghĩa "{vi_str}". Bắt buộc câu chuyện phải chứa từ mang âm thanh đó.

Yêu cầu định dạng đầu ra (BẮT BUỘC CHỈ XUẤT RA 2 DÒNG NÀY, KHÔNG GIẢI THÍCH THÊM):
📌 Âm thanh: [Điền từ/cụm từ tiếng Việt đồng âm ở Bước 1]
🎬 Câu chuyện: [Điền 1 câu chuyện ngắn gọn, vui vẻ, liên kết âm thanh và nghĩa]

Ví dụ mẫu:
📌 Âm thanh: ma
🎬 Câu chuyện: Con ma nằm mơ (mā) thấy mẹ (mā).
"""

def generate_new_story(zh, pinyin, vi):
    if not API_KEY:
        return ""

    prompt = build_story_prompt(zh, pinyin, vi)
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7, # Tăng nhẹ temperature để AI sáng tạo hơn
            max_tokens=150,
        )
        if response and response.choices:
            msg = response.choices[0].message
            if hasattr(msg, "content") and msg.content:
                return msg.content.strip()
    except Exception as e:
        print(f"      ⚠️ Lỗi API: {e}")
    return ""

def parse_info_from_content(content):
    """ Trích xuất Pinyin và Nghĩa tiếng Việt từ nội dung cũ """
    pinyin = ""
    vi_meaning = ""
    
    match = re.search(r'\(([a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵĐđ\s\-]+)\)', content, re.IGNORECASE)
    if match:
        pinyin_raw = match.group(1)
        parts = pinyin_raw.split('-')
        pinyin = parts[0].strip()
        if len(parts) > 1:
            vi_meaning = parts[1].strip()

    if not vi_meaning:
        match_eq = re.search(r'=\s*([A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÊẾỀỂỄỆÔỐỒỔỖỘƠỚỜỞỠỢƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴ\s\/]+)', content)
        if match_eq:
            vi_meaning = match_eq.group(1).strip().lower()

    return pinyin, vi_meaning

def clean_and_update_content(old_text, new_story_text):
    """ Xóa toàn bộ các dòng Âm thanh/Câu chuyện cũ để tránh lặp và chèn dòng mới vào """
    if not new_story_text:
        return old_text

    lines = old_text.split("\n")
    cleaned_lines = []
    
    # Xóa sạch các dòng chứa mẹo cũ (bao gồm cả icon và text)
    for line in lines:
        if not ("📌" in line or "🎬" in line or "Âm thanh:" in line or "Câu chuyện:" in line):
            cleaned_lines.append(line)

    # Lấy 2 dòng mới
    new_lines = [l.strip() for l in new_story_text.split("\n") if l.strip() and ("📌" in l or "🎬" in l)]
    
    insert_idx = 0
    for idx, l in enumerate(cleaned_lines):
        if "Chiết tự:" in l or "💡" in l:
            insert_idx = idx + 1
            break
            
    final_lines = cleaned_lines[:insert_idx] + new_lines + cleaned_lines[insert_idx:]
    return "\n".join(final_lines)

def main():
    if not os.path.exists(OUTPUT_FILE):
        print(f"❌ Không tìm thấy file {OUTPUT_FILE}")
        return

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_words = len(data)
    target_count = total_words if LIMIT_WORDS == 0 else min(LIMIT_WORDS, total_words)

    print(f"📦 Đã load {total_words} từ từ file JSON")
    print(f"🎯 MỤC TIÊU: Xử lý {target_count} từ {'(Chạy thử)' if LIMIT_WORDS > 0 else '(Toàn bộ)'}\n")

    updated_count = 0

    for idx, (key, content) in enumerate(data.items(), 1):
        if LIMIT_WORDS > 0 and idx > LIMIT_WORDS:
            print(f"\n🛑 Đã đạt giới hạn {LIMIT_WORDS} từ chạy thử. Dừng script!")
            break

        parts = key.split("|")
        zh = parts[-1] if len(parts) >= 3 else key
        
        pinyin, vi_meaning = parse_info_from_content(content)

        print(f"[{idx}/{target_count}] Đang xử lý: {zh} (pinyin: {pinyin} | nghĩa: {vi_meaning})...", flush=True)
        
        new_story = generate_new_story(zh, pinyin, vi_meaning)
        if new_story:
            updated_content = clean_and_update_content(content, new_story)
            data[key] = updated_content
            updated_count += 1
            print(f"   ✅ Hoàn tất {zh}", flush=True)
        else:
            print(f"   ❌ Thất bại, giữ nguyên {zh}", flush=True)

        # Lưu file liên tục để tránh mất dữ liệu
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        if updated_count > 0 and updated_count % 100 == 0:
            print(f"\n📦 [CHECKPOINT] Đã đạt {updated_count} từ. Tiến hành Push lên GitHub...")
            git_commit_and_push(updated_count)

        time.sleep(DELAY_BETWEEN)

    # Push những từ lẻ còn sót lại cuối cùng (nếu chưa đủ 100)
    if updated_count % 100 != 0 and updated_count > 0:
        git_commit_and_push(updated_count)

    print(f"\n🎉 HOÀN TẤT! Đã làm mới câu chuyện cho {updated_count} từ.")

if __name__ == "__main__":
    main()
