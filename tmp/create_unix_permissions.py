#!/usr/bin/env python3
"""
Unix Permissions Diagram
Shows: rwx bits for owner, group, others
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
type_color = '#3182CE'       # Blue for type
user_color = '#38A169'       # Green for user
group_color = '#DD6B20'      # Orange for group
other_color = '#805AD5'      # Purple for other
owner_color = '#38A169'      # Green for owner

fig, ax = plt.subplots(1, 1, figsize=(14, 7), facecolor='none')
ax.set_xlim(-1, 15)
ax.set_ylim(1, 11)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(7, 10.3, 'Unix-Berechtigungen', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# Main permission string display: -rwxr-xr--
# Centered at x=7, 10 characters
# Character positions (0-indexed): - r w x r - x r - -
#                                   0 1 2 3 4 5 6 7 8 9
perm_string = '-rwxr-xr--'
ax.text(7, 8.5, perm_string, ha='center', va='center',
        fontsize=28, color='#1A202C', fontweight='bold', family='monospace',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#4A5568', edgecolor=text_color))

# Calculate character positions
# With 10 chars centered at 7, char width ~0.36 to fit within box boundaries
char_width = 0.36
# Center of string is between char 4 and 5, so char 0 starts at 7 - 5*char_width + char_width/2
char_start = 7 - 5 * char_width + char_width / 2

def char_pos(idx):
    return char_start + idx * char_width

# Brackets and labels
# Type: char 0 (-) - only vertical line, explanation in markdown table
type_x = char_pos(0)
ax.plot([type_x, type_x], [7.8, 6.5], color=type_color, lw=2)
ax.text(type_x, 6.0, 'Typ', ha='center', va='top', fontsize=10, color=type_color, fontweight='bold')

# Owner (rwx): chars 1-3 - no gap with next section
owner_start = char_pos(0) + char_width/2  # Start right after type
owner_end = char_pos(3) + char_width/2    # End at boundary with group
owner_mid = char_pos(2)
ax.plot([owner_start, owner_end], [7.8, 7.8], color=owner_color, lw=3)
ax.plot([owner_mid, owner_mid], [7.8, 6.5], color=owner_color, lw=2)
ax.text(owner_mid, 6.0, 'Owner', ha='center', va='top', fontsize=10, color=owner_color, fontweight='bold')
ax.text(owner_mid, 5.4, 'rwx = 7', ha='center', va='top', fontsize=9, color=text_color)

# Group (r-x): chars 4-6 - no gap
group_start = char_pos(3) + char_width/2  # Start right after owner
group_end = char_pos(6) + char_width/2    # End at boundary with others
group_mid = char_pos(5)
ax.plot([group_start, group_end], [7.8, 7.8], color=group_color, lw=3)
ax.plot([group_mid, group_mid], [7.8, 6.5], color=group_color, lw=2)
ax.text(group_mid, 6.0, 'Group', ha='center', va='top', fontsize=10, color=group_color, fontweight='bold')
ax.text(group_mid, 5.4, 'r-x = 5', ha='center', va='top', fontsize=9, color=text_color)

# Others (r--): chars 7-9 - no gap
other_start = char_pos(6) + char_width/2  # Start right after group
other_end = char_pos(9) + char_width/2    # End at last char
other_mid = char_pos(8)
ax.plot([other_start, other_end], [7.8, 7.8], color=other_color, lw=3)
ax.plot([other_mid, other_mid], [7.8, 6.5], color=other_color, lw=2)
ax.text(other_mid, 6.0, 'Others', ha='center', va='top', fontsize=10, color=other_color, fontweight='bold')
ax.text(other_mid, 5.4, 'r-- = 4', ha='center', va='top', fontsize=9, color=text_color)

# Permission meaning table - aligned with the permission string box
table_y = 3.5
ax.text(7, table_y + 0.8, 'Berechtigungen:', ha='center', va='center',
        fontsize=12, color=text_color, fontweight='bold')

perms = [
    ('r', 'read', '4', 'Datei lesen / Verz. auflisten'),
    ('w', 'write', '2', 'Datei ändern / Dateien erstellen'),
    ('x', 'execute', '1', 'Ausführen / Verzeichnis betreten'),
]

# Align with permission box (centered around x=7)
for i, (bit, name, val, desc) in enumerate(perms):
    y = table_y - i * 0.7
    ax.text(4.5, y, bit, ha='center', va='center', fontsize=12, color='#1A202C', fontweight='bold', family='monospace')
    ax.text(5.2, y, f'= {name}', ha='left', va='center', fontsize=10, color=text_color)
    ax.text(7.0, y, f'= {val}', ha='left', va='center', fontsize=10, color=text_color, family='monospace')
    ax.text(8.0, y, desc, ha='left', va='center', fontsize=9, color=text_color)

# Calculation example is placed in markdown callout instead

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/unix-permissions.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: unix-permissions.png")
