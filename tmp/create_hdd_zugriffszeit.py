#!/usr/bin/env python3
"""
HDD Zugriffszeit (Access Time) Diagram
Shows Seek Time, Rotational Latency, and Transfer Time
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, FancyArrowPatch, Arc
import numpy as np

# Colors (theme-agnostic, matching project style)
box_fill = '#3182CE'        # Blue for main components
text_color = '#4A5568'      # Gray for labels
platter_color = '#4A5568'   # Dark gray for platter
seek_color = '#9F7AEA'      # Purple for seek
rotation_color = '#38A169'  # Green for rotation
transfer_color = '#ED8936'  # Orange for transfer
head_color = '#E53E3E'      # Red for head
highlight_bg = '#E2E8F0'    # Dark background for info boxes

fig, axes = plt.subplots(1, 3, figsize=(15, 8), facecolor='none')

# ============ PANEL 1: SEEK TIME ============
ax1 = axes[0]
ax1.set_xlim(-1, 11)
ax1.set_ylim(-2, 12)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_facecolor('none')

ax1.text(5, 11.2, '1. Seek Time', ha='center', va='center',
         fontsize=14, color=seek_color, fontweight='bold')
ax1.text(5, 10.4, '(Positionierzeit)', ha='center', va='center',
         fontsize=11, color=text_color)

# Draw platter
platter = Circle((5, 6), 3.5, facecolor=platter_color, edgecolor=text_color, linewidth=2)
ax1.add_patch(platter)

# Spindle
spindle = Circle((5, 6), 0.4, facecolor='#1A202C', edgecolor=text_color, linewidth=1)
ax1.add_patch(spindle)

# Draw tracks
for r in [3.2, 2.6, 2.0, 1.4]:
    track = Circle((5, 6), r, facecolor='none', edgecolor='#718096', linewidth=1, linestyle='--', alpha=0.5)
    ax1.add_patch(track)

# Cylinder A (outer) - starting position
ax1.plot([5, 8.2], [6, 6], color=seek_color, linewidth=3, alpha=0.5, linestyle='--')
head_a = Circle((8.2, 6), 0.2, facecolor=head_color, edgecolor='#1A202C', linewidth=2, alpha=0.5)
ax1.add_patch(head_a)
ax1.text(8.5, 6.5, 'Start', ha='left', va='bottom', fontsize=9, color=text_color, alpha=0.7)

# Cylinder B (inner) - target position
ax1.plot([5, 6.4], [6, 6], color=seek_color, linewidth=4)
head_b = Circle((6.4, 6), 0.25, facecolor=head_color, edgecolor='#1A202C', linewidth=2)
ax1.add_patch(head_b)
ax1.text(6.6, 6.5, 'Ziel', ha='left', va='bottom', fontsize=9, color=text_color)

# Arrow showing movement
ax1.annotate('', xy=(6.6, 5.3), xytext=(8, 5.3),
             arrowprops=dict(arrowstyle='->', color=seek_color, lw=3))
ax1.text(7.3, 4.8, 'Arm bewegen', ha='center', va='top', fontsize=9, color=seek_color)

# Labels for cylinders
ax1.text(1.3, 6, 'Zyl. A', ha='center', va='center', fontsize=9, color=text_color)
ax1.text(3.3, 6, 'Zyl. B', ha='center', va='center', fontsize=9, color=text_color)

# Info box (moved down)
info_box = FancyBboxPatch((0.5, -1.2), 9, 1.8,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor='#4A5568', edgecolor=seek_color, linewidth=2, alpha=0.9)
ax1.add_patch(info_box)
ax1.text(5, -0.3, 'Zeit für Kopfbewegung zum Zielzylinder\nTypisch: 3–15 ms', 
         ha='center', va='center', fontsize=10, color=text_color)

# ============ PANEL 2: ROTATIONAL LATENCY ============
ax2 = axes[1]
ax2.set_xlim(-1, 11)
ax2.set_ylim(-2, 12)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('none')

ax2.text(5, 11.2, '2. Rotational Latency', ha='center', va='center',
         fontsize=14, color=rotation_color, fontweight='bold')
ax2.text(5, 10.4, '(Rotationsverzögerung)', ha='center', va='center',
         fontsize=11, color=text_color)

# Draw platter
platter2 = Circle((5, 6), 3.5, facecolor=platter_color, edgecolor=text_color, linewidth=2)
ax2.add_patch(platter2)

# Spindle
spindle2 = Circle((5, 6), 0.4, facecolor='#1A202C', edgecolor=text_color, linewidth=1)
ax2.add_patch(spindle2)

# Draw track where head is positioned
track_r = 2.6
track = Circle((5, 6), track_r, facecolor='none', edgecolor='#718096', linewidth=2)
ax2.add_patch(track)

# Target sector (highlighted)
target_angle_start = 200
target_angle_end = 245
target_sector = Wedge((5, 6), track_r + 0.3, target_angle_start, target_angle_end,
                      width=0.6, facecolor=rotation_color, edgecolor='#1A202C', linewidth=1, alpha=0.8)
ax2.add_patch(target_sector)

# Head position (waiting)
head_angle = np.radians(90)
head_x = 5 + track_r * np.cos(head_angle)
head_y = 6 + track_r * np.sin(head_angle)
head2 = Circle((head_x, head_y), 0.25, facecolor=head_color, edgecolor='#1A202C', linewidth=2)
ax2.add_patch(head2)
ax2.text(head_x, head_y + 0.5, 'Kopf', ha='center', va='bottom', fontsize=9, color=head_color)

# Rotation arrow (arc)
arc = Arc((5, 6), 5, 5, angle=0, theta1=100, theta2=195,
          color=rotation_color, linewidth=3, linestyle='-')
ax2.add_patch(arc)
# Arrow head
arr_angle = np.radians(195)
arr_x = 5 + 2.5 * np.cos(arr_angle)
arr_y = 6 + 2.5 * np.sin(arr_angle)
ax2.annotate('', xy=(arr_x - 0.2, arr_y - 0.3), xytext=(arr_x, arr_y),
             arrowprops=dict(arrowstyle='->', color=rotation_color, lw=3))

# Label target sector
target_mid_angle = np.radians((target_angle_start + target_angle_end) / 2)
label_x = 5 + (track_r + 0.8) * np.cos(target_mid_angle)
label_y = 6 + (track_r + 0.8) * np.sin(target_mid_angle)
ax2.annotate('Ziel-\nSektor', xy=(label_x, label_y), xytext=(1.5, 4),
             fontsize=9, color=rotation_color, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=rotation_color, lw=1.5))

# Rotation direction label
ax2.text(2.2, 7.5, 'Warten auf\nSektor...', ha='center', va='center', 
         fontsize=9, color=rotation_color, style='italic')

# Info box (moved down)
info_box2 = FancyBboxPatch((0.5, -1.2), 9, 1.8,
                           boxstyle="round,pad=0.1,rounding_size=0.2",
                           facecolor='#4A5568', edgecolor=rotation_color, linewidth=2, alpha=0.9)
ax2.add_patch(info_box2)
ax2.text(5, -0.3, 'Warten bis Sektor unter Kopf rotiert\n∅ = ½ Umdrehung → bei 7200 RPM: ~4 ms', 
         ha='center', va='center', fontsize=10, color=text_color)

# ============ PANEL 3: TRANSFER + SUMMARY ============
ax3 = axes[2]
ax3.set_xlim(-1, 11)
ax3.set_ylim(-2, 12)
ax3.set_aspect('equal')
ax3.axis('off')
ax3.set_facecolor('none')

ax3.text(5, 11.2, '3. Transfer Time', ha='center', va='center',
         fontsize=14, color=transfer_color, fontweight='bold')
ax3.text(5, 10.4, '(Übertragungszeit)', ha='center', va='center',
         fontsize=11, color=text_color)

# Simple data flow illustration
# Platter segment
platter3 = Wedge((2.5, 7.5), 1.5, 0, 90, width=0.5,
                 facecolor=transfer_color, edgecolor=text_color, linewidth=1.5, alpha=0.8)
ax3.add_patch(platter3)
ax3.text(2.5, 7.5, 'Daten', ha='center', va='center', fontsize=9, color='#1A202C', fontweight='bold')

# Arrow to RAM
ax3.annotate('', xy=(6, 7.5), xytext=(4.2, 7.5),
             arrowprops=dict(arrowstyle='->', color=transfer_color, lw=3))
ax3.text(5.1, 8, 'lesen', ha='center', va='bottom', fontsize=9, color=transfer_color)

# RAM box
ram_box = FancyBboxPatch((6, 6.8), 2.5, 1.4,
                         boxstyle="round,pad=0.05,rounding_size=0.1",
                         facecolor=box_fill, edgecolor=text_color, linewidth=1.5)
ax3.add_patch(ram_box)
ax3.text(7.25, 7.5, 'RAM', ha='center', va='center', fontsize=11, color='#1A202C', fontweight='bold')

# Transfer info
ax3.text(5, 5.5, 'Bei 200 MB/s und 4 KB Block:\n≈ 0.02 ms (vernachlässigbar)', 
         ha='center', va='center', fontsize=10, color=text_color, style='italic')

# ============ SUMMARY BOX (moved down) ============
summary_box = FancyBboxPatch((0.3, -1.3), 9.4, 4.5,
                             boxstyle="round,pad=0.1,rounding_size=0.2",
                             facecolor='#4A5568', edgecolor=box_fill, linewidth=2, alpha=0.95)
ax3.add_patch(summary_box)

ax3.text(5, 2.7, 'BEISPIEL: Random Read @ 7200 RPM', ha='center', va='center',
         fontsize=11, color=text_color, fontweight='bold')

# Table-like summary
y_start = 2.0
line_height = 0.5
entries = [
    ('Seek:', '8 ms', seek_color),
    ('Rotation:', '4 ms', rotation_color),
    ('Transfer:', '≈ 0 ms', transfer_color),
]

for i, (label, value, color) in enumerate(entries):
    y = y_start - i * line_height
    ax3.text(2.5, y, label, ha='right', va='center', fontsize=10, color=color, fontweight='bold')
    ax3.text(3, y, value, ha='left', va='center', fontsize=10, color=text_color)

# Divider line
ax3.plot([1.5, 8.5], [0.3, 0.3], color=text_color, linewidth=1, alpha=0.5)

# Total
ax3.text(2.5, -0.2, 'Gesamt:', ha='right', va='center', fontsize=11, color=text_color, fontweight='bold')
ax3.text(3, -0.2, '12 ms → ~80 IOPS', ha='left', va='center', fontsize=11, color='#1A202C', fontweight='bold')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/hdd-zugriffszeit.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: hdd-zugriffszeit.png")
