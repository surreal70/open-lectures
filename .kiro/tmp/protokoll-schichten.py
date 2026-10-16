#!/usr/bin/env python3
"""Generate protocol layer comparison diagram based on provided table."""

from PIL import Image, ImageDraw, ImageFont

# Canvas - sized to match content with symmetric margins (~30px on all sides)
WIDTH, HEIGHT = 720, 505
img = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 11)
    font_layer = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
except:
    font_title = font_header = font_layer = font_text = font_small = ImageFont.load_default()

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
HEADER_BG = (70, 70, 90, 255)
TEXT_LIGHT = (245, 245, 245, 255)
TEXT_DARK = (40, 40, 40, 255)
BORDER_COLOR = (100, 100, 100, 255)
TITLE_COLOR = (70, 130, 180, 255)
BRACKET_COLOR = (80, 80, 80, 255)

# Title
draw.text((WIDTH//2, 30), "Protokolle und Schichtenmodelle im Vergleich", font=font_title, fill=TITLE_COLOR, anchor="mm")

# Table layout
TABLE_LEFT = 50
TABLE_TOP = 55
ROW_HEIGHT = 50
HEADER_HEIGHT = 45

# Column definitions: (header_text, width) - reduced widths
columns = [
    ("OSI", 35),
    ("OSI-Schicht", 95),
    ("OSI\nEinordnung", 75),
    ("Protokoll-\nbeispiele", 85),
    ("Einheiten", 95),
    ("Kopplungs-\nelemente", 105),
    ("DOD\nEinordnung", 75),
    ("DOD/\nTCP/IP", 75),
]

# Calculate column positions
col_positions = []
x = TABLE_LEFT
for header, width in columns:
    col_positions.append((x, width))
    x += width

TABLE_WIDTH = x - TABLE_LEFT

# Draw header row
draw.rectangle([TABLE_LEFT, TABLE_TOP, TABLE_LEFT + TABLE_WIDTH, TABLE_TOP + HEADER_HEIGHT],
               fill=HEADER_BG, outline=BORDER_COLOR, width=2)

for i, (header, width) in enumerate(columns):
    x, w = col_positions[i]
    # Draw column separator
    if i > 0:
        draw.line([(x, TABLE_TOP), (x, TABLE_TOP + HEADER_HEIGHT)], fill=BORDER_COLOR, width=1)
    # Draw header text (handle multiline)
    lines = header.split('\n')
    y_offset = TABLE_TOP + HEADER_HEIGHT//2 - (len(lines) - 1) * 7
    for line in lines:
        draw.text((x + w//2, y_offset), line, font=font_header, fill=TEXT_LIGHT, anchor="mm")
        y_offset += 14

# Layer data: (osi_num, osi_name, osi_einordnung, protokolle, einheiten, kopplung, dod_einordnung, dod_name)
# Rows span multiple OSI layers where indicated
# Note: kopplung and dod_einordnung are now handled separately with spanning
layers = [
    # OSI 7,6,5 -> Anwendungsorientiert -> Anwendung (TCP/IP)
    ([7, 6, 5], 
     ["Anwendung\n(application)", "Darstellung\n(presentation)", "Sitzung\n(session)"],
     "Anwendungs-\norientiert",
     "DNS\nHTTPS",
     "Daten",
     None,  # handled separately - spans to Transport
     None,  # handled separately - spans to Vermittlung
     "Anwendung"),
    # OSI 4 -> Transportorientiert -> Transport
    ([4],
     ["Transport\n(transport)"],
     None,  # part of Transportorientiert span (1-4)
     "TCP\nUDP",
     "TCP=Segmente\nUDP=Datagramme",
     None,  # part of Gateway span
     None,  # part of Ende-zu-Ende span
     "Transport"),
    # OSI 3 -> Internet
    ([3],
     ["Vermittlung\n(network)"],
     None,  # part of Transportorientiert span
     "ICMP, IGMP\nIP, IPSec",
     "Pakete",
     "Router",
     None,  # part of Ende-zu-Ende span
     "Internet"),
    # OSI 2 -> Netzzugriff
    ([2],
     ["Sicherung\n(data link)"],
     None,  # part of Transportorientiert span
     "IEEE 802.3\nIEEE 802.5\nIEEE 802.11",
     "Rahmen\n(frames)",
     "Bridges\nSwitches",
     None,  # part of Punkt-zu-Punkt span (1-2)
     "Netzzugriff"),
    # OSI 1 -> Netzzugriff (part of)
    ([1],
     ["Bitübertragung\n(physical)"],
     None,  # part of Transportorientiert span
     "Ethernet PHY\nWLAN PHY",
     "Bits",
     "Repeater\nHubs",
     None,  # part of Punkt-zu-Punkt span
     ""),  # merged with Netzzugriff above
]

# Draw rows
current_y = TABLE_TOP + HEADER_HEIGHT

def draw_multiline_text(draw, x, y, text, font, fill, anchor="mm", line_height=12):
    """Draw multiline text centered."""
    lines = text.split('\n')
    total_height = (len(lines) - 1) * line_height
    start_y = y - total_height // 2
    for i, line in enumerate(lines):
        draw.text((x, start_y + i * line_height), line, font=font, fill=fill, anchor=anchor)

for layer_data in layers:
    osi_nums, osi_names, osi_einord, protokolle, einheiten, kopplung, dod_einord, dod_name = layer_data
    
    num_rows = len(osi_nums)
    total_row_height = num_rows * ROW_HEIGHT
    
    # Draw cells for each OSI layer in this group
    for idx, (osi_num, osi_name) in enumerate(zip(osi_nums, osi_names)):
        row_y = current_y + idx * ROW_HEIGHT
        color = LAYER_COLORS[osi_num]
        
        # OSI number cell
        x, w = col_positions[0]
        draw.rectangle([x, row_y, x + w, row_y + ROW_HEIGHT], fill=color, outline=BORDER_COLOR, width=1)
        draw.text((x + w//2, row_y + ROW_HEIGHT//2), str(osi_num), font=font_layer, fill=TEXT_LIGHT, anchor="mm")
        
        # OSI name cell
        x, w = col_positions[1]
        draw.rectangle([x, row_y, x + w, row_y + ROW_HEIGHT], fill=color, outline=BORDER_COLOR, width=1)
        draw_multiline_text(draw, x + w//2, row_y + ROW_HEIGHT//2, osi_name, font_small, TEXT_LIGHT)
    
    # Merged cells for the group (columns 2-7)
    merge_start_y = current_y
    merge_end_y = current_y + total_row_height
    
    # Get average color for merged cells background
    avg_color = LAYER_COLORS[osi_nums[len(osi_nums)//2]]
    light_bg = tuple(min(255, c + 60) for c in avg_color[:3]) + (255,)
    
    # Column 2: OSI Einordnung - skip for spanning cells
    x, w = col_positions[2]
    if osi_einord is not None:
        draw.rectangle([x, merge_start_y, x + w, merge_end_y], fill=light_bg, outline=BORDER_COLOR, width=1)
        draw_multiline_text(draw, x + w//2, (merge_start_y + merge_end_y)//2, osi_einord, font_text, TEXT_DARK)
    
    # Column 3: Protokollbeispiele
    x, w = col_positions[3]
    draw.rectangle([x, merge_start_y, x + w, merge_end_y], fill=light_bg, outline=BORDER_COLOR, width=1)
    draw_multiline_text(draw, x + w//2, (merge_start_y + merge_end_y)//2, protokolle, font_text, TEXT_DARK)
    
    # Column 4: Einheiten
    x, w = col_positions[4]
    draw.rectangle([x, merge_start_y, x + w, merge_end_y], fill=light_bg, outline=BORDER_COLOR, width=1)
    draw_multiline_text(draw, x + w//2, (merge_start_y + merge_end_y)//2, einheiten, font_text, TEXT_DARK)
    
    # Column 5: Kopplungselemente - skip for now, draw spanning cells after
    x, w = col_positions[5]
    # Only draw individual cells for rows that don't span
    if kopplung is not None:
        draw.rectangle([x, merge_start_y, x + w, merge_end_y], fill=light_bg, outline=BORDER_COLOR, width=1)
        draw_multiline_text(draw, x + w//2, (merge_start_y + merge_end_y)//2, kopplung, font_text, TEXT_DARK)
    
    # Column 6: DOD Einordnung - skip for now, draw spanning cells after
    x, w = col_positions[6]
    if dod_einord is not None:
        draw.rectangle([x, merge_start_y, x + w, merge_end_y], fill=light_bg, outline=BORDER_COLOR, width=1)
        draw_multiline_text(draw, x + w//2, (merge_start_y + merge_end_y)//2, dod_einord, font_text, TEXT_DARK)
    
    # Column 7: DOD/TCP-IP - handle spanning for Netzzugriff (OSI 2+1)
    x, w = col_positions[7]
    if dod_name:  # Only draw if there's a name (skip empty for OSI 1)
        draw.rectangle([x, merge_start_y, x + w, merge_end_y], fill=avg_color, outline=BORDER_COLOR, width=1)
        draw.text((x + w//2, (merge_start_y + merge_end_y)//2), dod_name, font=font_layer, fill=TEXT_LIGHT, anchor="mm")
    
    current_y += total_row_height

# Draw brackets on the left side for "Anwendungsorientiert" and "Transportorientiert"
# Left bracket for OSI 7-5 (Anwendungsorientiert)
bracket_x = TABLE_LEFT - 25
row1_top = TABLE_TOP + HEADER_HEIGHT
row1_bottom = row1_top + 3 * ROW_HEIGHT
draw.line([(bracket_x + 10, row1_top + 5), (bracket_x, row1_top + 5)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, row1_top + 5), (bracket_x, row1_bottom - 5)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, row1_bottom - 5), (bracket_x + 10, row1_bottom - 5)], fill=BRACKET_COLOR, width=2)

# Left bracket for OSI 4-2 (Transportorientiert)
row2_top = row1_bottom
row2_bottom = current_y
draw.line([(bracket_x + 10, row2_top + 5), (bracket_x, row2_top + 5)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, row2_top + 5), (bracket_x, row2_bottom - 5)], fill=BRACKET_COLOR, width=2)
draw.line([(bracket_x, row2_bottom - 5), (bracket_x + 10, row2_bottom - 5)], fill=BRACKET_COLOR, width=2)

# Outer border
draw.rectangle([TABLE_LEFT, TABLE_TOP, TABLE_LEFT + TABLE_WIDTH, current_y], outline=BORDER_COLOR, width=2)

# Now draw the spanning cells for Kopplungselemente and DOD Einordnung
# Calculate row positions
row_top = TABLE_TOP + HEADER_HEIGHT
row_anwendung_bottom = row_top + 3 * ROW_HEIGHT  # OSI 7,6,5
row_transport_bottom = row_anwendung_bottom + ROW_HEIGHT  # OSI 4
row_vermittlung_bottom = row_transport_bottom + ROW_HEIGHT  # OSI 3
row_sicherung_bottom = row_vermittlung_bottom + ROW_HEIGHT  # OSI 2
row_physical_bottom = row_sicherung_bottom + ROW_HEIGHT  # OSI 1

# OSI Einordnung: Anwendungsorientiert spans OSI 7-5
x, w = col_positions[2]
anw_top = row_top
anw_bottom = row_anwendung_bottom
avg_color_anw = (130, 140, 200, 255)
draw.rectangle([x, anw_top, x + w, anw_bottom], fill=avg_color_anw, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (anw_top + anw_bottom)//2, "Anwendungs-\norientiert", font_text, TEXT_DARK)

# OSI Einordnung: Transportorientiert spans OSI 4-1
trans_top = row_anwendung_bottom
trans_bottom = row_physical_bottom
avg_color_trans = (180, 160, 120, 255)
draw.rectangle([x, trans_top, x + w, trans_bottom], fill=avg_color_trans, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (trans_top + trans_bottom)//2, "Transport-\norientiert", font_text, TEXT_DARK)

# Kopplungselemente: Application Level Gateway spans OSI 7-4
x, w = col_positions[5]
gateway_top = row_top
gateway_bottom = row_transport_bottom
avg_color_gateway = (130, 160, 200, 255)  # blue-ish for app/transport
draw.rectangle([x, gateway_top, x + w, gateway_bottom], fill=avg_color_gateway, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (gateway_top + gateway_bottom)//2, "Application Level\nGateway, Proxy", font_text, TEXT_DARK)

# Kopplungselemente: Router spans OSI 3
router_top = row_transport_bottom
router_bottom = row_vermittlung_bottom
avg_color_router = (255, 200, 150, 255)  # orange-ish for network
draw.rectangle([x, router_top, x + w, router_bottom], fill=avg_color_router, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (router_top + router_bottom)//2, "Router", font_text, TEXT_DARK)

# Kopplungselemente: Bridges/Switches spans OSI 2
bridges_top = row_vermittlung_bottom
bridges_bottom = row_sicherung_bottom
avg_color_bridges = (255, 160, 140, 255)  # red-ish for data link
draw.rectangle([x, bridges_top, x + w, bridges_bottom], fill=avg_color_bridges, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (bridges_top + bridges_bottom)//2, "Bridges\nSwitches", font_text, TEXT_DARK)

# Kopplungselemente: Repeater/Hubs spans OSI 1
repeater_top = row_sicherung_bottom
repeater_bottom = row_physical_bottom
avg_color_repeater = (240, 100, 100, 255)  # crimson-ish for physical
draw.rectangle([x, repeater_top, x + w, repeater_bottom], fill=avg_color_repeater, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (repeater_top + repeater_bottom)//2, "Repeater\nHubs", font_text, TEXT_DARK)

# DOD Einordnung: Ende zu Ende spans OSI 7-3
x, w = col_positions[6]
e2e_top = row_top
e2e_bottom = row_vermittlung_bottom
avg_color_e2e = (150, 180, 200, 255)  # blue-green
draw.rectangle([x, e2e_top, x + w, e2e_bottom], fill=avg_color_e2e, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (e2e_top + e2e_bottom)//2, "Ende zu\nEnde", font_text, TEXT_DARK)

# DOD Einordnung: Punkt zu Punkt spans OSI 2-1
p2p_top = row_vermittlung_bottom
p2p_bottom = row_physical_bottom
avg_color_p2p = (255, 140, 120, 255)  # red-ish
draw.rectangle([x, p2p_top, x + w, p2p_bottom], fill=avg_color_p2p, outline=BORDER_COLOR, width=1)
draw_multiline_text(draw, x + w//2, (p2p_top + p2p_bottom)//2, "Punkt zu\nPunkt", font_text, TEXT_DARK)

# DOD/TCP-IP: Netzzugriff spans OSI 2-1
x, w = col_positions[7]
netz_top = row_vermittlung_bottom
netz_bottom = row_physical_bottom
avg_color_netz = (240, 80, 65, 255)  # red for data link/physical combined
draw.rectangle([x, netz_top, x + w, netz_bottom], fill=avg_color_netz, outline=BORDER_COLOR, width=1)
draw.text((x + w//2, (netz_top + netz_bottom)//2), "Netzzugriff", font=font_layer, fill=TEXT_LIGHT, anchor="mm")

# Legend
legend_y = current_y + 15
draw.text((WIDTH//2, legend_y), "OSI = 7 Schichten  |  DOD/TCP/IP = 4 Schichten", 
          font=font_small, fill=(120, 120, 120, 255), anchor="mm")

# Save
output_dir = "/media/andhue/Wissen/open-lectures/.kiro/tmp"
img.save(f"{output_dir}/protokoll-schichten_draft.png", "PNG")
print(f"Created: {output_dir}/protokoll-schichten_draft.png")
