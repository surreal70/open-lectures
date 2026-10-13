#!/usr/bin/env python3
"""
Creates an inode (indexed allocation) diagram for 03-Implementierung.md
All pointer entries inside the Inode box, arrows originate from colored boxes
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(14, 11))

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
inode_color = '#805AD5'      # Purple for inode
block_color = '#38A169'      # Green for data blocks
indirect_color = '#DD6B20'   # Orange for indirect
direct_color = '#38A169'     # Green for direct blocks
double_indirect_color = '#E53E3E'  # Red for double indirect
triple_indirect_color = '#805AD5'  # Purple for triple indirect

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(7, 10.5, 'Indizierte Allokation (Inode-Struktur)', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# Draw Inode box - taller to fit everything
inode_x, inode_y = 0.5, 1.5
inode_width, inode_height = 4.2, 8.5

inode_box = FancyBboxPatch((inode_x, inode_y), inode_width, inode_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4A5568', edgecolor=inode_color,
                            linewidth=2.5)
ax.add_patch(inode_box)

# Inode header
ax.text(inode_x + inode_width/2, inode_y + inode_height - 0.35, 'Inode',
        fontsize=14, fontweight='bold', color=inode_color,
        ha='center', va='center')

# Metadaten section
meta_y = inode_y + inode_height - 1.0
ax.text(inode_x + 0.2, meta_y, 'Metadaten:', fontsize=10, fontweight='bold', 
        color=text_color, ha='left', va='center')

metadata = ['Size: 50 KB', 'Owner: 1000', 'Mode: 0644', 'Timestamps...']
for i, meta in enumerate(metadata):
    ax.text(inode_x + 0.3, meta_y - 0.35 - i*0.3, meta, fontsize=8, 
            color='#718096', ha='left', va='center', family='monospace')

# Separator line
sep1_y = meta_y - 1.6
ax.plot([inode_x + 0.1, inode_x + inode_width - 0.1], 
        [sep1_y, sep1_y], color=border_color, linewidth=1)

# ===== Direct blocks section (inside Inode) =====
direct_y = sep1_y - 0.4
ax.text(inode_x + 0.2, direct_y, 'Direct [0-11]:', fontsize=10, fontweight='bold', 
        color=direct_color, ha='left', va='center')

# Store positions for arrows
direct_positions = []
for i in range(6):
    entry_y = direct_y - 0.45 - i*0.4
    rect = FancyBboxPatch((inode_x + 0.15, entry_y - 0.15), 3.8, 0.35,
                          boxstyle="round,pad=0.01,rounding_size=0.03",
                          facecolor='#C6F6D5', edgecolor=direct_color, 
                          linewidth=1.5, alpha=0.7)
    ax.add_patch(rect)
    ax.text(inode_x + 2.05, entry_y, f'[{i}] → Block {42 + i*13}', fontsize=9, 
            color='#1A202C', ha='center', va='center', family='monospace', fontweight='bold')
    direct_positions.append((inode_x + inode_width - 0.05, entry_y))

ax.text(inode_x + 2.1, direct_y - 2.95, '... [6-11]', fontsize=9, color=direct_color, 
        ha='center', style='italic')

# Separator line
sep2_y = direct_y - 3.4
ax.plot([inode_x + 0.1, inode_x + inode_width - 0.1], 
        [sep2_y, sep2_y], color=border_color, linewidth=1)

# ===== Indirect pointers (inside Inode) =====
indirect_y = sep2_y - 0.5

# Single Indirect box
single_rect = FancyBboxPatch((inode_x + 0.15, indirect_y - 0.2), 3.8, 0.45,
                              boxstyle="round,pad=0.01,rounding_size=0.03",
                              facecolor='#C05621', edgecolor=indirect_color,
                              linewidth=2, alpha=0.7)
ax.add_patch(single_rect)
ax.text(inode_x + 2.05, indirect_y, 'Single Indirect', fontsize=10, fontweight='bold',
        color='#1A202C', ha='center', va='center')
single_arrow_start = (inode_x + inode_width - 0.05, indirect_y)

# Double Indirect box
double_y = indirect_y - 0.65
double_rect = FancyBboxPatch((inode_x + 0.15, double_y - 0.2), 3.8, 0.45,
                              boxstyle="round,pad=0.01,rounding_size=0.03",
                              facecolor='#9B2C2C', edgecolor=double_indirect_color,
                              linewidth=2, alpha=0.7)
ax.add_patch(double_rect)
ax.text(inode_x + 2.05, double_y, 'Double Indirect', fontsize=10, fontweight='bold',
        color='#1A202C', ha='center', va='center')
double_arrow_start = (inode_x + inode_width - 0.05, double_y)

# Triple Indirect box
triple_y = double_y - 0.65
triple_rect = FancyBboxPatch((inode_x + 0.15, triple_y - 0.2), 3.8, 0.45,
                              boxstyle="round,pad=0.01,rounding_size=0.03",
                              facecolor='#6B46C1', edgecolor=triple_indirect_color,
                              linewidth=2, alpha=0.7)
ax.add_patch(triple_rect)
ax.text(inode_x + 2.05, triple_y, 'Triple Indirect', fontsize=10, fontweight='bold',
        color='#1A202C', ha='center', va='center')
triple_arrow_start = (inode_x + inode_width - 0.05, triple_y)

# ===== Data Blocks Column (direct) =====
data_x = 6.5
ax.text(data_x + 1.3, 9.7, 'Datenblöcke', fontsize=12, fontweight='bold',
        color=text_color, ha='center', va='center')

# Direct data blocks
for i in range(4):
    block_y = 8.8 - i * 0.8
    rect = FancyBboxPatch((data_x, block_y - 0.3), 2.6, 0.6,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#C6F6D5', edgecolor=direct_color,
                          linewidth=2, alpha=0.8)
    ax.add_patch(rect)
    ax.text(data_x + 1.3, block_y, f'Block {42 + i*13}', fontsize=10,
            color='#1A202C', ha='center', va='center', fontweight='bold')
    
    # Arrow from direct box inside inode to data block
    arrow = FancyArrowPatch(direct_positions[i],
                            (data_x, block_y),
                            arrowstyle='->', mutation_scale=15,
                            color=direct_color, linewidth=2, alpha=0.8)
    ax.add_patch(arrow)

ax.text(data_x + 1.3, 5.7, '...', fontsize=14, color=direct_color, ha='center')

# ===== Single Indirect Block =====
single_idx_x = 6.5
single_idx_y = 4.5

single_box = FancyBboxPatch((single_idx_x, single_idx_y - 0.8), 2.6, 1.6,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#4A5568', edgecolor=indirect_color,
                             linewidth=2)
ax.add_patch(single_box)
ax.text(single_idx_x + 1.3, single_idx_y + 0.55, 'Index-Block', fontsize=9, fontweight='bold',
        color=indirect_color, ha='center', va='center')

# Entries in single indirect
for i, blk in enumerate([201, 445, 512]):
    ax.text(single_idx_x + 0.2, single_idx_y + 0.1 - i*0.35, f'→ {blk}', fontsize=9,
            color=indirect_color, ha='left', va='center', family='monospace')

# Arrow from Single Indirect box inside Inode
arrow_single = FancyArrowPatch(single_arrow_start,
                                (single_idx_x, single_idx_y + 0.1),
                                arrowstyle='->', mutation_scale=15,
                                color=indirect_color, linewidth=2.5,
                                connectionstyle="arc3,rad=-0.15")
ax.add_patch(arrow_single)

# Data blocks from single indirect
single_data_x = 10.5
for i, (blk, y_off) in enumerate([(201, 0.4), (445, -0.2)]):
    rect = FancyBboxPatch((single_data_x, single_idx_y + y_off - 0.25), 2.3, 0.5,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#4A5568', edgecolor=indirect_color,
                          linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)
    ax.text(single_data_x + 1.15, single_idx_y + y_off, f'Block {blk}', fontsize=9,
            color=indirect_color, ha='center', va='center', fontweight='bold')
    
    arrow = FancyArrowPatch((single_idx_x + 2.6, single_idx_y + 0.1 - i*0.35),
                            (single_data_x, single_idx_y + y_off),
                            arrowstyle='->', mutation_scale=12,
                            color=indirect_color, linewidth=1.5, alpha=0.8)
    ax.add_patch(arrow)

# ===== Double Indirect Block =====
double_idx_x = 6.5
double_idx_y = 2.5

double_box = FancyBboxPatch((double_idx_x, double_idx_y - 0.5), 2.6, 1.0,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#4A5568', edgecolor=double_indirect_color,
                             linewidth=2)
ax.add_patch(double_box)
ax.text(double_idx_x + 1.3, double_idx_y + 0.3, 'Index-Block', fontsize=9, fontweight='bold',
        color=double_indirect_color, ha='center', va='center')
ax.text(double_idx_x + 0.2, double_idx_y - 0.15, '→ Idx1, Idx2...', fontsize=8,
        color=double_indirect_color, ha='left', va='center', family='monospace')

# Arrow from Double Indirect box inside Inode
arrow_double = FancyArrowPatch(double_arrow_start,
                                (double_idx_x, double_idx_y),
                                arrowstyle='->', mutation_scale=15,
                                color=double_indirect_color, linewidth=2.5,
                                connectionstyle="arc3,rad=-0.2")
ax.add_patch(arrow_double)

# Second level index block
idx2_x = 10.5
idx2_box = FancyBboxPatch((idx2_x, double_idx_y - 0.35), 2.3, 0.8,
                           boxstyle="round,pad=0.01,rounding_size=0.05",
                           facecolor='#4A5568', edgecolor=double_indirect_color,
                           linewidth=1.5, alpha=0.9)
ax.add_patch(idx2_box)
ax.text(idx2_x + 1.15, double_idx_y + 0.2, 'Idx1', fontsize=8, fontweight='bold',
        color=double_indirect_color, ha='center', va='center')
ax.text(idx2_x + 0.15, double_idx_y - 0.1, '→789,321...', fontsize=7,
        color=double_indirect_color, ha='left', va='center', family='monospace')

arrow_d2 = FancyArrowPatch((double_idx_x + 2.6, double_idx_y - 0.1),
                            (idx2_x, double_idx_y),
                            arrowstyle='->', mutation_scale=12,
                            color=double_indirect_color, linewidth=1.5, alpha=0.8)
ax.add_patch(arrow_d2)

# ===== Triple Indirect (just indicating) =====
ax.text(6.5, 1.4, '... (3 Ebenen für sehr große Dateien)', fontsize=9, 
        color=triple_indirect_color, ha='left', va='center', style='italic')

arrow_triple = FancyArrowPatch(triple_arrow_start,
                                (6.3, 1.4),
                                arrowstyle='->', mutation_scale=12,
                                color=triple_indirect_color, linewidth=2,
                                connectionstyle="arc3,rad=-0.25", alpha=0.7)
ax.add_patch(arrow_triple)

# ===== Legend / Info Box =====
info_box = FancyBboxPatch((0.3, 0.15), 13.4, 1.0,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=border_color,
                           linewidth=1.5, alpha=0.9)
ax.add_patch(info_box)

# Legend items
legend_items = [
    (direct_color, '12 Direct', '48 KB'),
    (indirect_color, '1 Single Ind.', '4 MB'),
    (double_indirect_color, '1 Double Ind.', '4 GB'),
    (triple_indirect_color, '1 Triple Ind.', '4 TB'),
]

ax.text(0.6, 0.9, 'Max. Dateigröße (4KB Blöcke, 4B Pointer):', 
        fontsize=9, fontweight='bold', color=text_color, ha='left', va='center')

for i, (color, label, size) in enumerate(legend_items):
    x_pos = 0.8 + i * 3.2
    rect = Rectangle((x_pos, 0.35), 0.3, 0.3, facecolor=color, edgecolor='#1A202C', linewidth=1)
    ax.add_patch(rect)
    ax.text(x_pos + 0.45, 0.5, f'{label}: {size}', fontsize=9, color=text_color,
            ha='left', va='center')

ax.text(13.4, 0.5, '≈ 4 TB', fontsize=11, fontweight='bold', color=title_color,
        ha='right', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/inode-alloc.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created inode-alloc.png")
