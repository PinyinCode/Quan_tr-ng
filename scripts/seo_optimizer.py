import os
import re

file_path = "index.html"
if not os.path.exists(file_path):
    print(f"❌ Không tìm thấy file: {file_path}")
    exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"🔄 Đang xử lý file: {file_path}...")

SEO_CONFIG = {
    "title": "Học tiếng Trung · Văn phòng & Công xưởng",
    "description": "Học tiếng Trung giao tiếp Văn phòng & Công xưởng miễn phí. Tổng hợp từ vựng, mẫu câu thông dụng, luyện viết chữ Hán và phát âm chuẩn.",
    "keywords": "tiếng trung văn phòng, tiếng trung công xưởng, học tiếng trung miễn phí, từ vựng tiếng trung",
    "author": "Tuhoctiengtrung.org",
    "canonical_url": "https://tuhoctiengtrung.org/",
}

# ============================================================
# 1. QUÉT THƯ MỤC icons/ ĐỂ TÌM FILE PHÙ HỢP
# ============================================================
icon_dir = "icons"
favicon_tags = []

if os.path.isdir(icon_dir):
    icon_files = os.listdir(icon_dir)
    print(f"🔍 Tìm thấy {len(icon_files)} file trong thư mục '{icon_dir}/'")

    if "apple-touch-icon.png" in icon_files:
        favicon_tags.append('<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">')

    if "icon-192.png" in icon_files:
        favicon_tags.append('<link rel="icon" type="image/png" sizes="192x192" href="/icons/icon-192.png">')
    
    if "icon-512.png" in icon_files:
        favicon_tags.append('<link rel="icon" type="image/png" sizes="512x512" href="/icons/icon-512.png">')
    
    if not favicon_tags and "favicon.png" in icon_files:
        favicon_tags.append('<link rel="icon" type="image/png" href="/icons/favicon.png">')

    if os.path.exists("manifest.json"):
        favicon_tags.append('<link rel="manifest" href="/manifest.json">')
else:
    print(f"⚠️ Không tìm thấy thư mục '{icon_dir}/'. Bỏ qua bước chèn favicon.")

# ============================================================
# 2. XỬ LÝ CÁC THẺ SEO CƠ BẢN
# ============================================================
title_tag = f"<title>{SEO_CONFIG['title']}</title>"
if re.search(r'<title\b[^>]*>.*?</title>', content, re.IGNORECASE):
    content = re.sub(r'<title\b[^>]*>.*?</title>', title_tag, content, flags=re.IGNORECASE)
else:
    content = re.sub(r'(<head\b[^>]*>)', r'\1\n    ' + title_tag, content, flags=re.IGNORECASE)

desc_tag = f'<meta name="description" content="{SEO_CONFIG["description"]}">'
if re.search(r'<meta\s+name=["\']description["\'][^>]*>', content, re.IGNORECASE):
    content = re.sub(r'<meta\s+name=["\']description["\'][^>]*>', desc_tag, content, flags=re.IGNORECASE)
else:
    content = re.sub(r'(</title>)', r'\1\n    ' + desc_tag, content, flags=re.IGNORECASE)

# ============================================================
# 3. XÓA FAVICON CŨ VÀ CHÈN FAVICON MỚI TỪ icons/
# ============================================================
content = re.sub(r'<link[^>]*rel=["\'](shortcut )?(apple-touch-)?icon["\'][^>]*>\n?', '', content, flags=re.IGNORECASE)

if favicon_tags:
    favicon_html = "\n    ".join(favicon_tags)
    content = re.sub(r'(</title>)', r'\1\n    ' + favicon_html, content, flags=re.IGNORECASE)

# ============================================================
# 4. META PHỤ TRỢ & OPEN GRAPH
# ============================================================
extra_metas = f"""
    <meta name="keywords" content="{SEO_CONFIG['keywords']}">
    <meta name="author" content="{SEO_CONFIG['author']}">
    <link rel="canonical" href="{SEO_CONFIG['canonical_url']}">
    <meta property="og:title" content="{SEO_CONFIG['title']}">
    <meta property="og:description" content="{SEO_CONFIG['description']}">
    <meta property="og:url" content="{SEO_CONFIG['canonical_url']}">
    <meta property="og:type" content="website">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Học Tiếng Trung">
    <meta name="theme-color" content="#7c3aed">"""

if 'rel="canonical"' not in content:
    content = re.sub(r'(</head>)', extra_metas + r'\n  </head>', content, flags=re.IGNORECASE)

# ============================================================
# 5. CHỐNG SNIPPET BẰNG DATA-NOSNIPPET CHO BANNER
# ============================================================
banner_pattern = r'(<div\b[^>]*class\s*=\s*["\'][^"\']*quick-intro-banner[^"\']*["\'][^>]*)'
if re.search(banner_pattern, content, re.IGNORECASE):
    def add_nosnippet(match):
        tag = match.group(1)
        if 'data-nosnippet' not in tag:
            return tag + ' data-nosnippet'
        return tag
    content = re.sub(banner_pattern, add_nosnippet, content, flags=re.IGNORECASE)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Đã tối ưu SEO & Favicon thành công!")
