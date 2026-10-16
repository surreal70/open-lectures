#!/usr/bin/env python3
"""Generate encapsulation diagram showing step-by-step header addition."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 680, 450
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
except:
    font_title = font_label = font_text = font_small = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
TEXT_DARK = (60, 60, 60, 255)
TEXT_LIGHT = (245, 245, 245, 255)
BORDER_COLOR = (100, 100, 100, 255)
ARROW_COLOR = (80, 80, 80, 255)

# Header colors
HTTP_COLOR = (100, 149, 237, 255)    # Blue - Application data
TCP_COLOR = (60, 179, 113, 255)      # Green - Transport
IP_COLOR = (255, 165, 0, 255)        # Orange - Network
ETH_COLOR = (255, 99, 71, 255)       # Red - Data Link
FCS_COLOR = (220, 20, 60, 255)       # Crimson - FCS
BITS_COLOR = (180, 180, 180, 255)    # Gray - Physical

# Title
draw.text((WIDTH//2, 22), "Einkapselung (Encapsulation) – Client", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layout
LEFT_MARGIN = 100
ROW_HEIGHT = 70
START_Y = 55
SEGMENT_HEIGHT = 28

def draw_segment(x, y, w, h, text, color, size_text=None):
    """Draw a colored segment with text."""
    draw.rectangle([x, y, x + w, y + h], fill=color, outline=BORDER_COLOR, width=1)
    draw.text((x + w//2, y + h//2), text, font=font_small, fill=TEXT_LIGHT, anchor="mm")
    if size_text:
        draw.text((x + w//2, y + h + 8), size_text, font=font_small, fill=(120, 120, 120, 255), anchor="mm")

def draw_down_arrow(x, y1, y2, label=""):
    """Draw downward arrow with optional label."""
    draw.line([(x, y1), (x, y2 - 5)], fill=ARROW_COLOR, width=2)
    draw.polygon([(x, y2), (x - 5, y2 - 7), (x + 5, y2 - 7)], fill=ARROW_COLOR)
    if label:
        draw.text((x + 10, (y1 + y2)//2), label, font=font_small, fill=(100, 100, 100, 255), anchor="lm")

# Row 1: Application Layer - HTTP Data only
y = START_Y
draw.text((30, y + SEGMENT_HEIGHT//2), "Anwendung", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((30, y + SEGMENT_HEIGHT//2 + 12), "(Layer 7)", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

http_w = 200
draw_segment(LEFT_MARGIN + 120, y, http_w, SEGMENT_HEIGHT, "HTTP-Request (Daten)", HTTP_COLOR)
draw.text((LEFT_MARGIN + 120 + http_w + 10, y + SEGMENT_HEIGHT//2), "~200 Bytes", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Arrow down
arrow_x = LEFT_MARGIN + 180
draw_down_arrow(arrow_x, y + SEGMENT_HEIGHT + 5, y + ROW_HEIGHT - 5)

# Row 2: Transport Layer - TCP + Data
y += ROW_HEIGHT
draw.text((30, y + SEGMENT_HEIGHT//2), "Transport", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((30, y + SEGMENT_HEIGHT//2 + 12), "(Layer 4)", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

tcp_w = 50
draw_segment(LEFT_MARGIN + 70, y, tcp_w, SEGMENT_HEIGHT, "TCP", TCP_COLOR)
draw_segment(LEFT_MARGIN + 70 + tcp_w, y, http_w, SEGMENT_HEIGHT, "Daten", HTTP_COLOR)
draw.text((LEFT_MARGIN + 70 + tcp_w + http_w + 10, y + SEGMENT_HEIGHT//2), "+20 Bytes Header", font=font_small, fill=(60, 179, 113, 255), anchor="lm")

# Arrow down
draw_down_arrow(arrow_x, y + SEGMENT_HEIGHT + 5, y + ROW_HEIGHT - 5)

# Row 3: Network Layer - IP + TCP + Data
y += ROW_HEIGHT
draw.text((30, y + SEGMENT_HEIGHT//2), "Vermittlung", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((30, y + SEGMENT_HEIGHT//2 + 12), "(Layer 3)", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

ip_w = 40
draw_segment(LEFT_MARGIN + 30, y, ip_w, SEGMENT_HEIGHT, "IP", IP_COLOR)
draw_segment(LEFT_MARGIN + 30 + ip_w, y, tcp_w, SEGMENT_HEIGHT, "TCP", TCP_COLOR)
draw_segment(LEFT_MARGIN + 30 + ip_w + tcp_w, y, http_w, SEGMENT_HEIGHT, "Daten", HTTP_COLOR)
draw.text((LEFT_MARGIN + 30 + ip_w + tcp_w + http_w + 10, y + SEGMENT_HEIGHT//2), "+20 Bytes Header", font=font_small, fill=(255, 165, 0, 255), anchor="lm")

# Arrow down
draw_down_arrow(arrow_x, y + SEGMENT_HEIGHT + 5, y + ROW_HEIGHT - 5)

# Row 4: Data Link Layer - Eth + IP + TCP + Data + FCS
y += ROW_HEIGHT
draw.text((30, y + SEGMENT_HEIGHT//2), "Sicherung", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((30, y + SEGMENT_HEIGHT//2 + 12), "(Layer 2)", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

eth_w = 35
fcs_w = 30
draw_segment(LEFT_MARGIN - 5, y, eth_w, SEGMENT_HEIGHT, "Eth", ETH_COLOR)
draw_segment(LEFT_MARGIN - 5 + eth_w, y, ip_w, SEGMENT_HEIGHT, "IP", IP_COLOR)
draw_segment(LEFT_MARGIN - 5 + eth_w + ip_w, y, tcp_w, SEGMENT_HEIGHT, "TCP", TCP_COLOR)
draw_segment(LEFT_MARGIN - 5 + eth_w + ip_w + tcp_w, y, http_w, SEGMENT_HEIGHT, "Daten", HTTP_COLOR)
draw_segment(LEFT_MARGIN - 5 + eth_w + ip_w + tcp_w + http_w, y, fcs_w, SEGMENT_HEIGHT, "FCS", FCS_COLOR)
draw.text((LEFT_MARGIN - 5 + eth_w + ip_w + tcp_w + http_w + fcs_w + 10, y + SEGMENT_HEIGHT//2), "+14+4 Bytes", font=font_small, fill=(255, 99, 71, 255), anchor="lm")

# Arrow down
draw_down_arrow(arrow_x, y + SEGMENT_HEIGHT + 5, y + ROW_HEIGHT - 5)

# Row 5: Physical Layer - Bits
y += ROW_HEIGHT
draw.text((30, y + SEGMENT_HEIGHT//2 - 5), "Bitübertragung", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((30, y + SEGMENT_HEIGHT//2 + 7), "(Layer 1)", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

bits_w = eth_w + ip_w + tcp_w + http_w + fcs_w
draw.rectangle([LEFT_MARGIN - 5, y, LEFT_MARGIN - 5 + bits_w, y + SEGMENT_HEIGHT], fill=BITS_COLOR, outline=BORDER_COLOR, width=1)
draw.text((LEFT_MARGIN - 5 + bits_w//2, y + SEGMENT_HEIGHT//2), "01101001010101010101010101010101...", font=font_small, fill=TEXT_DARK, anchor="mm")
draw.text((LEFT_MARGIN - 5 + bits_w + 10, y + SEGMENT_HEIGHT//2), "Elektrische Signale", font=font_small, fill=(120, 120, 120, 255), anchor="lm")

# Summary box at bottom
summary_y = y + SEGMENT_HEIGHT + 20
draw.rectangle([30, summary_y, WIDTH - 30, summary_y + 35], fill=(245, 250, 255, 255), outline=(180, 200, 220, 255), width=1)
draw.text((WIDTH//2, summary_y + 10), "Gesamtgröße: 14 (Eth) + 20 (IP) + 20 (TCP) + ~200 (Daten) + 4 (FCS) = ~258 Bytes", 
          font=font_small, fill=TEXT_DARK, anchor="mm")
draw.text((WIDTH//2, summary_y + 24), "Jede Schicht fügt ihre Steuerinformationen (Header/Trailer) hinzu", 
          font=font_small, fill=(100, 100, 100, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/einkapselung_draft.png", "PNG")
print(f"Created: {output_dir}/einkapselung_draft.png")
