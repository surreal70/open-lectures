#!/usr/bin/env python3
"""
Linked Allocation Diagram
Shows blocks with pointers to next block
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
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
null_color = '#718096'       # Gray for null

fig, ax = plt.subplots(1, 1, figsize=(14, 8), facecolor='none')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-0.5, 10)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(7, 9.5, 'Verkettete Allokation (Linked List)', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# Directory table (simple)
dir_box = FancyBboxPatch((0.3, 7), 3.5, 1.8,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         facecolor='#4A5568', edgecolor=text_color, linewidth=1)
ax.add_patch(dir_box)
ax.text(2.05, 8.5, 'Verzeichnis', ha='center', va='center',
        fontsize=11, color=text_color, fontweight='bold')

ax.text(0.8, 8.0, 'Name', ha='left', va='center', fontsize=9, color=text_color, fontweight='bold')
ax.text(2.8, 8.0, 'Start', ha='center', va='center', fontsize=9, color=text_color, fontweight='bold')
ax.plot([0.5, 3.6], [7.75, 7.75], color=text_color, lw=1)
ax.text(0.8, 7.4, 'file1.txt', ha='left', va='center', fontsize=9, color=file_color, family='monospace')
ax.text(2.8, 7.4, '2', ha='center', va='center', fontsize=9, color=text_color, family='monospace')

# Linked blocks - show 4 blocks in a chain
block_positions = [(1.5, 4.5), (4.5, 4.5), (7.5, 4.5), (10.5, 4.5)]
block_numbers = [2, 7, 4, 9]
block_width = 2.2
block_height = 2.0

for i, ((x, y), num) in enumerate(zip(block_positions, block_numbers)):
    # Main block
    block = FancyBboxPatch((x, y), block_width, block_height,
                           boxstyle="round,pad=0.03,rounding_size=0.1",
                           facecolor=file_color, edgecolor='#1A202C', linewidth=2, alpha=0.9)
    ax.add_patch(block)
    
    # Data section
    ax.text(x + block_width/2, y + block_height * 0.7, 'Daten', ha='center', va='center',
            fontsize=10, color='#1A202C', fontweight='bold')
    
    # Pointer section (bottom part)
    pointer_box = FancyBboxPatch((x + 0.1, y + 0.1), block_width - 0.2, 0.6,
                                 boxstyle="round,pad=0.02,rounding_size=0.05",
                                 facecolor=pointer_color, edgecolor='#1A202C', linewidth=1, alpha=0.9)
    ax.add_patch(pointer_box)
    
    if i < 3:
        next_text = f'Next: {block_numbers[i+1]}'
    else:
        next_text = 'Next: -1'
    
    ax.text(x + block_width/2, y + 0.4, next_text, ha='center', va='center',
            fontsize=9, color='#1A202C', family='monospace')
    
    # Block number label
    ax.text(x + block_width/2, y - 0.4, f'Block {num}', ha='center', va='center',
            fontsize=10, color=text_color, fontweight='bold')

# Arrows between blocks - from orange pointer box to next orange pointer box
for i in range(3):
    x1 = block_positions[i][0] + block_width - 0.1  # End of current orange box
    x2 = block_positions[i+1][0] + 0.1  # Start of next orange box
    y = block_positions[i][1] + 0.4  # Y position of orange boxes
    
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color=pointer_color, lw=2.5,
                               connectionstyle='arc3,rad=0'))

# Arrow from directory to first block
ax.annotate('', xy=(1.5, 5.5), xytext=(2.8, 7.2),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=1.5,
                           connectionstyle='arc3,rad=-0.2'))

# Explanation box
info_box = FancyBboxPatch((0.3, 0.3), 13.2, 1.8,
                          boxstyle="round,pad=0.1,rounding_size=0.15",
                          facecolor='#4A5568', edgecolor=text_color, linewidth=1, alpha=0.9)
ax.add_patch(info_box)

ax.text(0.7, 1.7, 'Verkettung:', ha='left', va='center', fontsize=10, color=text_color, fontweight='bold')
ax.text(0.7, 1.2, 'Block 2 → Block 7 → Block 4 → Block 9 (EOF)', ha='left', va='center',
        fontsize=10, color=pointer_color, family='monospace')
ax.text(0.7, 0.7, '-1 = Ende der Kette (End of File)', ha='left', va='center',
        fontsize=10, color=text_color)
ax.text(7.5, 1.2, 'Jeder Block speichert einen Zeiger auf den nächsten Block.', ha='left', va='center',
        fontsize=10, color=text_color)
ax.text(7.5, 0.7, 'Nachteil: Für Random Access muss die Kette durchlaufen werden.', ha='left', va='center',
        fontsize=10, color='#E53E3E')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/linked-alloc.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: linked-alloc.png")
