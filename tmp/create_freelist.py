#!/usr/bin/env python3
"""
Creates a free list (linked free blocks) diagram for 03-Implementierung.md
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
used_color = '#FC8181'       # Light red for used blocks
free_color = '#9AE6B4'       # Light green for free blocks
pointer_color = '#805AD5'    # Purple for pointers

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6.5, 6.5, 'Freispeicherverwaltung: Verkettete Liste', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Free List Head =====
head_box = FancyBboxPatch((0.5, 5.5), 2.5, 0.8,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=pointer_color,
                           linewidth=2)
ax.add_patch(head_box)
ax.text(1.75, 5.9, 'Free List Head', fontsize=10, fontweight='bold',
        color=pointer_color, ha='center', va='center')
ax.text(1.75, 5.6, 'Block 2', fontsize=9, color=text_color,
        ha='center', va='center', family='monospace')

# ===== Disk representation =====
disk_y = 3.2
block_width = 0.72
block_height = 1.5

ax.text(0.5, disk_y + 1.8, 'Datenträger:', fontsize=12, fontweight='bold',
        color=text_color, ha='left', va='center')

# Disk blocks - mixed used and free
disk_data = [
    (0, True, None),    # Used
    (1, True, None),    # Used
    (2, False, 5),      # Free -> 5
    (3, True, None),    # Used
    (4, True, None),    # Used
    (5, False, 6),      # Free -> 6
    (6, False, 7),      # Free -> 7
    (7, False, 11),     # Free -> 11
    (8, True, None),    # Used
    (9, True, None),    # Used
    (10, True, None),   # Used
    (11, False, 12),    # Free -> 12
    (12, False, 13),    # Free -> 13
    (13, False, None),  # Free -> NULL
    (14, True, None),   # Used
    (15, True, None),   # Used
]

free_block_positions = {}

for i, (block_num, used, next_ptr) in enumerate(disk_data):
    x = 0.5 + i * block_width
    color = used_color if used else free_color
    
    rect = FancyBboxPatch((x, disk_y), block_width - 0.05, block_height,
                          boxstyle="round,pad=0.01,rounding_size=0.03",
                          facecolor=color if used else highlight_bg,
                          edgecolor=color, linewidth=2, alpha=0.7 if used else 0.9)
    ax.add_patch(rect)
    
    ax.text(x + block_width/2 - 0.025, disk_y + block_height - 0.3, str(block_num),
            fontsize=8, color='#1A202C' if used else free_color, ha='center', va='center',
            fontweight='bold')
    
    if not used:
        free_block_positions[block_num] = (x + block_width/2 - 0.025, disk_y + block_height/2)
        # Show pointer inside block
        if next_ptr is not None:
            ax.text(x + block_width/2 - 0.025, disk_y + 0.5, f'→{next_ptr}',
                    fontsize=7, color=pointer_color, ha='center', va='center',
                    family='monospace', fontweight='bold')
        else:
            ax.text(x + block_width/2 - 0.025, disk_y + 0.5, 'NULL',
                    fontsize=7, color='#718096', ha='center', va='center',
                    family='monospace')

# ===== Chain visualization above disk =====
chain_y = 5.4

# Arrow from head to first free block
arrow_head = FancyArrowPatch((3.0, 5.7), (free_block_positions[2][0], disk_y + block_height),
                              arrowstyle='->', mutation_scale=15,
                              color=pointer_color, linewidth=2.5,
                              connectionstyle="arc3,rad=0.2")
ax.add_patch(arrow_head)

# Chain arrows between free blocks
chain = [(2, 5), (5, 6), (6, 7), (7, 11), (11, 12), (12, 13)]

for from_blk, to_blk in chain:
    from_pos = free_block_positions[from_blk]
    to_pos = free_block_positions[to_blk]
    
    # Draw curved arrow above the blocks
    mid_x = (from_pos[0] + to_pos[0]) / 2
    
    arrow = FancyArrowPatch((from_pos[0], disk_y + block_height),
                            (to_pos[0], disk_y + block_height),
                            arrowstyle='->', mutation_scale=12,
                            color=pointer_color, linewidth=2,
                            connectionstyle=f"arc3,rad=-0.4")
    ax.add_patch(arrow)

# NULL terminator
null_x = free_block_positions[13][0] + 0.8
ax.text(null_x, disk_y + block_height + 0.3, 'NULL', fontsize=9, color='#718096',
        ha='center', va='center', family='monospace', fontweight='bold')
arrow_null = FancyArrowPatch((free_block_positions[13][0], disk_y + block_height),
                              (null_x - 0.3, disk_y + block_height + 0.25),
                              arrowstyle='->', mutation_scale=10,
                              color='#718096', linewidth=1.5)
ax.add_patch(arrow_null)

# ===== Legend =====
legend_x = 0.5
legend_y = 1.4

legend_box = FancyBboxPatch((legend_x, legend_y - 0.2), 5, 1.0,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#4A5568', edgecolor=border_color,
                             linewidth=1.5)
ax.add_patch(legend_box)

# Used legend
rect_used = Rectangle((legend_x + 0.2, legend_y + 0.4), 0.4, 0.25,
                        facecolor=used_color, edgecolor='#1A202C', linewidth=1)
ax.add_patch(rect_used)
ax.text(legend_x + 0.8, legend_y + 0.52, 'Belegt', fontsize=10, color=text_color,
        ha='left', va='center')

# Free legend
rect_free = Rectangle((legend_x + 0.2, legend_y + 0.0), 0.4, 0.25,
                        facecolor='#4A5568', edgecolor=free_color, linewidth=2)
ax.add_patch(rect_free)
ax.text(legend_x + 0.8, legend_y + 0.12, 'Frei (mit Pointer)', fontsize=10, color=text_color,
        ha='left', va='center')

# Operations
ax.text(legend_x + 3.0, legend_y + 0.52, 'Alloc:', fontsize=9, fontweight='bold',
        color=free_color, ha='left', va='center')
ax.text(legend_x + 3.7, legend_y + 0.52, 'Head nehmen', fontsize=9, color='#718096',
        ha='left', va='center')

ax.text(legend_x + 3.0, legend_y + 0.12, 'Free:', fontsize=9, fontweight='bold',
        color=pointer_color, ha='left', va='center')
ax.text(legend_x + 3.5, legend_y + 0.12, 'Am Head einfügen', fontsize=9, color='#718096',
        ha='left', va='center')

# ===== Info Box =====
info_box = FancyBboxPatch((5.8, legend_y - 0.2), 6.9, 1.0,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=border_color,
                           linewidth=1.5)
ax.add_patch(info_box)

ax.text(6.1, legend_y + 0.55, 'Nachteil:', fontsize=10, fontweight='bold',
        color=used_color, ha='left', va='center')
ax.text(7.3, legend_y + 0.55, 'Liste kann über Disk verstreut sein', fontsize=9, color=text_color,
        ha='left', va='center')

ax.text(6.1, legend_y + 0.15, '→ Viele Disk-Zugriffe nötig für große Listen', fontsize=9, color='#718096',
        ha='left', va='center')

# ===== Bottom info =====
bottom_box = FancyBboxPatch((0.3, 0.15), 12.4, 0.7,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#4A5568', edgecolor=border_color,
                             linewidth=1.5, alpha=0.9)
ax.add_patch(bottom_box)

ax.text(0.6, 0.5, 'Optimierungen:', fontsize=10, fontweight='bold', 
        color=title_color, ha='left', va='center')
ax.text(2.4, 0.5, 'Grouping (Blöcke speichern Adressen weiterer Blöcke)', fontsize=9, color=text_color,
        ha='left', va='center')
ax.text(8.2, 0.5, '|', fontsize=10, color=border_color, ha='center', va='center')
ax.text(8.6, 0.5, 'Counting (Startblock, Anzahl)', fontsize=9, color=text_color,
        ha='left', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/freelist.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created freelist.png")
