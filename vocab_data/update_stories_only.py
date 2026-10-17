# -*- coding: utf-8 -*-
r"""
Script CẬP NHẬT RIÊNG Âm thanh & Câu chuyện (Kiểu chơi chữ, bắt vần, cực kỳ dễ nhớ).
Không làm ảnh hưởng đến các phần Chiết tự, Ví dụ, Liên quan để tiết kiệm Quota.
"""
import os
import sys
import json
import time
import re
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "ai_mnemonics.json")
DELAY_BETWEEN = float(os.getenv("DELAY_BETWEEN", "1.5"))

# ═══════════════════════════════════════════════════════════════════
#  PROMPT DỄ NHỚ, CHƠI CHỮ, BẮT VẦN
# ═══════════════════════════════════════════════════════════════════
def build_story_prompt(zh, pinyin, vi):
    return f"""Từ cần nhớ: **{zh}** (pinyin: {pinyin}) - nghĩa: {vi}

Viết mẹo cực kỳ dễ nhớ bằng cách chơi chữ, hình ảnh tượng hình độc đáo hoặc bắt vần ngắn gọn (phần câu chuyện chỉ đúng 1 câu duy nhất):

📌 Âm thanh: [1 từ tiếng Việt đồng âm hoặc gần âm nhất với pinyin]
🎬 Câu chuyện: [1 câu chơi chữ hoặc hình ảnh phóng đại, hài hước, bắt vần giúp nad nhớ ngay nghĩa "{vi}" thông qua âm thanh].

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

    print(f"📦 Đã load {len(data)} từ từ {OUTPUT_FILE}")
    print("🔄 Đang tiến hành làm mới Âm thanh & Câu chuyện...\n")

    updated_count = 0

    for idx, (key, content) in enumerate(data.items(), 1):
        parts = key.split("|")
        zh = parts[-1] if len(parts) >= 3 else key
        
        pinyin_match = re.search(r'\(([^)]+)\)', content)
        pinyin = pinyin_match.group(1) if pinyin_match else ""

        print(f"[{idx}/{len(data)}] Đang làm mới: {zh}...")
        
        new_story = generate_new_story(zh, pinyin, "")
        if new_story:
            updated_content = update_mnemonic_content(content, new_story)
            data[key] = updated_content
            updated_count += 1
            print(f"   ✅ Xong {zh}")
        else:
            print(f"   ❌ Thất bại, giữ nguyên {zh}")

        # Ghi đè liên tục vào file JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

        time.sleep(DELAY_BETWEEN)

    print(f"\n🎉 HOÀN TẤT! Đã cập nhật câu chuyện mới cho {updated_count}/{len(data)} từ.")

if __name__ == "__main__":
    main()
