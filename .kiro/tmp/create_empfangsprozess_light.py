#!/usr/bin/env python3
"""
Create empfangsprozess.png - Light theme matching schicht-*.png style.
Detailed server receive process per layer.
"""

from PIL import Image, ImageDraw, ImageFont

# Canvas - transparent background
WIDTH, HEIGHT = 680, 750
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
except:
    font_title = font_label = font_text = font_small = ImageFont.load_default()

# Colors
TEXT_DARK = (60, 60, 60, 255)
TEXT_LIGHT = (245, 245, 245, 255)
TEXT_DIM = (120, 120, 120, 255)
CHECK_COLOR = (60, 140, 60, 255)
BORDER_COLOR = (100, 100, 100, 255)
BOX_BG = (240, 245, 255, 255)
TITLE_BG = (70, 130, 180, 255)

# Layer colors
ETH_COLOR = (100, 149, 237, 255)
IP_COLOR = (147, 112, 219, 255)
TCP_COLOR = (60, 179, 113, 255)
HTTP_COLOR = (255, 165, 79, 255)

# Title
draw.rounded_rectangle([20, 10, 660, 45], radius=6, fill=TITLE_BG, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 27), "SERVER – ENTKAPSELUNG IM DETAIL", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Steps data
steps = [
    {
        "name": "SCHRITT 1: Netzzugangsschicht",
        "color": ETH_COLOR,
        "items": [
            "✓ Frame vom Medium empfangen (elektrische Signale)",
            "✓ Preamble/SFD erkennen (Synchronisation)",
            "✓ Destination MAC prüfen: CC:CC:CC:CC:CC:CC = eigene? → JA",
            "✓ FCS/CRC prüfen → Keine Übertragungsfehler",
            "✓ EtherType 0x0800 → IPv4, an IP-Stack übergeben",
            "✓ Ethernet-Header und FCS entfernen"
        ],
        "remaining": "Verbleibend: IP-Paket (240 Bytes)"
    },
    {
        "name": "SCHRITT 2: Internetschicht",
        "color": IP_COLOR,
        "items": [
            "✓ IP-Version prüfen: 4 → IPv4",
            "✓ Header Checksum validieren → OK",
            "✓ Destination IP prüfen: 10.0.0.5 = eigene? → JA",
            "✓ Protocol-Feld auslesen: 6 → TCP",
            "✓ IP-Header entfernen, an TCP-Stack übergeben"
        ],
        "remaining": "Verbleibend: TCP-Segment (220 Bytes)"
    },
    {
        "name": "SCHRITT 3: Transportschicht",
        "color": TCP_COLOR,
        "items": [
            "✓ TCP Checksum validieren → OK",
            "✓ Destination Port: 80 → HTTP-Dienst",
            "✓ Socket-Zuordnung: (TCP, 192.168.1.10, 52345, 10.0.0.5, 80)",
            "✓ Sequenznummer prüfen, ACK senden",
            "✓ TCP-Header entfernen, Daten an Port 80 übergeben"
        ],
        "remaining": "Verbleibend: HTTP-Request (~200 Bytes)"
    },
    {
        "name": "SCHRITT 4: Anwendungsschicht",
        "color": HTTP_COLOR,
        "items": [
            "✓ Webserver (Apache/nginx) empfängt Request",
            "✓ HTTP-Request parsen: GET /index.html",
            "✓ Datei /var/www/html/index.html laden",
            "✓ HTTP-Response generieren"
        ],
        "remaining": None
    }
]

y = 60
for step in steps:
    # Calculate section height
    item_count = len(step["items"])
    section_height = 35 + item_count * 16 + (20 if step["remaining"] else 10)
    
    # Section background
    draw.rounded_rectangle([20, y, 660, y + section_height], radius=6, fill=BOX_BG, outline=BORDER_COLOR, width=1)
    
    # Section title bar
    draw.rounded_rectangle([20, y, 660, y + 28], radius=6, fill=step["color"], outline=BORDER_COLOR, width=1)
    draw.rectangle([20, y + 20, 660, y + 28], fill=step["color"])
    draw.text((30, y + 14), step["name"], font=font_label, fill=TEXT_LIGHT, anchor="lm")
    
    # Items
    for i, item in enumerate(step["items"]):
        draw.text((35, y + 40 + i * 16), item, font=font_small, fill=CHECK_COLOR, anchor="lm")
    
    # Remaining info
    if step["remaining"]:
        rem_y = y + section_height - 15
        draw.text((35, rem_y), step["remaining"], font=font_small, fill=TEXT_DIM, anchor="lm")
    
    y += section_height + 10

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/empfangsprozess.png", "PNG")
print(f"Created: {output_dir}/empfangsprozess.png")

gray = img.convert('LA').convert('RGBA')
gray.save(f"{output_dir}/empfangsprozess_g.png", "PNG")
print(f"Created: {output_dir}/empfangsprozess_g.png")
