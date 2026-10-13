#!/usr/bin/env python3
"""
Creates a directory as linear list diagram for 03-Implementierung.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(12, 7))

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
bg_color = 'none'            # Transparent background
dir_color = '#3182CE'        # Blue for directory
entry_color = '#38A169'      # Green for entries
special_color = '#DD6B20'    # Orange for special entries
inode_color = '#805AD5'      # Purple for inode numbers

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 6.5, 'Verzeichnis als Lineare Liste', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# Path label
ax.text(6, 6.0, '/home/user/', fontsize=12, color='#718096',
        ha='center', va='center', family='monospace')

# Directory box
dir_x, dir_y = 1.5, 0.8
dir_width, dir_height = 5.5, 4.5

dir_box = FancyBboxPatch((dir_x, dir_y), dir_width, dir_height,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor='#4A5568', edgecolor=dir_color,
                          linewidth=2.5)
ax.add_patch(dir_box)

# Header row
header_y = dir_y + dir_height - 0.5
ax.text(dir_x + 1.8, header_y, 'Name', fontsize=11, fontweight='bold',
        color=text_color, ha='center', va='center')
ax.text(dir_x + 4.3, header_y, 'Inode', fontsize=11, fontweight='bold',
        color=text_color, ha='center', va='center')

# Header separator
ax.plot([dir_x + 0.2, dir_x + dir_width - 0.2], 
        [header_y - 0.35, header_y - 0.35], color=border_color, linewidth=1.5)

# Directory entries
entries = [
    ('.', '42', special_color, '(aktuelles Verzeichnis)'),
    ('..', '10', special_color, '(Elternverzeichnis)'),
    ('documents', '103', dir_color, ''),
    ('report.pdf', '247', inode_color, ''),
    ('notes.txt', '198', inode_color, ''),
    ('config.ini', '301', inode_color, ''),
]

entry_positions = []
for i, (name, inode, color, comment) in enumerate(entries):
    entry_y = header_y - 0.75 - i * 0.6
    
    # Entry background
    rect = FancyBboxPatch((dir_x + 0.15, entry_y - 0.22), dir_width - 0.3, 0.5,
                          boxstyle="round,pad=0.01,rounding_size=0.03",
                          facecolor=bg_color, edgecolor=border_color,
                          linewidth=1, alpha=0.5)
    ax.add_patch(rect)
    
    # Name
    ax.text(dir_x + 1.8, entry_y, name, fontsize=10, color=color,
            ha='center', va='center', family='monospace', fontweight='bold')
    
    # Separator line
    ax.plot([dir_x + 3.2, dir_x + 3.2], [entry_y - 0.2, entry_y + 0.2], 
            color=border_color, linewidth=1)
    
    # Inode number
    ax.text(dir_x + 4.3, entry_y, inode, fontsize=10, color=color,
            ha='center', va='center', family='monospace', fontweight='bold')
    
    # Comment (for special entries)
    if comment:
        ax.text(dir_x + dir_width + 0.3, entry_y, comment, fontsize=8, 
                color='#718096', ha='left', va='center', style='italic')
    
    entry_positions.append((dir_x + dir_width, entry_y, inode, color))

# Inode boxes on the right
inode_x = 9

ax.text(inode_x + 1, 5.5, 'Inodes', fontsize=12, fontweight='bold',
        color=text_color, ha='center', va='center')

# Draw some inode boxes
inode_entries = [
    ('42', special_color, 4.8),
    ('103', dir_color, 4.0),
    ('198', inode_color, 3.2),
    ('247', inode_color, 2.4),
    ('301', inode_color, 1.6),
]

for inode_num, color, y_pos in inode_entries:
    rect = FancyBboxPatch((inode_x, y_pos - 0.25), 2, 0.5,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#4A5568', edgecolor=color,
                          linewidth=1.5)
    ax.add_patch(rect)
    ax.text(inode_x + 1, y_pos, f'Inode {inode_num}', fontsize=9,
            color=color, ha='center', va='center', fontweight='bold')

# Arrows from directory entries to inodes
arrow_targets = {
    '42': 4.8, '103': 4.0, '198': 3.2, '247': 2.4, '301': 1.6
}

for (start_x, start_y, inode, color) in entry_positions:
    if inode in arrow_targets:
        target_y = arrow_targets[inode]
        arrow = FancyArrowPatch((start_x, start_y),
                                (inode_x, target_y),
                                arrowstyle='->', mutation_scale=12,
                                color=color, linewidth=1.5, alpha=0.7,
                                connectionstyle="arc3,rad=0.1")
        ax.add_patch(arrow)

# Search complexity note
note_box = FancyBboxPatch((0.3, 0.15), 11.4, 0.55,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=border_color,
                           linewidth=1.5, alpha=0.9)
ax.add_patch(note_box)

ax.text(0.6, 0.43, 'Suche:', fontsize=10, fontweight='bold', 
        color='#E53E3E', ha='left', va='center')
ax.text(1.5, 0.43, 'O(n) – Liste muss sequentiell durchsucht werden', 
        fontsize=10, color=text_color, ha='left', va='center')

ax.text(7, 0.43, '|', fontsize=10, color=border_color, ha='center', va='center')

ax.text(7.5, 0.43, 'Geeignet für:', fontsize=10, fontweight='bold', 
        color=dir_color, ha='left', va='center')
ax.text(9.3, 0.43, 'kleine Verzeichnisse', 
        fontsize=10, color=text_color, ha='left', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/dir-linear.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created dir-linear.png")
