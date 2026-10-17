#!/usr/bin/env python3
"""
Create pdu.png - Light theme matching schicht-*.png style.
PDU (Protocol Data Unit) names per layer.
"""

from PIL import Image, ImageDraw, ImageFont

# Canvas - transparent background
WIDTH, HEIGHT = 680, 460
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
BORDER_COLOR = (100, 100, 100, 255)
BOX_BG = (240, 245, 255, 255)
TITLE_BG = (70, 130, 180, 255)

# Layer colors
ETH_COLOR = (100, 149, 237, 255)
IP_COLOR = (147, 112, 219, 255)
TCP_COLOR = (60, 179, 113, 255)
HTTP_COLOR = (255, 165, 79, 255)
BITS_COLOR = (205, 92, 92, 255)

# Title
draw.rounded_rectangle([20, 10, 660, 45], radius=6, fill=TITLE_BG, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 27), "PDU (Protocol Data Unit) pro Schicht", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Main box
draw.rounded_rectangle([20, 55, 660, 445], radius=8, fill=BOX_BG, outline=BORDER_COLOR, width=1)

# Table headers
headers = [("DoD-Schicht", 45), ("PDU-Name", 180), ("Enthält", 420)]
for name, x in headers:
    draw.text((x, 75), name, font=font_label, fill=TEXT_DIM, anchor="lm")

draw.line([(35, 88), (645, 88)], fill=BORDER_COLOR, width=1)

# Table rows
rows = [
    ("Anwendung", "Daten / Message", "Nutzdaten", HTTP_COLOR),
    ("Transport", "Segment (TCP) / Datagramm (UDP)", "TCP/UDP-Header + Daten", TCP_COLOR),
    ("Internet", "Paket / IP-Datagramm", "IP-Header + Segment", IP_COLOR),
    ("Netzzugang", "Frame / Rahmen", "Eth-Header + Paket + FCS", ETH_COLOR),
    ("(Physikalisch)", "Bits", "0 und 1 auf Medium", BITS_COLOR),
]

y = 98
row_height = 32
for layer, pdu, contains, color in rows:
    # Color indicator
    draw.rectangle([35, y + 5, 42, y + row_height - 5], fill=color, outline=BORDER_COLOR, width=1)
    
    # Layer name
    draw.text((50, y + row_height//2), layer, font=font_label, fill=TEXT_DARK, anchor="lm")
    
    # PDU name
    draw.text((180, y + row_height//2), pdu, font=font_text, fill=color, anchor="lm")
    
    # Contains
    draw.text((420, y + row_height//2), contains, font=font_small, fill=TEXT_DIM, anchor="lm")
    
    y += row_height

# Separator
draw.line([(35, y + 10), (645, y + 10)], fill=BORDER_COLOR, width=1)

# Visual encapsulation diagram
encap_y = y + 30
draw.text((45, encap_y), "Visuelle Einkapselung:", font=font_label, fill=TEXT_DARK, anchor="lm")

# Nested boxes
boxes = [
    (40, encap_y + 25, 600, 100, ETH_COLOR, "Frame"),
    (55, encap_y + 38, 530, 74, IP_COLOR, "Paket"),
    (70, encap_y + 51, 460, 48, TCP_COLOR, "Segment"),
    (85, encap_y + 64, 390, 22, HTTP_COLOR, "Daten"),
]

for x, by, w, h, color, label in boxes:
    # Semi-transparent fill
    overlay = Image.new('RGBA', (w, h), (*color[:3], 40))
    img.paste(overlay, (x, by), overlay)
    draw.rounded_rectangle([x, by, x + w, by + h], radius=4, outline=color, width=2)

# Labels
draw.text((48, encap_y + 115), "Eth", font=font_small, fill=ETH_COLOR, anchor="lm")
draw.text((63, encap_y + 102), "IP", font=font_small, fill=IP_COLOR, anchor="lm")
draw.text((78, encap_y + 89), "TCP", font=font_small, fill=TCP_COLOR, anchor="lm")
draw.text((270, encap_y + 75), "Daten", font=font_small, fill=HTTP_COLOR, anchor="mm")
draw.text((590, encap_y + 115), "FCS", font=font_small, fill=ETH_COLOR, anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/pdu.png", "PNG")
print(f"Created: {output_dir}/pdu.png")

gray = img.convert('LA').convert('RGBA')
gray.save(f"{output_dir}/pdu_g.png", "PNG")
print(f"Created: {output_dir}/pdu_g.png")
