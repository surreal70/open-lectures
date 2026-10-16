#!/usr/bin/env python3
"""Generate layer traversal diagram: Client → Router → Server."""

from PIL import Image, ImageDraw, ImageFont

# Canvas
WIDTH, HEIGHT = 820, 480
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
    font_label = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    font_layer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
except:
    font_title = font_label = font_layer = font_small = ImageFont.load_default()

# Colors
LAYER_COLORS = {
    7: (100, 149, 237, 255),   # Application - blue
    6: (123, 104, 238, 255),   # Presentation - slate blue  
    5: (138, 43, 226, 255),    # Session - violet
    4: (60, 179, 113, 255),    # Transport - green
    3: (255, 165, 0, 255),     # Network - orange
    2: (255, 99, 71, 255),     # Data Link - tomato
    1: (220, 20, 60, 255),     # Physical - crimson
}
TITLE_COLOR = (70, 130, 180, 255)
TEXT_LIGHT = (245, 245, 245, 255)
TEXT_DARK = (60, 60, 60, 255)
BORDER_COLOR = (100, 100, 100, 255)
ARROW_COLOR = (80, 80, 80, 255)
PHYSICAL_COLOR = (180, 180, 180, 255)

# Title
draw.text((WIDTH//2, 25), "Schichtendurchlauf: Client → Router → Server", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Layout
STACK_WIDTH = 140
STACK_HEIGHT = 210
LAYER_HEIGHT = 30
START_Y = 70

# Positions for three stacks
client_x = 80
router_x = WIDTH // 2 - STACK_WIDTH // 2
server_x = WIDTH - 80 - STACK_WIDTH

def draw_layer_stack(x, y, layers, label, sublabel=""):
    """Draw a stack of OSI layers."""
    # Label above
    draw.text((x + STACK_WIDTH//2, y - 20), label, font=font_label, fill=TEXT_DARK, anchor="mm")
    if sublabel:
        draw.text((x + STACK_WIDTH//2, y - 8), sublabel, font=font_small, fill=(120, 120, 120, 255), anchor="mm")
    
    # Draw layers
    for i, layer_num in enumerate(layers):
        ly = y + i * LAYER_HEIGHT
        color = LAYER_COLORS[layer_num]
        
        # Layer box
        draw.rounded_rectangle([x, ly, x + STACK_WIDTH, ly + LAYER_HEIGHT - 2], 
                              radius=4, fill=color, outline=BORDER_COLOR, width=1)
        
        # Layer text
        layer_names = {7: "7 Anwendung", 6: "6 Darstellung", 5: "5 Sitzung", 
                      4: "4 Transport", 3: "3 Vermittlung", 2: "2 Sicherung", 1: "1 Bitübertragung"}
        draw.text((x + STACK_WIDTH//2, ly + LAYER_HEIGHT//2 - 1), 
                 layer_names[layer_num], font=font_layer, fill=TEXT_LIGHT, anchor="mm")
    
    return y + len(layers) * LAYER_HEIGHT

# Draw Client stack (all 7 layers)
client_layers = [7, 6, 5, 4, 3, 2, 1]
client_bottom = draw_layer_stack(client_x, START_Y, client_layers, "CLIENT", "(Sender)")

# Draw Router stack (only layers 1-3)
router_layers = [3, 2, 1]
router_y = START_Y + 4 * LAYER_HEIGHT  # Align with layer 3 of client
router_bottom = draw_layer_stack(router_x, router_y, router_layers, "ROUTER", "(Vermittler)")

# Draw Server stack (all 7 layers)
server_layers = [7, 6, 5, 4, 3, 2, 1]
server_bottom = draw_layer_stack(server_x, START_Y, server_layers, "SERVER", "(Empfänger)")

# Draw arrows for logical connections (Ende-zu-Ende)
def draw_arrow(x1, y1, x2, y2, dashed=False, color=ARROW_COLOR):
    """Draw an arrow from (x1,y1) to (x2,y2)."""
    if dashed:
        # Dashed line
        dash_len = 8
        gap_len = 4
        dx = x2 - x1
        dy = y2 - y1
        length = (dx**2 + dy**2)**0.5
        dx, dy = dx/length, dy/length
        pos = 0
        while pos < length - 10:
            end_pos = min(pos + dash_len, length - 10)
            draw.line([(x1 + dx*pos, y1 + dy*pos), (x1 + dx*end_pos, y1 + dy*end_pos)], fill=color, width=2)
            pos = end_pos + gap_len
    else:
        draw.line([(x1, y1), (x2 - 8, y2)], fill=color, width=2)
    
    # Arrowhead
    arrow_size = 6
    draw.polygon([(x2, y2), (x2 - arrow_size, y2 - arrow_size//2), (x2 - arrow_size, y2 + arrow_size//2)], fill=color)

# Logical connection: Application layer (7) - Client to Server
app_y = START_Y + LAYER_HEIGHT // 2
draw_arrow(client_x + STACK_WIDTH, app_y, server_x, app_y, dashed=True, color=(100, 149, 237, 255))

# Logical connection: Transport layer (4) - Client to Server
trans_y = START_Y + 3 * LAYER_HEIGHT + LAYER_HEIGHT // 2
draw_arrow(client_x + STACK_WIDTH, trans_y, server_x, trans_y, dashed=True, color=(60, 179, 113, 255))

# Physical path arrows
# Client L3 → Router L3
l3_client_y = START_Y + 4 * LAYER_HEIGHT + LAYER_HEIGHT // 2
l3_router_y = router_y + LAYER_HEIGHT // 2
draw.line([(client_x + STACK_WIDTH, l3_client_y), (router_x, l3_router_y)], fill=ARROW_COLOR, width=2)
draw.polygon([(router_x, l3_router_y), (router_x - 6, l3_router_y - 3), (router_x - 6, l3_router_y + 3)], fill=ARROW_COLOR)

# Router L3 → Server L3
l3_server_y = START_Y + 4 * LAYER_HEIGHT + LAYER_HEIGHT // 2
draw.line([(router_x + STACK_WIDTH, l3_router_y), (server_x, l3_server_y)], fill=ARROW_COLOR, width=2)
draw.polygon([(server_x, l3_server_y), (server_x - 6, l3_server_y - 3), (server_x - 6, l3_server_y + 3)], fill=ARROW_COLOR)

# Client L2 → Router L2
l2_client_y = START_Y + 5 * LAYER_HEIGHT + LAYER_HEIGHT // 2
l2_router_y = router_y + LAYER_HEIGHT + LAYER_HEIGHT // 2
draw.line([(client_x + STACK_WIDTH, l2_client_y), (router_x, l2_router_y)], fill=ARROW_COLOR, width=2)
draw.polygon([(router_x, l2_router_y), (router_x - 6, l2_router_y - 3), (router_x - 6, l2_router_y + 3)], fill=ARROW_COLOR)

# Router L2 → Server L2
l2_server_y = START_Y + 5 * LAYER_HEIGHT + LAYER_HEIGHT // 2
draw.line([(router_x + STACK_WIDTH, l2_router_y), (server_x, l2_server_y)], fill=ARROW_COLOR, width=2)
draw.polygon([(server_x, l2_server_y), (server_x - 6, l2_server_y - 3), (server_x - 6, l2_server_y + 3)], fill=ARROW_COLOR)

# Physical layer connections (thick double lines)
l1_y = START_Y + 6 * LAYER_HEIGHT + LAYER_HEIGHT // 2
l1_router_y = router_y + 2 * LAYER_HEIGHT + LAYER_HEIGHT // 2

# LAN 1 (Client to Router)
lan1_y = max(l1_y, l1_router_y) + 25
draw.line([(client_x + STACK_WIDTH//2, l1_y + LAYER_HEIGHT//2), (client_x + STACK_WIDTH//2, lan1_y)], fill=PHYSICAL_COLOR, width=3)
draw.line([(router_x + STACK_WIDTH//2, l1_router_y + LAYER_HEIGHT//2), (router_x + STACK_WIDTH//2, lan1_y)], fill=PHYSICAL_COLOR, width=3)
draw.line([(client_x + STACK_WIDTH//2, lan1_y), (router_x + STACK_WIDTH//2, lan1_y)], fill=PHYSICAL_COLOR, width=3)
draw.text(((client_x + STACK_WIDTH//2 + router_x + STACK_WIDTH//2)//2, lan1_y + 12), "LAN 1", font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# LAN 2 (Router to Server)
draw.line([(router_x + STACK_WIDTH//2, lan1_y), (server_x + STACK_WIDTH//2, lan1_y)], fill=PHYSICAL_COLOR, width=3)
draw.line([(server_x + STACK_WIDTH//2, l1_y + LAYER_HEIGHT//2), (server_x + STACK_WIDTH//2, lan1_y)], fill=PHYSICAL_COLOR, width=3)
draw.text(((router_x + STACK_WIDTH//2 + server_x + STACK_WIDTH//2)//2, lan1_y + 12), "LAN 2", font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# Legend
legend_y = lan1_y + 35
legend_x = 40

draw.text((legend_x, legend_y), "Legende:", font=font_label, fill=TEXT_DARK, anchor="lm")

# Dashed line = logical
draw.line([(legend_x + 70, legend_y), (legend_x + 110, legend_y)], fill=(100, 149, 237, 255), width=2)
draw.line([(legend_x + 78, legend_y), (legend_x + 86, legend_y)], fill=(0, 0, 0, 0), width=2)  # gap effect
draw.line([(legend_x + 94, legend_y), (legend_x + 102, legend_y)], fill=(0, 0, 0, 0), width=2)
draw.text((legend_x + 120, legend_y), "Logische Verbindung (Ende-zu-Ende)", font=font_small, fill=TEXT_DARK, anchor="lm")

# Solid line = hop-by-hop
legend_y += 16
draw.line([(legend_x + 70, legend_y), (legend_x + 110, legend_y)], fill=ARROW_COLOR, width=2)
draw.text((legend_x + 120, legend_y), "Hop-by-Hop Verbindung", font=font_small, fill=TEXT_DARK, anchor="lm")

# Thick line = physical
legend_y += 16
draw.line([(legend_x + 70, legend_y), (legend_x + 110, legend_y)], fill=PHYSICAL_COLOR, width=3)
draw.text((legend_x + 120, legend_y), "Physisches Medium", font=font_small, fill=TEXT_DARK, anchor="lm")

# Info box on the right
info_x = 500
info_y = lan1_y + 35
draw.text((info_x, info_y), "Verarbeitung:", font=font_label, fill=TEXT_DARK, anchor="lm")
draw.text((info_x, info_y + 16), "• Client: Schicht 7→1 (Einkapselung)", font=font_small, fill=TEXT_DARK, anchor="lm")
draw.text((info_x, info_y + 30), "• Router: Nur Schicht 1-3", font=font_small, fill=TEXT_DARK, anchor="lm")
draw.text((info_x, info_y + 44), "• Server: Schicht 1→7 (Entkapselung)", font=font_small, fill=TEXT_DARK, anchor="lm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/schichtendurchlauf_draft.png", "PNG")
print(f"Created: {output_dir}/schichtendurchlauf_draft.png")
