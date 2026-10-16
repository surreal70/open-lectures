#!/usr/bin/env python3
"""Generate network scenario diagram: Client - Router - Server."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 700, 280
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
    font_mono = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 9)
except:
    font_title = font_label = font_text = font_small = font_mono = ImageFont.load_default()

# Colors
TITLE_COLOR = (70, 130, 180, 255)
TEXT_DARK = (60, 60, 60, 255)
TEXT_LIGHT = (245, 245, 245, 255)
BORDER_COLOR = (100, 100, 100, 255)
DEVICE_COLOR = (200, 210, 230, 255)
ROUTER_COLOR = (180, 200, 180, 255)
LINK_COLOR = (150, 150, 150, 255)
LAN_COLOR = (100, 149, 237, 180)

# Title
draw.text((WIDTH//2, 22), "Szenario: HTTP-Anfrage über Router", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Device positions
client_x, client_y = 80, 90
router_x, router_y = WIDTH//2, 90
server_x, server_y = WIDTH - 80, 90
device_w, device_h = 100, 60

def draw_device(x, y, w, h, label, sublabel, color, icon_type="pc"):
    """Draw a device box with icon-like appearance."""
    # Main box
    draw.rounded_rectangle([x - w//2, y - h//2, x + w//2, y + h//2], 
                          radius=8, fill=color, outline=BORDER_COLOR, width=2)
    
    # Icon area (top portion)
    icon_y = y - h//4
    if icon_type == "pc":
        # Monitor shape
        draw.rectangle([x - 15, icon_y - 10, x + 15, icon_y + 5], fill=(80, 80, 100, 255), outline=BORDER_COLOR)
        draw.rectangle([x - 5, icon_y + 5, x + 5, icon_y + 12], fill=(80, 80, 80, 255))
    elif icon_type == "router":
        # Router shape with arrows
        draw.rectangle([x - 18, icon_y - 8, x + 18, icon_y + 8], fill=(60, 100, 60, 255), outline=BORDER_COLOR)
        draw.text((x, icon_y), "⟷", font=font_label, fill=TEXT_LIGHT, anchor="mm")
    elif icon_type == "server":
        # Server rack shape
        draw.rectangle([x - 12, icon_y - 12, x + 12, icon_y + 10], fill=(70, 70, 90, 255), outline=BORDER_COLOR)
        for i in range(3):
            draw.rectangle([x - 9, icon_y - 10 + i*7, x + 9, icon_y - 5 + i*7], fill=(100, 100, 120, 255))
    
    # Labels below
    draw.text((x, y + h//2 - 12), label, font=font_label, fill=TEXT_DARK, anchor="mm")
    draw.text((x, y + h//2 + 2), sublabel, font=font_small, fill=(100, 100, 100, 255), anchor="mm")

# Draw devices
draw_device(client_x, client_y, device_w, device_h, "Client", "(Browser)", DEVICE_COLOR, "pc")
draw_device(router_x, router_y, device_w, device_h, "Router", "", ROUTER_COLOR, "router")
draw_device(server_x, server_y, device_w, device_h, "Server", "(Webserver)", DEVICE_COLOR, "server")

# Draw LAN connections
lan_y = client_y + device_h//2 + 25

# LAN 1 line
lan1_start = client_x
lan1_end = router_x
draw.line([(lan1_start, lan_y), (lan1_end, lan_y)], fill=LAN_COLOR, width=6)
draw.text(((lan1_start + lan1_end)//2, lan_y + 12), "LAN 1", font=font_small, fill=(70, 130, 180, 255), anchor="mm")

# Vertical connections to LAN 1
draw.line([(client_x, client_y + device_h//2), (client_x, lan_y)], fill=LINK_COLOR, width=2)
draw.line([(router_x, router_y + device_h//2), (router_x, lan_y)], fill=LINK_COLOR, width=2)

# LAN 2 line
lan2_start = router_x
lan2_end = server_x
draw.line([(lan2_start, lan_y), (lan2_end, lan_y)], fill=LAN_COLOR, width=6)
draw.text(((lan2_start + lan2_end)//2, lan_y + 12), "LAN 2", font=font_small, fill=(70, 130, 180, 255), anchor="mm")

# Vertical connection to LAN 2
draw.line([(server_x, server_y + device_h//2), (server_x, lan_y)], fill=LINK_COLOR, width=2)

# IP/MAC information below devices
info_y = lan_y + 35

# Client info
draw.text((client_x, info_y), "IP: 192.168.1.10", font=font_mono, fill=TEXT_DARK, anchor="mm")
draw.text((client_x, info_y + 12), "MAC: AA:AA:AA:...", font=font_mono, fill=(100, 100, 100, 255), anchor="mm")

# Router info (two interfaces)
draw.text((router_x, info_y), "eth0: 192.168.1.1", font=font_mono, fill=TEXT_DARK, anchor="mm")
draw.text((router_x, info_y + 12), "eth1: 10.0.0.1", font=font_mono, fill=TEXT_DARK, anchor="mm")

# Server info
draw.text((server_x, info_y), "IP: 10.0.0.5", font=font_mono, fill=TEXT_DARK, anchor="mm")
draw.text((server_x, info_y + 12), "MAC: CC:CC:CC:...", font=font_mono, fill=(100, 100, 100, 255), anchor="mm")

# Request info at bottom
request_y = HEIGHT - 30
draw.rectangle([40, request_y - 12, WIDTH - 40, request_y + 12], fill=(255, 250, 230, 255), outline=(200, 180, 100, 255), width=1)
draw.text((WIDTH//2, request_y), "Anfrage: GET http://10.0.0.5/index.html", font=font_mono, fill=(100, 80, 0, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/szenario_draft.png", "PNG")
print(f"Created: {output_dir}/szenario_draft.png")
