#!/usr/bin/env python3
"""Generate HTTPS protocol stack diagram in grayscale."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas
WIDTH, HEIGHT = 700, 620
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_layer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    font_mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 10)
except:
    font_title = font_layer = font_text = font_mono = ImageFont.load_default()

# Grayscale colors - different shades for layer distinction
TITLE_COLOR = (80, 80, 80, 255)
APP_COLOR = (60, 60, 60, 255)           # Darkest - Layer 4
TRANSPORT_COLOR = (90, 90, 90, 255)     # Dark - Layer 3
INTERNET_COLOR = (120, 120, 120, 255)   # Medium - Layer 2
NETACCESS_COLOR = (150, 150, 150, 255)  # Lightest - Layer 1
TEXT_LIGHT = (240, 240, 240, 255)
TEXT_DARK = (50, 50, 50, 255)
ARROW_COLOR = (100, 100, 100, 255)

# Title
draw.text((WIDTH//2, 40), "Protokoll-Stack: HTTPS-Anfrage", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Browser icon at top
draw.text((WIDTH//2, 75), "Browser", font=font_layer, fill=(120, 120, 120, 255), anchor="mm")

# Layout
start_y = 110
layer_height = 100
box_width = 550
box_x = (WIDTH - box_width) // 2

def draw_arrow_down(x, y1, y2):
    draw.line([(x, y1), (x, y2 - 8)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x, y2), (x - 6, y2 - 10), (x + 6, y2 - 10)], fill=ARROW_COLOR)

# Layer 4: Application
y = start_y
draw.rounded_rectangle([box_x, y, box_x + box_width, y + layer_height - 15], radius=8, 
                        fill=APP_COLOR, outline=(50, 50, 50, 255), width=2)
draw.text((box_x + 15, y + 15), "Anwendung: HTTP/2 + TLS 1.3", font=font_layer, fill=TEXT_LIGHT, anchor="lm")
draw.text((box_x + 15, y + 40), "GET /index.html HTTP/2", font=font_mono, fill=(200, 200, 200, 255), anchor="lm")
draw.text((box_x + 15, y + 58), "Host: example.com", font=font_mono, fill=(180, 180, 180, 255), anchor="lm")

draw_arrow_down(WIDTH//2, y + layer_height - 10, y + layer_height + 10)

# Layer 3: Transport
y = start_y + layer_height
draw.rounded_rectangle([box_x, y, box_x + box_width, y + layer_height - 15], radius=8, 
                        fill=TRANSPORT_COLOR, outline=(50, 50, 50, 255), width=2)
draw.text((box_x + 15, y + 15), "Transport: TCP", font=font_layer, fill=TEXT_LIGHT, anchor="lm")
draw.text((box_x + 15, y + 40), "Src Port: 52431  ->  Dst Port: 443", font=font_mono, fill=(200, 200, 200, 255), anchor="lm")
draw.text((box_x + 15, y + 58), "Seq: 1000, Ack: 1, Flags: PSH,ACK", font=font_mono, fill=(180, 180, 180, 255), anchor="lm")

draw_arrow_down(WIDTH//2, y + layer_height - 10, y + layer_height + 10)

# Layer 2: Internet
y = start_y + 2 * layer_height
draw.rounded_rectangle([box_x, y, box_x + box_width, y + layer_height - 15], radius=8, 
                        fill=INTERNET_COLOR, outline=(50, 50, 50, 255), width=2)
draw.text((box_x + 15, y + 15), "Internet: IPv4", font=font_layer, fill=TEXT_DARK, anchor="lm")
draw.text((box_x + 15, y + 40), "Src: 192.168.1.100  ->  Dst: 93.184.216.34", font=font_mono, fill=(60, 60, 60, 255), anchor="lm")
draw.text((box_x + 15, y + 58), "TTL: 64, Protocol: TCP (6)", font=font_mono, fill=(70, 70, 70, 255), anchor="lm")

draw_arrow_down(WIDTH//2, y + layer_height - 10, y + layer_height + 10)

# Layer 1: Network Access
y = start_y + 3 * layer_height
draw.rounded_rectangle([box_x, y, box_x + box_width, y + layer_height - 15], radius=8, 
                        fill=NETACCESS_COLOR, outline=(50, 50, 50, 255), width=2)
draw.text((box_x + 15, y + 15), "Netzzugang: Ethernet", font=font_layer, fill=TEXT_DARK, anchor="lm")
draw.text((box_x + 15, y + 40), "Src MAC: aa:bb:cc:dd:ee:ff", font=font_mono, fill=(60, 60, 60, 255), anchor="lm")
draw.text((box_x + 15, y + 58), "Dst MAC: 11:22:33:44:55:66 (Gateway)", font=font_mono, fill=(70, 70, 70, 255), anchor="lm")

# Network line at bottom
y_network = start_y + 4 * layer_height + 15
draw.line([(50, y_network), (650, y_network)], fill=(80, 80, 80, 255), width=3)
draw.text((WIDTH//2, y_network + 25), "Netzwerk", font=font_layer, fill=(100, 100, 100, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/https-protokollstack_draft.png", "PNG")
print(f"Created: {output_dir}/https-protokollstack_draft.png")
