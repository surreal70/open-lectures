#!/usr/bin/env python3
"""
Create paketfluss.png - Light theme matching schicht-*.png style.
Complete packet flow from client through router to server.
"""

from PIL import Image, ImageDraw, ImageFont

# Canvas - transparent background
WIDTH, HEIGHT = 720, 480
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
ARROW_COLOR = (70, 130, 180, 255)

# Layer colors
ETH_COLOR = (100, 149, 237, 255)
IP_COLOR = (147, 112, 219, 255)
TCP_COLOR = (60, 179, 113, 255)
HTTP_COLOR = (255, 165, 79, 255)

# Title
draw.rounded_rectangle([20, 10, 700, 45], radius=6, fill=TITLE_BG, outline=BORDER_COLOR, width=2)
draw.text((WIDTH//2, 27), "KOMPLETTER PAKETFLUSS", font=font_title, fill=TEXT_LIGHT, anchor="mm")

# Main box
draw.rounded_rectangle([20, 55, 700, 465], radius=8, fill=BOX_BG, outline=BORDER_COLOR, width=1)

# Column headers
cols = [("CLIENT", "192.168.1.10", 120), ("ROUTER", "192.168.1.1 / 10.0.0.1", 360), ("SERVER", "10.0.0.5", 600)]
for name, ip, x in cols:
    draw.text((x, 75), name, font=font_label, fill=TEXT_DARK, anchor="mm")
    draw.text((x, 90), ip, font=font_small, fill=TEXT_DIM, anchor="mm")

# CLIENT stack
def draw_layer_stack(x, y, layers, width=130):
    for i, (name, color, desc) in enumerate(layers):
        ly = y + i * 40
        draw.rounded_rectangle([x, ly, x + width, ly + 35], radius=4, fill=color, outline=BORDER_COLOR, width=1)
        draw.text((x + 5, ly + 12), name, font=font_small, fill=TEXT_LIGHT, anchor="lm")
        draw.text((x + 5, ly + 25), desc, font=font_small, fill=(255, 255, 255, 180), anchor="lm")

client_layers = [
    ("Application", HTTP_COLOR, "HTTP erstellen"),
    ("Transport", TCP_COLOR, "+TCP Header"),
    ("Internet", IP_COLOR, "+IP Header"),
    ("Net Access", ETH_COLOR, "+Eth Header")
]
draw_layer_stack(55, 110, client_layers)

# ROUTER (only 2 layers)
router_x, router_y = 295, 150
draw.rounded_rectangle([router_x, router_y, router_x + 130, router_y + 95], radius=6, fill=(220, 230, 245, 255), outline=BORDER_COLOR, width=2)
router_layers = [
    ("Internet", IP_COLOR, "Routing, TTL--"),
    ("Net Access", ETH_COLOR, "MAC ändern")
]
for i, (name, color, desc) in enumerate(router_layers):
    ly = router_y + 10 + i * 42
    draw.rounded_rectangle([router_x + 8, ly, router_x + 122, ly + 35], radius=4, fill=color, outline=BORDER_COLOR, width=1)
    draw.text((router_x + 15, ly + 12), name, font=font_small, fill=TEXT_LIGHT, anchor="lm")
    draw.text((router_x + 15, ly + 25), desc, font=font_small, fill=(255, 255, 255, 180), anchor="lm")

# SERVER stack
server_layers = [
    ("Application", HTTP_COLOR, "HTTP verarbeiten"),
    ("Transport", TCP_COLOR, "-TCP Header"),
    ("Internet", IP_COLOR, "-IP Header"),
    ("Net Access", ETH_COLOR, "-Eth Header")
]
draw_layer_stack(535, 110, server_layers)

# Arrows
arrow_y = 265
# Client -> Router
draw.line([(190, arrow_y), (290, arrow_y)], fill=ARROW_COLOR, width=3)
draw.polygon([(285, arrow_y - 6), (285, arrow_y + 6), (295, arrow_y)], fill=ARROW_COLOR)
draw.text((240, arrow_y - 12), "LAN 1", font=font_small, fill=TEXT_DIM, anchor="mm")

# Router -> Server
draw.line([(430, arrow_y), (530, arrow_y)], fill=ARROW_COLOR, width=3)
draw.polygon([(525, arrow_y - 6), (525, arrow_y + 6), (535, arrow_y)], fill=ARROW_COLOR)
draw.text((480, arrow_y - 12), "LAN 2", font=font_small, fill=TEXT_DIM, anchor="mm")

# Summary
draw.line([(35, 310), (685, 310)], fill=BORDER_COLOR, width=1)

summaries = [
    ("Client:", "Vollständige Einkapselung (alle 4 Schichten)"),
    ("Router:", "Nur Layer 1-3, IP unverändert, MAC ändert sich"),
    ("Server:", "Vollständige Entkapselung (alle 4 Schichten)")
]
for i, (label, desc) in enumerate(summaries):
    y = 330 + i * 22
    draw.text((50, y), label, font=font_label, fill=HTTP_COLOR, anchor="lm")
    draw.text((110, y), desc, font=font_text, fill=TEXT_DARK, anchor="lm")

# Legend
legend_y = 420
items = [(HTTP_COLOR, "Anwendung"), (TCP_COLOR, "Transport"), (IP_COLOR, "Internet"), (ETH_COLOR, "Netzzugang")]
lx = 100
for color, name in items:
    draw.rectangle([lx, legend_y, lx + 15, legend_y + 15], fill=color, outline=BORDER_COLOR, width=1)
    draw.text((lx + 22, legend_y + 8), name, font=font_small, fill=TEXT_DIM, anchor="lm")
    lx += 130

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/paketfluss.png", "PNG")
print(f"Created: {output_dir}/paketfluss.png")

gray = img.convert('LA').convert('RGBA')
gray.save(f"{output_dir}/paketfluss_g.png", "PNG")
print(f"Created: {output_dir}/paketfluss_g.png")
