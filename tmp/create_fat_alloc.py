#!/usr/bin/env python3
"""
FAT (File Allocation Table) Diagram
Shows the FAT table with pointers in a central table
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

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
file_color = '#3182CE'       # Blue for file
free_color = '#E2E8F0'       # Light gray for free
eof_color = '#E53E3E'        # Red for EOF
fat_color = '#805AD5'        # Purple for FAT

fig, ax = plt.subplots(1, 1, figsize=(14, 9), facecolor='none')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-0.5, 11)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(7, 10.5, 'File Allocation Table (FAT)', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# Directory table (left)
dir_box = FancyBboxPatch((0.3, 6.5), 3.2, 2.2,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         facecolor='#4A5568', edgecolor=text_color, linewidth=1)
ax.add_patch(dir_box)
ax.text(1.9, 8.4, 'Verzeichnis', ha='center', va='center',
        fontsize=11, color=text_color, fontweight='bold')

ax.text(0.7, 7.9, 'Name', ha='left', va='center', fontsize=9, color=text_color, fontweight='bold')
ax.text(2.7, 7.9, 'Start', ha='center', va='center', fontsize=9, color=text_color, fontweight='bold')
ax.plot([0.5, 3.3], [7.65, 7.65], color=text_color, lw=1)
ax.text(0.7, 7.3, 'file1.txt', ha='left', va='center', fontsize=9, color=file_color, family='monospace')
ax.text(2.7, 7.3, '2', ha='center', va='center', fontsize=9, color=text_color, family='monospace')
ax.text(0.7, 6.9, 'file2.txt', ha='left', va='center', fontsize=9, color=pointer_color, family='monospace')
ax.text(2.7, 6.9, '5', ha='center', va='center', fontsize=9, color=text_color, family='monospace')

# FAT Table (center)
fat_box = FancyBboxPatch((4.5, 2.5), 3.5, 6.2,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         facecolor='#4A5568', edgecolor=fat_color, linewidth=2)
ax.add_patch(fat_box)
ax.text(6.25, 8.4, 'FAT (im RAM)', ha='center', va='center',
        fontsize=11, color=fat_color, fontweight='bold')

# FAT header
ax.text(5.2, 7.9, 'Block', ha='center', va='center', fontsize=9, color=text_color, fontweight='bold')
ax.text(7.0, 7.9, 'Next', ha='center', va='center', fontsize=9, color=text_color, fontweight='bold')
ax.plot([4.7, 7.8], [7.65, 7.65], color=text_color, lw=1)

# FAT entries
fat_entries = [
    (0, '---', text_color),
    (1, '---', text_color),
    (2, '7', file_color),
    (3, '---', text_color),
    (4, '9', file_color),
    (5, '6', pointer_color),
    (6, 'EOF', pointer_color),
    (7, '4', file_color),
    (8, '---', text_color),
    (9, 'EOF', file_color),
]

for i, (block, next_val, color) in enumerate(fat_entries):
    y = 7.3 - i * 0.45
    ax.text(5.2, y, str(block), ha='center', va='center', fontsize=9, color=text_color, family='monospace')
    if next_val == 'EOF':
        ax.text(7.0, y, next_val, ha='center', va='center', fontsize=9, color=eof_color, family='monospace', fontweight='bold')
    else:
        ax.text(7.0, y, next_val, ha='center', va='center', fontsize=9, color=color, family='monospace')

# Draw chain arrows for file1 (2 -> 7 -> 4 -> 9)
# Arrow from entry 2 to entry 7 - curved to the right
ax.annotate('', xy=(7.6, 7.3 - 7*0.45), xytext=(7.4, 7.3 - 2*0.45),
            arrowprops=dict(arrowstyle='->', color=file_color, lw=1.5,
                           connectionstyle='arc3,rad=-0.3'))

# Chain visualization on the right
chain_x = 9.5
ax.text(11, 8.4, 'Dateiketten', ha='center', va='center',
        fontsize=11, color=text_color, fontweight='bold')

# file1.txt chain
ax.text(9, 7.5, 'file1.txt:', ha='left', va='center', fontsize=9, color=file_color, fontweight='bold')
chain1 = ['2', '→', '7', '→', '4', '→', '9', '(EOF)']
for i, item in enumerate(chain1):
    x = 9 + i * 0.55
    if item == '→':
        ax.text(x + 0.15, 7.0, item, ha='center', va='center', fontsize=10, color=text_color)
    elif item == '(EOF)':
        ax.text(x + 0.3, 7.0, item, ha='center', va='center', fontsize=8, color=eof_color)
    else:
        box = FancyBboxPatch((x, 6.8), 0.5, 0.4,
                             boxstyle="round,pad=0.02,rounding_size=0.05",
                             facecolor=file_color, edgecolor='#1A202C', linewidth=1)
        ax.add_patch(box)
        ax.text(x + 0.25, 7.0, item, ha='center', va='center', fontsize=9, color='#1A202C', fontweight='bold')

# file2.txt chain  
ax.text(9, 6.0, 'file2.txt:', ha='left', va='center', fontsize=9, color=pointer_color, fontweight='bold')
chain2 = ['5', '→', '6', '(EOF)']
for i, item in enumerate(chain2):
    x = 9 + i * 0.55
    if item == '→':
        ax.text(x + 0.15, 5.5, item, ha='center', va='center', fontsize=10, color=text_color)
    elif item == '(EOF)':
        ax.text(x + 0.3, 5.5, item, ha='center', va='center', fontsize=8, color=eof_color)
    else:
        box = FancyBboxPatch((x, 5.3), 0.5, 0.4,
                             boxstyle="round,pad=0.02,rounding_size=0.05",
                             facecolor=pointer_color, edgecolor='#1A202C', linewidth=1)
        ax.add_patch(box)
        ax.text(x + 0.25, 5.5, item, ha='center', va='center', fontsize=9, color='#1A202C', fontweight='bold')

# Arrow from directory to FAT
ax.annotate('', xy=(4.5, 7.3), xytext=(3.5, 7.3),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5))

# Info box at bottom
info_box = FancyBboxPatch((0.3, 0.2), 13.2, 1.8,
                          boxstyle="round,pad=0.1,rounding_size=0.15",
                          facecolor='#4A5568', edgecolor=text_color, linewidth=1, alpha=0.9)
ax.add_patch(info_box)

ax.text(0.7, 1.6, 'Vorteile:', ha='left', va='center', fontsize=10, color=fat_color, fontweight='bold')
ax.text(2.0, 1.6, 'FAT liegt im RAM → schneller Random Access, keine Zeiger in Datenblöcken', ha='left', va='center',
        fontsize=9, color=text_color)
ax.text(0.7, 1.0, 'Nachteile:', ha='left', va='center', fontsize=10, color=eof_color, fontweight='bold')
ax.text(2.3, 1.0, 'FAT kann sehr groß werden, FAT-Korruption = Totalverlust', ha='left', va='center',
        fontsize=9, color=text_color)
ax.text(0.7, 0.5, 'Anwendung:', ha='left', va='center', fontsize=10, color=text_color, fontweight='bold')
ax.text(2.5, 0.5, 'MS-DOS, USB-Sticks (FAT32), SD-Karten', ha='left', va='center',
        fontsize=9, color=text_color)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/fat-alloc.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: fat-alloc.png")
