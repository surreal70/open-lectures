#!/usr/bin/env python3
"""
Create entkapselung.png - Light theme matching schicht-*.png style.
Shows decapsulation process on server side.
"""

from PIL import Image, ImageDraw, ImageFont

# Canvas - transparent background
WIDTH, HEIGHT = 680, 520
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 9)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
except:
    font_title = font_label = font_text = font_mono = font_small = ImageFont.load_default()

# Colors matching schicht-*.png style
TEXT_DARK = (60, 60, 60, 255)
TEXT_LIGHT = (245, 245, 245, 255)
TEXT_DIM = (120, 120, 120, 255)
BORDER_COLOR = (100, 100, 100, 255)
BOX_BG = (240, 245, 255, 255)
TITLE_BG = (70, 130, 180, 255)

# Layer colors (matching the schicht-* files)
ETH_COLOR = (100, 149, 237, 255)    # Blue - Netzzugang
IP_COLOR = (147, 112, 219, 255)      # Purple - Internet  
TCP_COLOR = (60, 179, 113, 255)      # Green - Transport
HTTP_COLOR = (255, 165, 79, 255)     # Orange - Anwendung
FCS_COLOR = (205, 92, 92, 255)       # Red - FCS

# Removed/strikethrough colors
REMOVED_BG = (200, 200, 200, 150)

# Title
draw.rounded_rectangle([20, 10, 660, 45], radius=6, fill=TITLE_BG, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 27), "ENTKAPSELUNG (DECAPSULATION) – SERVER", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Main content box
draw.rounded_rectangle([20, 55, 660, 505], radius=8, fill=BOX_BG, outline=BORDER_COLOR, width=1)

# Bits on medium
draw.text((35, 70), "Empfangener Frame auf dem Medium:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((35, 88), "0110100101010101010101010101010101010101010101...", font=font_mono, fill=TEXT_DIM, anchor="lm")

def draw_frame_row(y, label, segments, arrow=True):
    """Draw a frame row with segments."""
    if arrow:
        # Down arrow
        arrow_x = 340
        draw.polygon([(arrow_x-6, y-20), (arrow_x+6, y-20), (arrow_x, y-8)], fill=TEXT_DIM)
        draw.line([(arrow_x, y-35), (arrow_x, y-20)], fill=TEXT_DIM, width=2)
    
    # Label
    draw.text((35, y - 5), label, font=font_small, fill=TEXT_DIM, anchor="lm")
    
    # Frame background
    draw.rounded_rectangle([30, y + 5, 650, y + 50], radius=4, fill=(255, 255, 255, 255), outline=BORDER_COLOR, width=1)
    
    # Segments
    x = 35
    for seg_w, seg_label, seg_color, removed in segments:
        if removed:
            # Strikethrough style for removed headers
            draw.rectangle([x, y + 10, x + seg_w, y + 45], fill=REMOVED_BG, outline=BORDER_COLOR, width=1)
            draw.text((x + seg_w//2, y + 27), seg_label, font=font_small, fill=TEXT_DIM, anchor="mm")
            # Strikethrough line
            draw.line([(x + 5, y + 27), (x + seg_w - 5, y + 27)], fill=(150, 150, 150, 255), width=1)
        else:
            draw.rectangle([x, y + 10, x + seg_w, y + 45], fill=seg_color, outline=BORDER_COLOR, width=1)
            draw.text((x + seg_w//2, y + 27), seg_label, font=font_small, fill=TEXT_LIGHT, anchor="mm")
        x += seg_w + 3

# Row 1: Full frame with all headers
y1 = 115
draw_frame_row(y1, "Netzzugangsschicht entfernt Ethernet-Header/Trailer", [
    (70, "Eth-Hdr", ETH_COLOR, False),
    (70, "IP-Hdr", IP_COLOR, False),
    (70, "TCP-Hdr", TCP_COLOR, False),
    (350, "HTTP-Request", HTTP_COLOR, False),
    (50, "FCS", FCS_COLOR, False),
], arrow=False)

# Row 2: IP layer removes Eth
y2 = 205
draw_frame_row(y2, "Internetschicht entfernt IP-Header", [
    (70, "IP-Hdr", IP_COLOR, True),
    (70, "TCP-Hdr", TCP_COLOR, False),
    (420, "HTTP-Request", HTTP_COLOR, False),
])

# Row 3: Transport layer removes IP
y3 = 295
draw_frame_row(y3, "Transportschicht entfernt TCP-Header", [
    (70, "TCP-Hdr", TCP_COLOR, True),
    (490, "HTTP-Request", HTTP_COLOR, False),
])

# Row 4: Application layer gets pure data
y4 = 385
draw_frame_row(y4, "Anwendungsschicht erhält reine Nutzdaten", [
    (560, "HTTP-Request: \"GET /index.html HTTP/1.1...\"", HTTP_COLOR, False),
])

# Result text
draw.text((WIDTH//2, 470), "→ Webserver verarbeitet HTTP-Request", font=font_label, fill=(60, 140, 60, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/entkapselung.png", "PNG")
print(f"Created: {output_dir}/entkapselung.png")

# Grayscale version
gray = img.convert('LA').convert('RGBA')
gray.save(f"{output_dir}/entkapselung_g.png", "PNG")
print(f"Created: {output_dir}/entkapselung_g.png")
