#!/usr/bin/env python3
"""
Open File Tables Diagram
Shows: Per-Process FD Table -> System Open File Table -> Inode Table
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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
process_color = '#3182CE'    # Blue for process
system_color = '#38A169'     # Green for system table
inode_color = '#805AD5'      # Purple for inodes

fig, ax = plt.subplots(1, 1, figsize=(14, 11), facecolor='none')
ax.set_xlim(-2.5, 15)
ax.set_ylim(-1, 14)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(7, 13.3, 'Open File Tables', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# ============ Process A FD Table ============
proc_a = FancyBboxPatch((0.5, 9), 4, 3.5,
                        boxstyle="round,pad=0.05,rounding_size=0.2",
                        facecolor='#4A5568', edgecolor=process_color, linewidth=2)
ax.add_patch(proc_a)
ax.text(2.5, 12, 'Prozess A', ha='center', va='center', fontsize=12, color=process_color, fontweight='bold')
ax.text(2.5, 11.3, 'FD-Tabelle', ha='center', va='center', fontsize=10, color=text_color)

fd_entries_a = ['0: stdin', '1: stdout', '2: stderr', '3: →']
for i, entry in enumerate(fd_entries_a):
    ax.text(1.2, 10.5 - i * 0.5, entry, ha='left', va='center', fontsize=9, color=text_color, family='monospace')

# ============ Process B FD Table ============
proc_b = FancyBboxPatch((9.5, 9), 4, 3.5,
                        boxstyle="round,pad=0.05,rounding_size=0.2",
                        facecolor='#4A5568', edgecolor=process_color, linewidth=2)
ax.add_patch(proc_b)
ax.text(11.5, 12, 'Prozess B', ha='center', va='center', fontsize=12, color=process_color, fontweight='bold')
ax.text(11.5, 11.3, 'FD-Tabelle', ha='center', va='center', fontsize=10, color=text_color)

fd_entries_b = ['0: stdin', '1: stdout', '2: stderr', '3: →']
for i, entry in enumerate(fd_entries_b):
    ax.text(10.2, 10.5 - i * 0.5, entry, ha='left', va='center', fontsize=9, color=text_color, family='monospace')

# ============ System-wide Open File Table ============
sys_table = FancyBboxPatch((3, 4), 8, 3.5,
                           boxstyle="round,pad=0.05,rounding_size=0.2",
                           facecolor='#4A5568', edgecolor=system_color, linewidth=2)
ax.add_patch(sys_table)
ax.text(7, 7, 'System-weite Open File Table', ha='center', va='center', 
        fontsize=12, color=system_color, fontweight='bold')

entries = [
    'Entry 1: Mode=READ,  Offset=0,    Inode→',
    'Entry 2: Mode=WRITE, Offset=1024, Inode→',
]
for i, entry in enumerate(entries):
    ax.text(3.5, 6 - i * 0.7, entry, ha='left', va='center', fontsize=9, color=text_color, family='monospace')

# ============ In-Memory Inode Table ============
inode_table = FancyBboxPatch((3, 0), 8, 2.8,
                             boxstyle="round,pad=0.05,rounding_size=0.2",
                             facecolor='#4A5568', edgecolor=inode_color, linewidth=2)
ax.add_patch(inode_table)
ax.text(7, 2.4, 'In-Memory Inode Table', ha='center', va='center', 
        fontsize=12, color=inode_color, fontweight='bold')
ax.text(7, 1.5, 'Inode 4711: Size=4096, Blocks=[...], RefCount=2', ha='center', va='center', 
        fontsize=9, color=text_color, family='monospace')
ax.text(7, 0.7, 'Inode 8823: Size=1024, Blocks=[...], RefCount=1', ha='center', va='center', 
        fontsize=9, color=text_color, family='monospace')

# ============ Arrows ============
# Process A -> System Table
ax.annotate('', xy=(5, 7), xytext=(3.5, 9),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Process B -> System Table
ax.annotate('', xy=(9, 7), xytext=(10.5, 9),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# System Table -> Inode Table
ax.annotate('', xy=(7, 2.8), xytext=(7, 4),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Labels for the three levels (moved to left side to avoid overlap)
ax.text(-1.8, 10.5, '1. Per-Process', ha='left', va='center', fontsize=10, color=process_color, fontweight='bold')
ax.text(-1.8, 5.5, '2. System-wide', ha='left', va='center', fontsize=10, color=system_color, fontweight='bold')
ax.text(-1.8, 1.4, '3. Inode Cache', ha='left', va='center', fontsize=10, color=inode_color, fontweight='bold')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/open-file-tables.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: open-file-tables.png")
