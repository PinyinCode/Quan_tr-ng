# -*- coding: utf-8 -*-
r"""
Script CẬP NHẬT RIÊNG Âm thanh & Câu chuyện (Kiểu chơi chữ, bắt vần, siêu ngắn gọn).
Tự động commit và push sau mỗi 100 từ để lưu tiến trình trực tiếp lên GitHub.
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

# Số từ xử lý từ biến môi trường (0 = tất cả, 20 = chạy thử)
LIMIT_WORDS = int(os.getenv("LIMIT_WORDS", "20"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "ai_mnemonics.json")
DELAY_BETWEEN = float(os.getenv("DELAY_BETWEEN", "1.5"))

# ═══════════════════════════════════════════════════════════════════
#  HÀM TỰ ĐỘNG COMMIT & PUSH BẰNG GIT
# ═══════════════════════════════════════════════════════════════════
def git_commit_and_push(count):
    try:
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
        subprocess.run(["git", "add", OUTPUT_FILE], check=True)
        
        # Kiểm tra xem có thay đổi gì để commit không
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            msg = f"🔄 Auto-commit: Đã làm mới {count} từ vựng [skip ci]"
            subprocess.run(["git", "commit", "-m", msg], check=True)
            subprocess.run(["git", "push"], check=True)
            print(f"   🚀 [GIT] Đã push tiến trình ({count} từ) lên GitHub thành công!")
    except Exception as e:
        print(f"   ⚠️ Lỗi khi git commit/push: {e}")

# ═══════════════════════════════════════════════════════════════════
#  PROMPT DỄ NHỚ, CHƠI CHỮ, BẮT VẦN
# ═══════════════════════════════════════════════════════════════════
def build_story_prompt(zh, pinyin, vi):
    return f"""Từ cần nhớ: **{zh}** (pinyin: {pinyin}) - nghĩa: {vi}

Viết mẹo cực kỳ dễ nhớ bằng cách chơi chữ, hình ảnh tượng hình độc đáo hoặc bắt vần ngắn gọn (phần câu chuyện chỉ đúng 1 câu duy nhất):

📌 Âm thanh: [1 từ tiếng Việt đồng âm hoặc gần âm nhất với pinyin]
🎬 Câu chuyện: [1 câu chơi chữ hoặc hình ảnh phóng đại, hài hước, bắt vần giúp não nhớ ngay nghĩa "{vi}" thông qua âm thanh].

Output đúng 2 dòng có emoji 📌 và 🎬:"""

def generate_new_story(zh, pinyin, vi):
    if not API_KEY:
        return ""

    prompt = build_story_prompt(zh, pinyin, vi)
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200,
        )
        if response and response.choices:
            msg = response.choices[0].message
            if hasattr(msg, "content") and msg.content:
                return msg.content.strip()
    except Exception as e:
        print(f"      ⚠️ Lỗi API: {e}")
    return ""

def update_mnemonic_content(old_text, new_story_text):
    if not new_story_text:
        return old_text

    lines = old_text.split("\n")
    new_story_lines = new_story_text.split("\n")

    new_sound = next((l for l in new_story_lines if "📌" in l or "Âm thanh" in l), None)
    new_story = next((l for l in new_story_lines if "🎬" in l or "Câu chuyện" in l), None)

    updated_lines = []
    for line in lines:
        if ("📌" in line or "Âm thanh" in line) and new_sound:
            updated_lines.append(new_sound)
        elif ("🎬" in line or "Câu chuyện" in line) and new_story:
            updated_lines.append(new_story)
        else:
            updated_lines.append(line)

    return "\n".join(updated_lines)

def main():
    if not os.path.exists(OUTPUT_FILE):
        print(f"❌ Không tìm thấy file {OUTPUT_FILE}")
        return

    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_words = len(data)
    target_count = total_words if LIMIT_WORDS == 0 else min(LIMIT_WORDS, total_words)

    print(f"📦 Đã load {total_words} từ từ file JSON")
    print(f"🎯 MỤC TIÊU: Xử lý {target_count} từ {'(Chạy thử)' if LIMIT_WORDS > 0 else '(Tất cả)'}")
    print("🔄 Đang tiến hành làm mới Âm thanh & Câu chuyện...\n")

    updated_count = 0

    for idx, (key, content) in enumerate(data.items(), 1):
        if LIMIT_WORDS > 0 and idx > LIMIT_WORDS:
            print(f"\n🛑 Đã đạt giới hạn {LIMIT_WORDS} từ chạy thử. Dừng script!")
            break

        parts = key.split("|")
        zh = parts[-1] if len(parts) >= 3 else key
        
        pinyin_match = re.search(r'\(([^)]+)\)', content)
        pinyin = pinyin_match.group(1) if pinyin_match else ""

        print(f"[{idx}/{target_count}] Đang làm mới: {zh}...", flush=True)
        
        new_story = generate_new_story(zh, pinyin, "")
        if new_story:
            updated_content = update_mnemonic_content(content, new_story)
            data[key] = updated_content
            updated_count += 1
            print(f"   ✅ Xong {zh}", flush=True)
        else:
            print(f"   ❌ Thất bại, giữ nguyên {zh}", flush=True)

        # Lưu file JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

        # 🔄 TỰ ĐỘNG COMMIT MỖI KHI ĐẠT CỘT MỐC 100 TỪ
        if updated_count > 0 and updated_count % 100 == 0:
            print(f"\n📦 [CHECKPOINT] Đã đạt {updated_count} từ. Tiến hành commit & push lên GitHub...")
            git_commit_and_push(updated_count)

        time.sleep(DELAY_BETWEEN)

    print(f"\n🎉 HOÀN TẤT BƯỚC NÀY! Đã cập nhật câu chuyện mới cho {updated_count} từ.")

if __name__ == "__main__":
    main()
