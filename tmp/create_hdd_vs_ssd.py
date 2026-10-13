#!/usr/bin/env python3
"""
HDD vs SSD Comparison Diagram
Shows visual comparison of mechanical vs electronic storage
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Rectangle, Arc
import numpy as np

# Colors (theme-agnostic, matching project style)
box_fill = '#3182CE'        # Blue for main components
text_color = '#4A5568'      # Gray for labels
platter_color = '#4A5568'   # Dark gray for platter
hdd_color = '#9F7AEA'       # Purple for HDD
ssd_color = '#38A169'       # Green for SSD
chip_color = '#2D3748'      # Dark for chips
head_color = '#E53E3E'      # Red for head
highlight_bg = '#E2E8F0'    # Dark background

fig, axes = plt.subplots(1, 2, figsize=(14, 7), facecolor='none')

# ============ LEFT: HDD (Mechanical) ============
ax1 = axes[0]
ax1.set_xlim(-1, 11)
ax1.set_ylim(2, 12)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_facecolor('none')

# Title
ax1.text(5, 11.3, 'HDD (Mechanisch)', ha='center', va='center',
         fontsize=16, color=hdd_color, fontweight='bold')

# HDD case outline
hdd_case = FancyBboxPatch((0.5, 3), 9, 6.5,
                          boxstyle="round,pad=0.05,rounding_size=0.3",
                          facecolor='#1A202C', edgecolor=text_color, linewidth=2)
ax1.add_patch(hdd_case)

# Platter
platter = Circle((4.5, 6), 2.8, facecolor=platter_color, edgecolor=text_color, linewidth=2)
ax1.add_patch(platter)

# Tracks on platter
for r in [2.4, 1.9, 1.4, 0.9]:
    track = Circle((4.5, 6), r, facecolor='none', edgecolor='#718096', 
                   linewidth=1, linestyle='--', alpha=0.4)
    ax1.add_patch(track)

# Spindle
spindle = Circle((4.5, 6), 0.35, facecolor='#1A202C', edgecolor=text_color, linewidth=1)
ax1.add_patch(spindle)

# Rotation arrow
arc = Arc((4.5, 6), 1.2, 1.2, angle=0, theta1=30, theta2=330,
          color=text_color, linewidth=2, alpha=0.7)
ax1.add_patch(arc)
ax1.text(4.5, 6, '↻', ha='center', va='center', fontsize=16, color=text_color, alpha=0.7)

# Actuator arm
arm_pivot = (8, 4)
arm_end = (5.8, 6.3)
ax1.plot([arm_pivot[0], arm_end[0]], [arm_pivot[1], arm_end[1]], 
         color='#4A5568', linewidth=6, solid_capstyle='round')

# Read/write head
head = Circle(arm_end, 0.18, facecolor=head_color, edgecolor='#1A202C', linewidth=1.5)
ax1.add_patch(head)

# Arm pivot base
pivot_rect = FancyBboxPatch((7.5, 3.3), 1.3, 1.8,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4A5568', edgecolor=text_color, linewidth=1)
ax1.add_patch(pivot_rect)

# Labels inside
ax1.text(4.5, 8.5, 'Platten', ha='center', va='center', fontsize=10, color=text_color)
ax1.text(8.2, 6, 'Arm', ha='left', va='center', fontsize=10, color=text_color)

# Characteristics box (below) - REMOVED, will be in markdown
# char_box = FancyBboxPatch((0.5, -1.3), 9, 3.8,
#                           boxstyle="round,pad=0.1,rounding_size=0.2",
#                           facecolor='#4A5568', edgecolor=hdd_color, linewidth=2, alpha=0.95)
# ax1.add_patch(char_box)
# 
# characteristics_hdd = [
#     '• Mechanische Teile',
#     '• Empfindlich gegen Stöße',
#     '• Seek Time > 0',
#     '• Sequentiell viel schneller',
# ]
# for i, text in enumerate(characteristics_hdd):
#     ax1.text(1, 1.8 - i * 0.7, text, ha='left', va='center', 
#              fontsize=11, color=text_color)

# ============ RIGHT: SSD (Electronic) ============
ax2 = axes[1]
ax2.set_xlim(-1, 11)
ax2.set_ylim(2, 12)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('none')

# Title
ax2.text(5, 11.3, 'SSD (Elektronisch)', ha='center', va='center',
         fontsize=16, color=ssd_color, fontweight='bold')

# SSD case outline
ssd_case = FancyBboxPatch((0.5, 3), 9, 6.5,
                          boxstyle="round,pad=0.05,rounding_size=0.3",
                          facecolor='#1A202C', edgecolor=text_color, linewidth=2)
ax2.add_patch(ssd_case)

# NAND Flash chips grid (4x3)
chip_width = 1.6
chip_height = 1.2
chip_gap_x = 0.3
chip_gap_y = 0.3
start_x = 1.3
start_y = 4

for row in range(3):
    for col in range(4):
        x = start_x + col * (chip_width + chip_gap_x)
        y = start_y + row * (chip_height + chip_gap_y)
        chip = FancyBboxPatch((x, y), chip_width, chip_height,
                              boxstyle="round,pad=0.02,rounding_size=0.05",
                              facecolor=chip_color, edgecolor=ssd_color, linewidth=1.5)
        ax2.add_patch(chip)
        # Chip pattern (small squares to indicate NAND cells)
        for cx in range(3):
            for cy in range(2):
                cell_x = x + 0.25 + cx * 0.4
                cell_y = y + 0.25 + cy * 0.4
                cell = Rectangle((cell_x, cell_y), 0.25, 0.25,
                                 facecolor=ssd_color, alpha=0.6)
                ax2.add_patch(cell)

# Label
ax2.text(5, 8.5, 'NAND Flash Chips', ha='center', va='center', fontsize=10, color=text_color)

# Controller chip (bottom of SSD)
controller = FancyBboxPatch((3, 3.3), 4, 0.5,
                            boxstyle="round,pad=0.02,rounding_size=0.05",
                            facecolor=box_fill, edgecolor=text_color, linewidth=1)
ax2.add_patch(controller)
ax2.text(5, 3.55, 'Controller', ha='center', va='center', fontsize=9, color='#1A202C')

# Characteristics box (below) - REMOVED, will be in markdown
# char_box2 = FancyBboxPatch((0.5, -1.3), 9, 3.8,
#                            boxstyle="round,pad=0.1,rounding_size=0.2",
#                            facecolor='#4A5568', edgecolor=ssd_color, linewidth=2, alpha=0.95)
# ax2.add_patch(char_box2)
# 
# characteristics_ssd = [
#     '• Keine beweglichen Teile',
#     '• Stoßunempfindlich',
#     '• Random ≈ Sequentiell',
#     '• Begrenzte Schreibzyklen',
# ]
# for i, text in enumerate(characteristics_ssd):
#     ax2.text(1, 1.8 - i * 0.7, text, ha='left', va='center', 
#              fontsize=11, color=text_color)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/hdd-vs-ssd.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: hdd-vs-ssd.png")
