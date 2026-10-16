#!/usr/bin/env python3
"""Generate communication types diagram (Unicast, Broadcast, Multicast)."""

from PIL import Image, ImageDraw, ImageFont
import os

# Canvas
WIDTH, HEIGHT = 820, 490
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except:
    font_title = font_label = font_text = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
SENDER_COLOR = (60, 179, 113, 255)      # Green
RECEIVER_COLOR = (100, 149, 237, 255)   # Blue
INACTIVE_COLOR = (150, 150, 150, 255)   # Gray
ARROW_COLOR = (80, 80, 80, 255)
TEXT_LIGHT = (240, 240, 240, 255)

def draw_node(x, y, color, label):
    """Draw a network node."""
    draw.ellipse([x-20, y-20, x+20, y+20], fill=color, outline=(60, 60, 60, 255), width=2)
    draw.text((x, y), label, font=font_text, fill=TEXT_LIGHT, anchor="mm")

def draw_arrow(x1, y1, x2, y2):
    """Draw an arrow from (x1,y1) to (x2,y2)."""
    draw.line([(x1, y1), (x2, y2)], fill=ARROW_COLOR, width=2)
    # Simple arrowhead
    import math
    angle = math.atan2(y2-y1, x2-x1)
    arrow_len = 10
    draw.polygon([
        (x2, y2),
        (x2 - arrow_len * math.cos(angle - 0.4), y2 - arrow_len * math.sin(angle - 0.4)),
        (x2 - arrow_len * math.cos(angle + 0.4), y2 - arrow_len * math.sin(angle + 0.4)),
    ], fill=ARROW_COLOR)

# Title
draw.text((WIDTH//2, 45), "Kommunikationsarten", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layout
row_height = 100
start_y = 110
label_x = 130
sender_x = 250
receiver_x = [410, 510, 610]

# Row 1: Unicast (1:1)
y = start_y
draw.text((label_x, y + 20), "Unicast", font=font_label, fill=TITLE_COLOR, anchor="mm")
draw.text((label_x, y + 40), "(1:1)", font=font_text, fill=(120, 120, 120, 255), anchor="mm")

draw_node(sender_x, y + 30, SENDER_COLOR, "S")
draw_arrow(sender_x + 25, y + 30, receiver_x[0] - 25, y + 30)
draw_node(receiver_x[0], y + 30, RECEIVER_COLOR, "E")
draw_node(receiver_x[1], y + 30, INACTIVE_COLOR, "")
draw_node(receiver_x[2], y + 30, INACTIVE_COLOR, "")

# Row 2: Broadcast (1:n)
y = start_y + row_height
draw.text((label_x, y + 20), "Broadcast", font=font_label, fill=TITLE_COLOR, anchor="mm")
draw.text((label_x, y + 40), "(1:alle)", font=font_text, fill=(120, 120, 120, 255), anchor="mm")

draw_node(sender_x, y + 30, SENDER_COLOR, "S")
for rx in receiver_x:
    draw_arrow(sender_x + 25, y + 30, rx - 25, y + 30)
    draw_node(rx, y + 30, RECEIVER_COLOR, "E")

# Row 3: Multicast (1:m)
y = start_y + 2 * row_height
draw.text((label_x, y + 20), "Multicast", font=font_label, fill=TITLE_COLOR, anchor="mm")
draw.text((label_x, y + 40), "(1:Gruppe)", font=font_text, fill=(120, 120, 120, 255), anchor="mm")

draw_node(sender_x, y + 30, SENDER_COLOR, "S")
draw_arrow(sender_x + 25, y + 30, receiver_x[0] - 25, y + 30)
draw_node(receiver_x[0], y + 30, RECEIVER_COLOR, "E")
draw_node(receiver_x[1], y + 30, INACTIVE_COLOR, "")
draw_arrow(sender_x + 25, y + 30, receiver_x[2] - 25, y + 30)
draw_node(receiver_x[2], y + 30, RECEIVER_COLOR, "E")

# Legend at bottom
legend_y = start_y + 3 * row_height + 30
draw.line([(60, legend_y - 10), (720, legend_y - 10)], fill=(150, 150, 150, 255), width=1)

draw_node(170, legend_y + 15, SENDER_COLOR, "S")
draw.text((200, legend_y + 15), "= Sender", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

draw_node(340, legend_y + 15, RECEIVER_COLOR, "E")
draw.text((370, legend_y + 15), "= Empfänger (aktiv)", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

draw_node(550, legend_y + 15, INACTIVE_COLOR, "")
draw.text((580, legend_y + 15), "= nicht adressiert", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/kommunikationsarten_draft.png", "PNG")
print(f"Created: {output_dir}/kommunikationsarten_draft.png")
