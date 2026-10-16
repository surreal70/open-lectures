#!/usr/bin/env python3
"""Generate communication types diagram - classic horizontal layout."""

from PIL import Image, ImageDraw, ImageFont
import os
import math

# Canvas
WIDTH, HEIGHT = 850, 550
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
except:
    font_title = font_label = font_text = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
SENDER_COLOR = (60, 179, 113, 255)      # Green
RECEIVER_COLOR = (100, 149, 237, 255)   # Blue (active)
INACTIVE_COLOR = (180, 180, 180, 255)   # Gray (not addressed)
ARROW_COLOR = (80, 80, 80, 255)
TEXT_LIGHT = (245, 245, 245, 255)
CLOUD_COLOR = (230, 230, 230, 100)

def draw_computer(x, y, color, active=True):
    """Draw a simple computer/host icon."""
    # Monitor
    draw.rounded_rectangle([x-18, y-15, x+18, y+8], radius=3, fill=color, outline=(60, 60, 60, 255), width=2)
    # Stand
    draw.rectangle([x-5, y+8, x+5, y+15], fill=color, outline=(60, 60, 60, 255))
    # Base
    draw.rectangle([x-12, y+15, x+12, y+18], fill=color, outline=(60, 60, 60, 255))

def draw_arrow(x1, y1, x2, y2, active=True):
    """Draw an arrow."""
    color = ARROW_COLOR if active else (200, 200, 200, 255)
    width = 2 if active else 1
    
    # Calculate direction
    angle = math.atan2(y2-y1, x2-x1)
    
    # Shorten to not overlap icons
    x1_adj = x1 + 25 * math.cos(angle)
    y1_adj = y1 + 25 * math.sin(angle)
    x2_adj = x2 - 30 * math.cos(angle)
    y2_adj = y2 - 30 * math.sin(angle)
    
    draw.line([(x1_adj, y1_adj), (x2_adj, y2_adj)], fill=color, width=width)
    
    # Arrowhead
    if active:
        arrow_len = 12
        draw.polygon([
            (x2_adj + 8 * math.cos(angle), y2_adj + 8 * math.sin(angle)),
            (x2_adj - arrow_len * math.cos(angle - 0.35), y2_adj - arrow_len * math.sin(angle - 0.35)),
            (x2_adj - arrow_len * math.cos(angle + 0.35), y2_adj - arrow_len * math.sin(angle + 0.35)),
        ], fill=color)

# Title
draw.text((WIDTH//2, 40), "Kommunikationsarten", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layout - 3 rows
row_height = 140
start_y = 100
sender_x = 120
receiver_base_x = 550
receiver_spread = 70  # vertical spacing between receivers

# Define scenarios
scenarios = [
    ("Unicast", "1 : 1", "One-to-One", [True, False, False, False]),
    ("Broadcast", "1 : alle", "One-to-All", [True, True, True, True]),
    ("Multicast", "1 : Gruppe", "One-to-Many", [True, False, True, True]),
]

for row, (name, relation, english, active_receivers) in enumerate(scenarios):
    y_center = start_y + row * row_height + 50
    
    # Row label (left)
    draw.text((50, y_center - 20), name, font=font_label, fill=TITLE_COLOR, anchor="lm")
    draw.text((50, y_center + 5), f"({relation})", font=font_small, fill=(120, 120, 120, 255), anchor="lm")
    
    # Sender
    draw_computer(sender_x, y_center, SENDER_COLOR)
    draw.text((sender_x, y_center + 35), "Sender", font=font_small, fill=(100, 100, 100, 255), anchor="mm")
    
    # Cloud/Network area background
    cloud_x = 350
    cloud_y = y_center - 55
    cloud_w = 430
    cloud_h = 110
    draw.rounded_rectangle([cloud_x, cloud_y, cloud_x + cloud_w, cloud_y + cloud_h], 
                           radius=20, fill=CLOUD_COLOR, outline=(200, 200, 200, 255), width=1)
    
    # Receivers (in a horizontal-ish group)
    receiver_positions = [
        (receiver_base_x - 50, y_center - 35),
        (receiver_base_x + 50, y_center - 35),
        (receiver_base_x - 50, y_center + 35),
        (receiver_base_x + 50, y_center + 35),
    ]
    
    for i, ((rx, ry), is_active) in enumerate(zip(receiver_positions, active_receivers)):
        color = RECEIVER_COLOR if is_active else INACTIVE_COLOR
        draw_computer(rx, ry, color, is_active)
        
        # Draw arrow from sender to active receiver
        if is_active:
            draw_arrow(sender_x, y_center, rx, ry, True)
    
    # Label for receiver group
    draw.text((receiver_base_x + 130, y_center), "Empfänger", font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Legend at very bottom
legend_y = start_y + 3 * row_height + 30
draw.line([(40, legend_y), (810, legend_y)], fill=(180, 180, 180, 255), width=1)

# Sender legend
draw_computer(100, legend_y + 35, SENDER_COLOR)
draw.text((130, legend_y + 35), "= Sender", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

# Active receiver legend
draw_computer(320, legend_y + 35, RECEIVER_COLOR)
draw.text((350, legend_y + 35), "= adressierter Empfänger", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

# Inactive receiver legend
draw_computer(600, legend_y + 35, INACTIVE_COLOR)
draw.text((630, legend_y + 35), "= nicht adressiert", font=font_text, fill=(100, 100, 100, 255), anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/kommunikationsarten_draft.png", "PNG")
print(f"Created: {output_dir}/kommunikationsarten_draft.png")
