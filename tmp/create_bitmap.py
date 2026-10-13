#!/usr/bin/env python3
"""
Creates a bitmap (free space management) diagram for 03-Implementierung.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(13, 7))

# Theme-agnostic colors (work on dark and light backgrounds)
# Using colors with good contrast in both modes
text_color = '#4A5568'       # Medium gray for text (works on both)
title_color = '#2B6CB0'      # Medium blue for titles
border_color = '#718096'     # Gray for borders
highlight_bg = '#E2E8F0'     # Light gray with some opacity for boxes
journal_color = '#805AD5'    # Purple for journal
disk_color = '#3182CE'       # Blue for disk
metadata_color = '#DD6B20'   # Orange for metadata  
data_color = '#38A169'       # Green for data
success_color = '#38A169'    # Green for success
warning_color = '#DD6B20'    # Orange for warnings
danger_color = '#E53E3E'     # Red for danger
old_color = '#E53E3E'        # Red for old data
new_color = '#38A169'        # Green for new data
pointer_color = '#805AD5'    # Purple for pointer
fs_color = '#3182CE'         # Blue for filesystem
commit_color = '#38A169'     # Green for commit
desc_color = '#DD6B20'       # Orange for descriptor
# Script-specific colors
bitmap_color = '#805AD5'     # Purple for bitmap label
used_color = '#FC8181'       # Light red for used blocks
free_color = '#9AE6B4'       # Light green for free blocks

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6.5, 6.5, 'Freispeicherverwaltung: Bitmap', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Bitmap visualization =====
bitmap_x, bitmap_y = 0.5, 4.2
bit_width = 0.7
bit_height = 0.7

# Bitmap data: 1 = used, 0 = free
bitmap_data = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1]

ax.text(bitmap_x, bitmap_y + 1.2, 'Bitmap:', fontsize=12, fontweight='bold',
        color=bitmap_color, ha='left', va='center')

for i, bit in enumerate(bitmap_data):
    x = bitmap_x + i * bit_width
    color = used_color if bit == 1 else free_color
    
    rect = FancyBboxPatch((x, bitmap_y), bit_width - 0.05, bit_height,
                          boxstyle="round,pad=0.01,rounding_size=0.02",
                          facecolor=color, edgecolor='#1A202C',
                          linewidth=1, alpha=0.8)
    ax.add_patch(rect)
    
    ax.text(x + bit_width/2 - 0.025, bitmap_y + bit_height/2, str(bit),
            fontsize=11, color='#1A202C', fontweight='bold',
            ha='center', va='center')

# Block numbers below
ax.text(bitmap_x, bitmap_y - 0.35, 'Block:', fontsize=9, color=text_color,
        ha='left', va='center')
for i in range(len(bitmap_data)):
    x = bitmap_x + i * bit_width
    ax.text(x + bit_width/2 - 0.025, bitmap_y - 0.35, str(i),
            fontsize=8, color='#718096', ha='center', va='center')

# ===== Disk blocks visualization =====
disk_y = 2.5
block_width = 0.7
block_height = 1.0

ax.text(bitmap_x, disk_y + 1.3, 'Datenträger:', fontsize=12, fontweight='bold',
        color=text_color, ha='left', va='center')

for i, bit in enumerate(bitmap_data):
    x = bitmap_x + i * block_width
    color = used_color if bit == 1 else free_color
    
    rect = FancyBboxPatch((x, disk_y), block_width - 0.05, block_height,
                          boxstyle="round,pad=0.01,rounding_size=0.03",
                          facecolor=color if bit == 1 else highlight_bg,
                          edgecolor=color, linewidth=2, alpha=0.7 if bit == 1 else 0.4)
    ax.add_patch(rect)
    
    if bit == 1:
        ax.text(x + block_width/2 - 0.025, disk_y + block_height/2, '▓',
                fontsize=14, color='#1A202C', ha='center', va='center', alpha=0.5)
    else:
        ax.text(x + block_width/2 - 0.025, disk_y + block_height/2, '░',
                fontsize=14, color=free_color, ha='center', va='center', alpha=0.5)

# Arrows connecting bitmap to disk
for i in [2, 5, 6, 7, 11, 12, 13]:  # Free blocks
    x = bitmap_x + i * bit_width + bit_width/2 - 0.025
    arrow = FancyArrowPatch((x, bitmap_y), (x, disk_y + block_height),
                            arrowstyle='->', mutation_scale=8,
                            color=free_color, linewidth=1, alpha=0.5)
    ax.add_patch(arrow)

# Highlight contiguous free area
highlight_rect = Rectangle((bitmap_x + 5 * block_width - 0.1, disk_y - 0.15), 
                            3 * block_width + 0.1, block_height + 0.3,
                            facecolor='none', edgecolor=free_color,
                            linewidth=2, linestyle='--', alpha=0.8)
ax.add_patch(highlight_rect)

ax.text(bitmap_x + 6.5 * block_width, disk_y - 0.5, '3 zusammenhängende freie Blöcke',
        fontsize=9, color=free_color, ha='center', va='center', style='italic')

# ===== Legend =====
legend_x = 0.5
legend_y = 1.3

legend_box = FancyBboxPatch((legend_x, legend_y - 0.2), 5.5, 1.0,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#4A5568', edgecolor=border_color,
                             linewidth=1.5)
ax.add_patch(legend_box)

# Used legend
rect_used = Rectangle((legend_x + 0.2, legend_y + 0.35), 0.4, 0.3,
                        facecolor=used_color, edgecolor='#1A202C', linewidth=1)
ax.add_patch(rect_used)
ax.text(legend_x + 0.8, legend_y + 0.5, '= 1 (belegt)', fontsize=10, color=text_color,
        ha='left', va='center')

# Free legend
rect_free = Rectangle((legend_x + 0.2, legend_y - 0.05), 0.4, 0.3,
                        facecolor=free_color, edgecolor='#1A202C', linewidth=1)
ax.add_patch(rect_free)
ax.text(legend_x + 0.8, legend_y + 0.1, '= 0 (frei)', fontsize=10, color=text_color,
        ha='left', va='center')

# Size calculation
ax.text(legend_x + 3.2, legend_y + 0.5, 'Größe:', fontsize=9, fontweight='bold',
        color=text_color, ha='left', va='center')
ax.text(legend_x + 3.2, legend_y + 0.1, '1 Bit / Block', fontsize=9, color='#718096',
        ha='left', va='center')

# ===== Info Box =====
info_box = FancyBboxPatch((6.3, legend_y - 0.2), 6.4, 1.0,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=border_color,
                           linewidth=1.5)
ax.add_patch(info_box)

ax.text(6.6, legend_y + 0.55, 'Beispiel:', fontsize=10, fontweight='bold',
        color=title_color, ha='left', va='center')
ax.text(7.6, legend_y + 0.55, '1 TB Disk, 4 KB Blöcke', fontsize=9, color=text_color,
        ha='left', va='center')

ax.text(6.6, legend_y + 0.15, '→ 256M Blöcke → 256M Bits =', fontsize=9, color='#718096',
        ha='left', va='center', family='monospace')
ax.text(10.8, legend_y + 0.15, '32 MB', fontsize=10, fontweight='bold', color=free_color,
        ha='left', va='center')

# ===== Advantages Box =====
adv_box = FancyBboxPatch((0.3, 0.15), 12.4, 0.85,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='#4A5568', edgecolor=border_color,
                          linewidth=1.5, alpha=0.9)
ax.add_patch(adv_box)

ax.text(0.6, 0.58, 'Vorteile:', fontsize=10, fontweight='bold', 
        color=free_color, ha='left', va='center')
ax.text(1.6, 0.58, 'Kompakt (1 Bit/Block)', fontsize=9, color=text_color,
        ha='left', va='center')
ax.text(4.3, 0.58, '•', fontsize=10, color=border_color, ha='center', va='center')
ax.text(4.6, 0.58, 'Zusammenhängende Bereiche leicht findbar', fontsize=9, color=text_color,
        ha='left', va='center')
ax.text(9.3, 0.58, '•', fontsize=10, color=border_color, ha='center', va='center')
ax.text(9.6, 0.58, 'CPU-Bit-Ops', fontsize=9, color=text_color,
        ha='left', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/bitmap-free.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created bitmap-free.png")
