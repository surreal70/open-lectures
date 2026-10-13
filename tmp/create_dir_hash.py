#!/usr/bin/env python3
"""
Creates a directory with hash table diagram for 03-Implementierung.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(13, 8))

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
hash_color = '#805AD5'       # Purple for hash
dir_color = '#3182CE'        # Blue for directory
entry_color = '#38A169'      # Green for entries
bucket_color = '#DD6B20'     # Orange for buckets
empty_color = '#E2E8F0'      # Light gray for empty

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 13)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6.5, 7.5, 'Verzeichnis mit Hash-Tabelle', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Hash Table =====
hash_x, hash_y = 1, 1.5
hash_width, hash_height = 2.5, 5

hash_box = FancyBboxPatch((hash_x, hash_y), hash_width, hash_height,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=hash_color,
                           linewidth=2.5)
ax.add_patch(hash_box)

ax.text(hash_x + hash_width/2, hash_y + hash_height + 0.3, 'Hash-Tabelle',
        fontsize=12, fontweight='bold', color=hash_color,
        ha='center', va='center')

# Hash table entries (buckets)
buckets = [
    (0, bucket_color, True),   # Has entries
    (1, empty_color, False),   # Empty
    (2, bucket_color, True),   # Has entries (collision)
    (3, bucket_color, True),   # Has entries
    (4, empty_color, False),   # Empty
]

bucket_positions = []
for i, (idx, color, has_entries) in enumerate(buckets):
    bucket_y = hash_y + hash_height - 0.7 - i * 0.9
    
    rect = FancyBboxPatch((hash_x + 0.2, bucket_y - 0.3), hash_width - 0.4, 0.6,
                          boxstyle="round,pad=0.01,rounding_size=0.03",
                          facecolor=bg_color if not has_entries else highlight_bg, 
                          edgecolor=color, linewidth=2)
    ax.add_patch(rect)
    
    ax.text(hash_x + 0.5, bucket_y, str(idx), fontsize=11, fontweight='bold',
            color=color, ha='center', va='center')
    
    # Separator
    ax.plot([hash_x + 0.85, hash_x + 0.85], [bucket_y - 0.25, bucket_y + 0.25],
            color=border_color, linewidth=1)
    
    if has_entries:
        ax.text(hash_x + 1.8, bucket_y, '→', fontsize=14, color=color,
                ha='center', va='center')
        bucket_positions.append((hash_x + hash_width, bucket_y, idx, color))
    else:
        ax.text(hash_x + 1.8, bucket_y, 'NULL', fontsize=9, color=empty_color,
                ha='center', va='center', family='monospace')

# ===== Linked Lists (Buckets content) =====
lists_x = 5

# Bucket 0 - single entry
b0_y = bucket_positions[0][1]
entry0 = FancyBboxPatch((lists_x, b0_y - 0.35), 3.2, 0.7,
                         boxstyle="round,pad=0.01,rounding_size=0.05",
                         facecolor='#4A5568', edgecolor=bucket_color, linewidth=1.5)
ax.add_patch(entry0)
ax.text(lists_x + 1.2, b0_y + 0.1, 'notes.txt', fontsize=9, color='#1A202C',
        ha='center', va='center', family='monospace', fontweight='bold')
ax.text(lists_x + 1.2, b0_y - 0.2, 'Inode: 198', fontsize=8, color=text_color,
        ha='center', va='center')
ax.text(lists_x + 2.7, b0_y, '→ ∅', fontsize=10, color=bucket_color,
        ha='center', va='center')

arrow0 = FancyArrowPatch(bucket_positions[0][:2], (lists_x, b0_y),
                          arrowstyle='->', mutation_scale=12,
                          color=bucket_color, linewidth=2)
ax.add_patch(arrow0)

# Bucket 2 - collision (two entries)
b2_y = bucket_positions[1][1]
entry2a = FancyBboxPatch((lists_x, b2_y - 0.35), 3.2, 0.7,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#4A5568', edgecolor=bucket_color, linewidth=1.5)
ax.add_patch(entry2a)
ax.text(lists_x + 1.2, b2_y + 0.1, 'report.pdf', fontsize=9, color='#1A202C',
        ha='center', va='center', family='monospace', fontweight='bold')
ax.text(lists_x + 1.2, b2_y - 0.2, 'Inode: 247', fontsize=8, color=text_color,
        ha='center', va='center')
ax.text(lists_x + 2.7, b2_y, '→', fontsize=10, color=bucket_color,
        ha='center', va='center')

# Second entry in bucket 2
entry2b = FancyBboxPatch((lists_x + 3.5, b2_y - 0.35), 3.2, 0.7,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#4A5568', edgecolor=bucket_color, linewidth=1.5)
ax.add_patch(entry2b)
ax.text(lists_x + 4.7, b2_y + 0.1, 'config.ini', fontsize=9, color='#1A202C',
        ha='center', va='center', family='monospace', fontweight='bold')
ax.text(lists_x + 4.7, b2_y - 0.2, 'Inode: 301', fontsize=8, color=text_color,
        ha='center', va='center')
ax.text(lists_x + 6.2, b2_y, '→ ∅', fontsize=10, color=bucket_color,
        ha='center', va='center')

# Collision label
ax.text(lists_x + 3.35, b2_y + 0.55, 'Kollision!', fontsize=8, color='#E53E3E',
        ha='center', va='center', style='italic')

arrow2 = FancyArrowPatch(bucket_positions[1][:2], (lists_x, b2_y),
                          arrowstyle='->', mutation_scale=12,
                          color=bucket_color, linewidth=2)
ax.add_patch(arrow2)

# Bucket 3 - single entry
b3_y = bucket_positions[2][1]
entry3 = FancyBboxPatch((lists_x, b3_y - 0.35), 3.2, 0.7,
                         boxstyle="round,pad=0.01,rounding_size=0.05",
                         facecolor='#4A5568', edgecolor=bucket_color, linewidth=1.5)
ax.add_patch(entry3)
ax.text(lists_x + 1.2, b3_y + 0.1, 'documents', fontsize=9, color='#1A202C',
        ha='center', va='center', family='monospace', fontweight='bold')
ax.text(lists_x + 1.2, b3_y - 0.2, 'Inode: 103', fontsize=8, color=text_color,
        ha='center', va='center')
ax.text(lists_x + 2.7, b3_y, '→ ∅', fontsize=10, color=bucket_color,
        ha='center', va='center')

arrow3 = FancyArrowPatch(bucket_positions[2][:2], (lists_x, b3_y),
                          arrowstyle='->', mutation_scale=12,
                          color=bucket_color, linewidth=2)
ax.add_patch(arrow3)

# ===== Search Example =====
search_box = FancyBboxPatch((0.3, 0.3), 12.4, 1.0,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='#4A5568', edgecolor=border_color,
                             linewidth=1.5, alpha=0.9)
ax.add_patch(search_box)

ax.text(0.6, 1.0, 'Suche "report.pdf":', fontsize=10, fontweight='bold', 
        color=title_color, ha='left', va='center')

ax.text(2.8, 1.0, 'hash("report.pdf")', fontsize=9, color=hash_color,
        ha='left', va='center', family='monospace')
ax.text(5.2, 1.0, '→', fontsize=12, color=text_color, ha='center', va='center')
ax.text(5.6, 1.0, 'Bucket 2', fontsize=9, color=bucket_color,
        ha='left', va='center', fontweight='bold')
ax.text(6.9, 1.0, '→', fontsize=12, color=text_color, ha='center', va='center')
ax.text(7.3, 1.0, 'Lineare Suche in Bucket', fontsize=9, color=text_color,
        ha='left', va='center')

ax.text(0.6, 0.55, 'Komplexität:', fontsize=9, fontweight='bold', 
        color='#48BB78', ha='left', va='center')
ax.text(2.2, 0.55, 'O(1) durchschnittlich', fontsize=9, color=text_color,
        ha='left', va='center')

ax.text(5.5, 0.55, '|', fontsize=10, color=border_color, ha='center', va='center')

ax.text(6.0, 0.55, 'Worst Case:', fontsize=9, fontweight='bold', 
        color='#E53E3E', ha='left', va='center')
ax.text(7.6, 0.55, 'O(n) bei vielen Kollisionen', fontsize=9, color=text_color,
        ha='left', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/dir-hash.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created dir-hash.png")
