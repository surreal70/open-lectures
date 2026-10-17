#!/usr/bin/env python3
"""
Create empfangsprozess.png - Detailed server receive process per layer.
"""

from pathlib import Path
from lxml import etree
from PIL import Image
import cairosvg

NSMAP = {None: "http://www.w3.org/2000/svg"}

def create_svg_root(width, height):
    root = etree.Element("svg", nsmap=NSMAP)
    root.set("width", str(width))
    root.set("height", str(height))
    root.set("viewBox", f"0 0 {width} {height}")
    etree.SubElement(root, "rect", x="0", y="0", width=str(width), height=str(height), fill="#1A1A1A")
    return root

def export_png(svg_path, png_path, width, height):
    cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width, output_height=height)

def create_grayscale_version(color_path, gray_path):
    img = Image.open(color_path)
    if img.mode == 'RGBA':
        gray = img.convert('LA').convert('RGBA')
    else:
        gray = img.convert('L').convert('RGB')
    gray.save(gray_path)

def svg_to_string(root):
    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8").decode('utf-8')

def create_empfangsprozess():
    width = 750
    height = 850
    
    root = create_svg_root(width, height)
    
    # Colors
    title_color = "#E8E8E8"
    text_color = "#CCCCCC"
    box_fill = "#2D2D2D"
    box_stroke = "#4A9EFF"
    section_fill = "#1E3A5F"
    check_color = "#4ADE80"
    highlight_color = "#FFB347"
    remaining_color = "#888888"
    
    # Title
    title = etree.SubElement(root, "text", x=str(width//2), y="30",
                             fill=title_color, attrib={
                                 "font-family": "monospace",
                                 "font-size": "16",
                                 "font-weight": "bold",
                                 "text-anchor": "middle"
                             })
    title.text = "SERVER – ENTKAPSELUNG IM DETAIL"
    
    # Main container
    etree.SubElement(root, "rect", x="20", y="50", width="710", height="785",
                     fill=box_fill, stroke=box_stroke, rx="8",
                     attrib={"stroke-width": "2"})
    
    # Steps data
    steps = [
        {
            "name": "SCHRITT 1: Netzzugangsschicht",
            "items": [
                "✓ Frame vom Medium empfangen (elektrische Signale)",
                "✓ Preamble/SFD erkennen (Synchronisation)",
                "✓ Destination MAC prüfen: CC:CC:CC:CC:CC:CC = eigene? → JA",
                "✓ FCS/CRC prüfen → Keine Übertragungsfehler",
                "✓ EtherType 0x0800 → IPv4, an IP-Stack übergeben",
                "✓ Ethernet-Header und FCS entfernen"
            ],
            "remaining": "Verbleibend: IP-Paket (240 Bytes)"
        },
        {
            "name": "SCHRITT 2: Internetschicht",
            "items": [
                "✓ IP-Version prüfen: 4 → IPv4",
                "✓ Header Checksum validieren → OK",
                "✓ Destination IP prüfen: 10.0.0.5 = eigene? → JA",
                "✓ Protocol-Feld auslesen: 6 → TCP",
                "✓ IP-Header entfernen, an TCP-Stack übergeben"
            ],
            "remaining": "Verbleibend: TCP-Segment (220 Bytes)"
        },
        {
            "name": "SCHRITT 3: Transportschicht",
            "items": [
                "✓ TCP Checksum validieren → OK",
                "✓ Destination Port: 80 → HTTP-Dienst",
                "✓ Socket-Zuordnung: (TCP, 192.168.1.10, 52345, 10.0.0.5, 80)",
                "✓ Sequenznummer prüfen (Reihenfolge)",
                "✓ ACK senden (Bestätigung)",
                "✓ TCP-Header entfernen",
                "✓ Daten an Port 80 (Webserver-Prozess) übergeben"
            ],
            "remaining": "Verbleibend: HTTP-Request (~200 Bytes)"
        },
        {
            "name": "SCHRITT 4: Anwendungsschicht",
            "items": [
                "✓ Webserver (z.B. Apache, nginx) empfängt Request",
                "✓ HTTP-Request parsen:",
                "    - Methode: GET",
                "    - Pfad: /index.html",
                "    - Headers: Host, User-Agent, Accept, ...",
                "✓ Datei /var/www/html/index.html laden",
                "✓ HTTP-Response generieren"
            ],
            "remaining": None
        }
    ]
    
    y = 70
    for step in steps:
        # Calculate section height
        item_count = len(step["items"])
        section_height = 45 + item_count * 18 + (25 if step["remaining"] else 10)
        
        # Section background
        etree.SubElement(root, "rect", x="35", y=str(y), width="680", height=str(section_height),
                         fill=section_fill, stroke=box_stroke, rx="5",
                         attrib={"stroke-width": "1"})
        
        # Section title
        title_txt = etree.SubElement(root, "text", x="50", y=str(y + 22),
                                     fill=highlight_color, attrib={
                                         "font-family": "monospace",
                                         "font-size": "13",
                                         "font-weight": "bold"
                                     })
        title_txt.text = step["name"]
        
        # Separator
        etree.SubElement(root, "line", x1="50", y1=str(y + 30), x2="700", y2=str(y + 30),
                         stroke="#444444", attrib={"stroke-width": "1"})
        
        # Items
        for i, item in enumerate(step["items"]):
            txt = etree.SubElement(root, "text", x="60", y=str(y + 48 + i * 18),
                                   fill=text_color if not item.startswith("    ") else "#AAAAAA",
                                   attrib={
                                       "font-family": "monospace",
                                       "font-size": "11"
                                   })
            txt.text = item
        
        # Remaining info
        if step["remaining"]:
            rem_y = y + section_height - 15
            rem_txt = etree.SubElement(root, "text", x="50", y=str(rem_y),
                                       fill=remaining_color, attrib={
                                           "font-family": "monospace",
                                           "font-size": "11",
                                           "font-style": "italic"
                                       })
            rem_txt.text = step["remaining"]
        
        y += section_height + 15
    
    return root, width, height

def main():
    output_dir = Path("/media/andhue/Wissen/open-lectures/.kiro/tmp")
    
    root, width, height = create_empfangsprozess()
    
    svg_path = output_dir / "empfangsprozess.svg"
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_to_string(root))
    print(f"Created: {svg_path}")
    
    png_path = output_dir / "empfangsprozess.png"
    export_png(str(svg_path), str(png_path), width, height)
    print(f"Created: {png_path}")
    
    gray_path = output_dir / "empfangsprozess_g.png"
    create_grayscale_version(str(png_path), str(gray_path))
    print(f"Created: {gray_path}")

if __name__ == "__main__":
    main()
