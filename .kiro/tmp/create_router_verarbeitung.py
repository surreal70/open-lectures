#!/usr/bin/env python3
"""
Create router-verarbeitung.png - Router processing diagram showing
receive, process, and send steps with detailed explanations.
"""

import subprocess
from pathlib import Path
from lxml import etree
from PIL import Image

NSMAP = {None: "http://www.w3.org/2000/svg"}

def create_svg_root(width, height):
    """Create SVG root element."""
    root = etree.Element("svg", nsmap=NSMAP)
    root.set("width", str(width))
    root.set("height", str(height))
    root.set("viewBox", f"0 0 {width} {height}")
    
    # Black background
    etree.SubElement(root, "rect", x="0", y="0", width=str(width), height=str(height), fill="#1A1A1A")
    return root

def add_definitions(root):
    """Add defs for gradients etc."""
    return etree.SubElement(root, "defs")

def svg_to_string(root):
    """Convert SVG element to string."""
    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8").decode('utf-8')

def export_png(svg_path, png_path, width, height):
    """Export SVG to PNG using cairosvg."""
    import cairosvg
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width, output_height=height)

def create_grayscale_version(color_path, gray_path):
    """Create grayscale version of PNG."""
    img = Image.open(color_path)
    if img.mode == 'RGBA':
        gray = img.convert('LA')
        gray = gray.convert('RGBA')
    else:
        gray = img.convert('L').convert('RGB')
    gray.save(gray_path)

def create_router_verarbeitung():
    """Create the router processing diagram."""
    
    width = 900
    height = 850
    
    root = create_svg_root(width, height)
    defs = add_definitions(root)
    
    # Colors - theme-agnostic
    title_color = "#E8E8E8"
    text_color = "#CCCCCC"
    text_dark = "#333333"
    box_fill = "#2D2D2D"
    box_stroke = "#4A9EFF"
    section_fill = "#1E3A5F"
    check_color = "#4ADE80"
    highlight_color = "#FFB347"
    frame_fill = "#3D3D3D"
    arrow_color = "#4A9EFF"
    
    from lxml import etree
    NSMAP = {None: "http://www.w3.org/2000/svg"}
    
    # Title
    title = etree.SubElement(root, "text", x=str(width//2), y="35",
                             fill=title_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "18",
                                 "font-weight": "bold",
                                 "text-anchor": "middle"
                             })
    title.text = "ROUTER – VERARBEITUNG"
    
    # Main container
    etree.SubElement(root, "rect", x="20", y="55", width="860", height="780",
                     fill=box_fill, stroke=box_stroke, rx="8",
                     attrib={"stroke-width": "2"})
    
    # === EMPFANG SECTION ===
    etree.SubElement(root, "rect", x="35", y="70", width="830", height="100",
                     fill=section_fill, stroke=box_stroke, rx="5",
                     attrib={"stroke-width": "1"})
    
    recv_title = etree.SubElement(root, "text", x="50", y="95",
                                  fill=highlight_color, attrib={
                                      "font-family": "monospace",
                                      "font-size": "14",
                                      "font-weight": "bold"
                                  })
    recv_title.text = "EMPFANG auf LAN 1 (192.168.1.0/24):"
    
    # Frame visualization - receive
    etree.SubElement(root, "rect", x="50", y="115", width="800", height="40",
                     fill=frame_fill, stroke="#666666", rx="3")
    
    # Frame segments
    segments = [
        (50, 70, "BB:BB", "#4A9EFF"),
        (120, 70, "AA:AA", "#9B59B6"),
        (190, 70, "0x0800", "#2ECC71"),
        (260, 460, "IP-Paket", "#F39C12"),
        (720, 60, "FCS", "#E74C3C")
    ]
    
    for x, w, label, color in segments:
        etree.SubElement(root, "rect", x=str(x), y="120", width=str(w), height="30",
                         fill=color, stroke="#333333", rx="2",
                         attrib={"fill-opacity": "0.3", "stroke-width": "1"})
        txt = etree.SubElement(root, "text", x=str(x + w//2), y="140",
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "11",
                                   "text-anchor": "middle"
                               })
        txt.text = label
    
    # === SCHRITT 1: Netzzugangsschicht ===
    y_start = 185
    etree.SubElement(root, "rect", x="35", y=str(y_start), width="830", height="130",
                     fill=section_fill, stroke=box_stroke, rx="5",
                     attrib={"stroke-width": "1"})
    
    step1_title = etree.SubElement(root, "text", x="50", y=str(y_start + 20),
                                   fill=highlight_color, attrib={
                                       "font-family": "monospace",
                                       "font-size": "13",
                                       "font-weight": "bold"
                                   })
    step1_title.text = "Schritt 1: Netzzugangsschicht (Layer 2)"
    
    step1_items = [
        "✓ FCS prüfen → OK",
        "✓ Destination MAC = eigene MAC (BB:BB:BB:BB:BB:BB)? → JA",
        "✓ Ethernet-Header und FCS entfernen",
        "✓ EtherType 0x0800 → an IPv4-Verarbeitung übergeben"
    ]
    
    for i, item in enumerate(step1_items):
        txt = etree.SubElement(root, "text", x="70", y=str(y_start + 45 + i*22),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "12"
                               })
        txt.text = item
    
    # === SCHRITT 2: Internetschicht ===
    y_start = 325
    etree.SubElement(root, "rect", x="35", y=str(y_start), width="830", height="230",
                     fill=section_fill, stroke=box_stroke, rx="5",
                     attrib={"stroke-width": "1"})
    
    step2_title = etree.SubElement(root, "text", x="50", y=str(y_start + 20),
                                   fill=highlight_color, attrib={
                                       "font-family": "monospace",
                                       "font-size": "13",
                                       "font-weight": "bold"
                                   })
    step2_title.text = "Schritt 2: Internetschicht (Layer 3)"
    
    step2_items = [
        "✓ IP-Header analysieren: Src 192.168.1.10 → Dst 10.0.0.5",
        "✓ Bin ich das Ziel (10.0.0.5)? → NEIN, weiterleiten",
        "✓ TTL dekrementieren: 64 → 63",
        "✓ Header Checksum neu berechnen"
    ]
    
    for i, item in enumerate(step2_items):
        txt = etree.SubElement(root, "text", x="70", y=str(y_start + 45 + i*20),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "12"
                               })
        txt.text = item
    
    # Routing table
    rt_y = y_start + 125
    etree.SubElement(root, "rect", x="70", y=str(rt_y), width="500", height="85",
                     fill="#1A1A2E", stroke="#4A9EFF", rx="3",
                     attrib={"stroke-width": "1"})
    
    rt_title = etree.SubElement(root, "text", x="85", y=str(rt_y + 18),
                                fill=check_color, attrib={
                                    "font-family": "monospace",
                                    "font-size": "11",
                                    "font-weight": "bold"
                                })
    rt_title.text = "✓ Routing-Tabelle konsultieren:"
    
    rt_headers = ["Ziel", "Gateway", "Interface"]
    rt_x = [100, 240, 380]
    for i, h in enumerate(rt_headers):
        txt = etree.SubElement(root, "text", x=str(rt_x[i]), y=str(rt_y + 38),
                               fill="#888888", attrib={
                                   "font-family": "monospace",
                                   "font-size": "10"
                               })
        txt.text = h
    
    rt_rows = [
        ("10.0.0.0/24", "directly", "eth1 (LAN 2)"),
        ("192.168.1.0/24", "directly", "eth0 (LAN 1)"),
        ("0.0.0.0/0", "ISP-Router", "eth2")
    ]
    
    for i, row in enumerate(rt_rows):
        for j, cell in enumerate(row):
            color = highlight_color if i == 0 else text_color
            txt = etree.SubElement(root, "text", x=str(rt_x[j]), y=str(rt_y + 55 + i*14),
                                   fill=color, attrib={
                                       "font-family": "monospace",
                                       "font-size": "10"
                                   })
            txt.text = cell
    
    # Match result
    match_txt = etree.SubElement(root, "text", x="590", y=str(rt_y + 50),
                                 fill=check_color, attrib={
                                     "font-family": "monospace",
                                     "font-size": "11"
                                 })
    match_txt.text = "→ Match!"
    
    # === SCHRITT 3: Neuer Frame ===
    y_start = 565
    etree.SubElement(root, "rect", x="35", y=str(y_start), width="830", height="145",
                     fill=section_fill, stroke=box_stroke, rx="5",
                     attrib={"stroke-width": "1"})
    
    step3_title = etree.SubElement(root, "text", x="50", y=str(y_start + 20),
                                   fill=highlight_color, attrib={
                                       "font-family": "monospace",
                                       "font-size": "13",
                                       "font-weight": "bold"
                                   })
    step3_title.text = "Schritt 3: Neuer Frame für LAN 2"
    
    step3_items = [
        "✓ ARP für 10.0.0.5 → Server MAC: CC:CC:CC:CC:CC:CC",
        "✓ Neuen Ethernet-Header: Dst CC:CC, Src DD:DD (Router eth1)",
        "✓ EtherType: 0x0800",
        "✓ Neue FCS berechnen"
    ]
    
    for i, item in enumerate(step3_items):
        txt = etree.SubElement(root, "text", x="70", y=str(y_start + 45 + i*20),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "12"
                               })
        txt.text = item
    
    # === VERSAND SECTION ===
    y_start = 720
    etree.SubElement(root, "rect", x="35", y=str(y_start), width="830", height="100",
                     fill=section_fill, stroke=box_stroke, rx="5",
                     attrib={"stroke-width": "1"})
    
    send_title = etree.SubElement(root, "text", x="50", y=str(y_start + 20),
                                  fill=highlight_color, attrib={
                                      "font-family": "monospace",
                                      "font-size": "14",
                                      "font-weight": "bold"
                                  })
    send_title.text = "VERSAND auf LAN 2 (10.0.0.0/24):"
    
    # Frame visualization - send
    etree.SubElement(root, "rect", x="50", y=str(y_start + 35), width="800", height="40",
                     fill=frame_fill, stroke="#666666", rx="3")
    
    segments_out = [
        (50, 70, "CC:CC", "#4A9EFF"),
        (120, 70, "DD:DD", "#9B59B6"),
        (190, 70, "0x0800", "#2ECC71"),
        (260, 420, "IP-Paket (TTL=63)", "#F39C12"),
        (680, 60, "FCS'", "#E74C3C")
    ]
    
    for x, w, label, color in segments_out:
        etree.SubElement(root, "rect", x=str(x), y=str(y_start + 40), width=str(w), height="30",
                         fill=color, stroke="#333333", rx="2",
                         attrib={"fill-opacity": "0.3", "stroke-width": "1"})
        txt = etree.SubElement(root, "text", x=str(x + w//2), y=str(y_start + 60),
                               fill=text_color, attrib={
                                   "font-family": "monospace",
                                   "font-size": "11",
                                   "text-anchor": "middle"
                               })
        txt.text = label
    
    # Important note
    note = etree.SubElement(root, "text", x="50", y=str(y_start + 90),
                            fill=check_color, attrib={
                                "font-family": "monospace",
                                "font-size": "11",
                                "font-weight": "bold"
                            })
    note.text = "WICHTIG: IP-Adressen bleiben unverändert! Nur MAC-Adressen und TTL ändern sich."
    
    return root, width, height

def main():
    output_dir = Path("/media/andhue/Wissen/open-lectures/.kiro/tmp")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    root, width, height = create_router_verarbeitung()
    
    # Save SVG
    svg_path = output_dir / "router-verarbeitung.svg"
    svg_content = svg_to_string(root)
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created: {svg_path}")
    
    # Export PNG
    png_path = output_dir / "router-verarbeitung.png"
    export_png(str(svg_path), str(png_path), width, height)
    print(f"Created: {png_path}")
    
    # Create grayscale version
    gray_path = output_dir / "router-verarbeitung_g.png"
    create_grayscale_version(str(png_path), str(gray_path))
    print(f"Created: {gray_path}")

if __name__ == "__main__":
    main()
