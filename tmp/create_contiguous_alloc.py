#!/usr/bin/env python3
"""
Contiguous Allocation Diagram
Shows files allocated in sequential blocks
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
file_a_color = '#3182CE'     # Blue for file A
file_b_color = '#38A169'     # Green for file B
free_color = '#E2E8F0'       # Light gray for free space

fig, ax = plt.subplots(1, 1, figsize=(14, 9), facecolor='none')
ax.set_xlim(-0.5, 14)
ax.set_ylim(-1, 11)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(7, 10.3, 'Zusammenhängende Allokation (Contiguous)', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# Directory table
dir_box = FancyBboxPatch((0.5, 7), 4.5, 2.5,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         facecolor='#4A5568', edgecolor=text_color, linewidth=1)
ax.add_patch(dir_box)
ax.text(2.75, 9.2, 'Verzeichnis', ha='center', va='center',
        fontsize=12, color=text_color, fontweight='bold')

# Table header
ax.text(1.0, 8.6, 'Name', ha='left', va='center', fontsize=10, color=text_color, fontweight='bold')
ax.text(2.8, 8.6, 'Start', ha='center', va='center', fontsize=10, color=text_color, fontweight='bold')
ax.text(4.2, 8.6, 'Länge', ha='center', va='center', fontsize=10, color=text_color, fontweight='bold')

# Separator line
ax.plot([0.7, 4.8], [8.35, 8.35], color=text_color, lw=1)

# Table entries
ax.text(1.0, 8.0, 'file1.txt', ha='left', va='center', fontsize=10, color=file_a_color, family='monospace')
ax.text(2.8, 8.0, '2', ha='center', va='center', fontsize=10, color=text_color, family='monospace')
ax.text(4.2, 8.0, '4', ha='center', va='center', fontsize=10, color=text_color, family='monospace')

ax.text(1.0, 7.5, 'file2.txt', ha='left', va='center', fontsize=10, color=file_b_color, family='monospace')
ax.text(2.8, 7.5, '8', ha='center', va='center', fontsize=10, color=text_color, family='monospace')
ax.text(4.2, 7.5, '3', ha='center', va='center', fontsize=10, color=text_color, family='monospace')

# Disk blocks
ax.text(7, 5.8, 'Disk:', ha='center', va='center',
        fontsize=12, color=text_color, fontweight='bold')

block_width = 0.95
block_height = 1.3
block_y = 4
block_start_x = 0.7

# Draw blocks 0-11
for i in range(12):
    x = block_start_x + i * block_width
    
    if i >= 2 and i <= 5:  # file1.txt blocks
        color = file_a_color
        label = 'A'
    elif i >= 8 and i <= 10:  # file2.txt blocks
        color = file_b_color
        label = 'B'
    else:
        color = free_color
        label = ''
    
    block = FancyBboxPatch((x, block_y), block_width - 0.1, block_height,
                           boxstyle="round,pad=0.02,rounding_size=0.08",
                           facecolor=color, edgecolor='#1A202C', linewidth=1, alpha=0.9)
    ax.add_patch(block)
    
    if label:
        ax.text(x + block_width/2 - 0.05, block_y + block_height/2, label,
                ha='center', va='center', fontsize=14, color='#1A202C', fontweight='bold')
    
    # Block number below
    ax.text(x + block_width/2 - 0.05, block_y - 0.3, str(i),
            ha='center', va='center', fontsize=9, color=text_color)

# Legend / explanation
legend_y = 1.5
ax.text(1, legend_y + 1.2, 'Legende:', ha='left', va='center',
        fontsize=11, color=text_color, fontweight='bold')

# File A indicator
rect_a = Rectangle((1, legend_y + 0.4), 0.5, 0.5, facecolor=file_a_color, edgecolor='none')
ax.add_patch(rect_a)
ax.text(1.7, legend_y + 0.65, 'A = file1.txt (Blöcke 2-5, zusammenhängend)', ha='left', va='center',
        fontsize=10, color=text_color)

# File B indicator
rect_b = Rectangle((1, legend_y - 0.3), 0.5, 0.5, facecolor=file_b_color, edgecolor='none')
ax.add_patch(rect_b)
ax.text(1.7, legend_y - 0.05, 'B = file2.txt (Blöcke 8-10, zusammenhängend)', ha='left', va='center',
        fontsize=10, color=text_color)

# Free indicator
rect_free = Rectangle((1, legend_y - 1.0), 0.5, 0.5, facecolor=free_color, edgecolor='none')
ax.add_patch(rect_free)
ax.text(1.7, legend_y - 0.75, 'Frei (können neue Dateien aufnehmen)', ha='left', va='center',
        fontsize=10, color=text_color)

# Arrow showing contiguous nature for file A
ax.annotate('', xy=(4.45, block_y + block_height + 0.3), xytext=(1.6, block_y + block_height + 0.3),
            arrowprops=dict(arrowstyle='<->', color=file_a_color, lw=2))
ax.text(3, block_y + block_height + 0.6, '4 zusammenhängende Blöcke', ha='center', va='bottom',
        fontsize=9, color=file_a_color)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/contiguous-alloc.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: contiguous-alloc.png")
