#!/usr/bin/env python3
"""Generate Process Control Block (PCB) diagram as PNG - Theme-agnostic version"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

# Create figure with transparent background
fig, ax = plt.subplots(1, 1, figsize=(12, 11))
ax.set_xlim(0, 12)
ax.set_ylim(0, 11)
ax.set_aspect('equal')
ax.axis('off')

# Theme-agnostic colors (work on both dark and light backgrounds)
# Avoid pure black #000000 and pure white #FFFFFF
header_color = '#4A5568'      # Neutral dark gray (not pure black)
section_bg = '#E2E8F0'        # Light gray background
box_blue = '#4299E1'          # Blue for main boxes
box_green = '#48BB78'         # Green for memory boxes
text_dark = '#A0AEC0'         # Lighter gray for better dark mode visibility
text_light = '#F7FAFC'        # Off-white for text on dark backgrounds
border_color = '#718096'      # Medium gray for borders

# Main container with border
main_box = FancyBboxPatch((0.5, 0.5), 11, 10, 
                           boxstyle="round,pad=0.05,rounding_size=0.2",
                           facecolor=section_bg, edgecolor=border_color, linewidth=3)
ax.add_patch(main_box)

# Header
header = FancyBboxPatch((0.5, 9.5), 11, 1,
                         boxstyle="round,pad=0.02,rounding_size=0.2",
                         facecolor=header_color, edgecolor=header_color, linewidth=2)
ax.add_patch(header)
ax.text(6, 10, 'PROCESS CONTROL BLOCK (PCB)', ha='center', va='center',
        fontsize=16, fontweight='bold', color=text_light, family='monospace')

# Section 1: PID and State
y_pos = 8.3
# PID Box
pid_box = FancyBboxPatch((1, y_pos), 4.5, 1,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=box_blue, edgecolor=border_color, linewidth=2)
ax.add_patch(pid_box)
ax.text(3.25, y_pos + 0.6, 'Prozess-ID', ha='center', va='center',
        fontsize=11, fontweight='bold', color=text_light)
ax.text(3.25, y_pos + 0.25, '(PID)', ha='center', va='center',
        fontsize=10, color=text_light)

# State Box
state_box = FancyBboxPatch((6, y_pos), 5, 1,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor=box_blue, edgecolor=border_color, linewidth=2)
ax.add_patch(state_box)
ax.text(8.5, y_pos + 0.6, 'Prozesszustand', ha='center', va='center',
        fontsize=11, fontweight='bold', color=text_light)
ax.text(8.5, y_pos + 0.25, '(Running/Ready/Blocked)', ha='center', va='center',
        fontsize=9, color=text_light)

# Divider line after first section
ax.plot([0.8, 11.2], [8.0, 8.0], color=border_color, linewidth=1.5)

# Section 2: Memory - Label ABOVE the boxes
y_label = 7.6
y_boxes = 6.7

ax.text(1.2, y_label, 'SPEICHER', ha='left', va='center',
        fontsize=12, fontweight='bold', color=text_dark)

# Memory boxes (positioned below the label)
mem_boxes = [('Code', 1.5), ('Daten', 4.5), ('Stack', 7.5)]
for label, x in mem_boxes:
    box = FancyBboxPatch((x, y_boxes), 2.5, 0.7,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=box_green, edgecolor=border_color, linewidth=2)
    ax.add_patch(box)
    ax.text(x + 1.25, y_boxes + 0.35, label, ha='center', va='center',
            fontsize=11, fontweight='bold', color=text_light)

# Divider line after memory section
ax.plot([0.8, 11.2], [6.3, 6.3], color=border_color, linewidth=1.5)

# Section 3: Processor Registers
y_label = 5.9
y_start = 5.5

ax.text(1.2, y_label, 'PROZESSORREGISTER', ha='left', va='center',
        fontsize=12, fontweight='bold', color=text_dark)

registers = [
    '• Instruktionszeiger (IP/PC)',
    '• Stapelzeiger (SP)',
    '• Mehrzweckregister',
    '• Prozessorstatusregister (PSW)'
]
for i, reg in enumerate(registers):
    ax.text(1.5, y_start - i*0.4, reg, ha='left', va='center',
            fontsize=10, color=text_dark, family='monospace')

# Divider line after registers section
ax.plot([0.8, 11.2], [3.7, 3.7], color=border_color, linewidth=1.5)

# Section 4: Additional Information
y_label = 3.3
y_start = 2.9

ax.text(1.2, y_label, 'WEITERE INFORMATIONEN', ha='left', va='center',
        fontsize=12, fontweight='bold', color=text_dark)

info = [
    '• Benutzer und Zugriffsrechte',
    '• Belegte Betriebsmittel (Dateien, Geräte)',
    '• Elternprozess / Kindprozesse',
    '• CPU-Zeitverbrauch'
]
for i, item in enumerate(info):
    ax.text(1.5, y_start - i*0.4, item, ha='left', va='center',
            fontsize=10, color=text_dark, family='monospace')

# Save with transparent background
output_path = "/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/03-Prozesse/assets/pcb-diagram.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()

print(f"Saved: {output_path}")
