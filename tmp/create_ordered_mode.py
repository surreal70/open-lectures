#!/usr/bin/env python3
"""
Creates an ordered mode journaling diagram for 04-Journaling.md
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

fig.patch.set_facecolor('none')
ax.set_facecolor('none')
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 6.5, 'Ordered Mode (ext4 Default)', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

ax.text(6, 6.0, 'Reihenfolge garantiert: Daten vor Metadaten', 
        fontsize=11, color=text_color, ha='center', va='center', style='italic')

# ===== Step boxes =====
step_height = 1.0
step_width = 2.8

# Step 1: Data blocks to Disk
step1_box = FancyBboxPatch((0.5, 4.2), step_width, step_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#C6F6D5', edgecolor=data_color,
                            linewidth=2)
ax.add_patch(step1_box)
step1_circle = plt.Circle((0.9, 5.0), 0.25, color=data_color, fill=True)
ax.add_patch(step1_circle)
ax.text(0.9, 5.0, '1', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(1.9, 4.9, 'Datenblöcke', fontsize=10, color='#1A202C',
        ha='center', va='center', fontweight='bold')
ax.text(1.9, 4.5, 'auf Disk', fontsize=10, color='#276749',
        ha='center', va='center')

# Step 2: Metadata to Journal
step2_box = FancyBboxPatch((0.5, 2.8), step_width, step_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#E9D8FD', edgecolor=journal_color,
                            linewidth=2)
ax.add_patch(step2_box)
step2_circle = plt.Circle((0.9, 3.6), 0.25, color=journal_color, fill=True)
ax.add_patch(step2_circle)
ax.text(0.9, 3.6, '2', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(1.9, 3.5, 'Metadaten', fontsize=10, color='#1A202C',
        ha='center', va='center', fontweight='bold')
ax.text(1.9, 3.1, 'ins Journal', fontsize=10, color='#553C9A',
        ha='center', va='center')

# Step 3: Commit
step3_box = FancyBboxPatch((0.5, 1.4), step_width, step_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#C6F6D5', edgecolor='#48BB78',
                            linewidth=2)
ax.add_patch(step3_box)
step3_circle = plt.Circle((0.9, 2.2), 0.25, color='#48BB78', fill=True)
ax.add_patch(step3_circle)
ax.text(0.9, 2.2, '3', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(1.9, 2.1, 'Journal-Commit', fontsize=10, color='#1A202C',
        ha='center', va='center', fontweight='bold')
ax.text(1.9, 1.7, 'schreiben', fontsize=10, color='#276749',
        ha='center', va='center')

# Step 4: Metadata to Disk
step4_box = FancyBboxPatch((0.5, 0.0), step_width, step_height,
                            boxstyle="round,pad=0.02,rounding_size=0.1",
                            facecolor='#4A5568', edgecolor=metadata_color,
                            linewidth=2)
ax.add_patch(step4_box)
step4_circle = plt.Circle((0.9, 0.8), 0.25, color=metadata_color, fill=True)
ax.add_patch(step4_circle)
ax.text(0.9, 0.8, '4', fontsize=10, fontweight='bold', color='#1A202C',
        ha='center', va='center')
ax.text(1.9, 0.7, 'Metadaten', fontsize=10, color=metadata_color,
        ha='center', va='center', fontweight='bold')
ax.text(1.9, 0.3, 'auf FS-Bereich', fontsize=10, color=text_color,
        ha='center', va='center')

# Arrows between steps
for y_start, y_end in [(4.2, 3.85), (2.8, 2.45), (1.4, 1.05)]:
    ax.annotate('', xy=(1.9, y_end), xytext=(1.9, y_start),
                arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# ===== Right side: Journal and Disk =====
# Journal (moved down to avoid collision with green arrow)
journal_box = FancyBboxPatch((5.5, 1.8), 2.5, 2.0,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#4A5568', edgecolor=journal_color,
                              linewidth=2)
ax.add_patch(journal_box)
ax.text(6.75, 3.5, 'Journal', fontsize=11, fontweight='bold',
        color=journal_color, ha='center', va='center')
ax.text(6.75, 2.8, 'Metadata', fontsize=10, color='#553C9A',
        ha='center', va='center')
ax.text(6.75, 2.3, 'Commit', fontsize=10, color='#276749',
        ha='center', va='center')

# Disk
disk_box = FancyBboxPatch((9, 1.0), 2.5, 4.5,
                           boxstyle="round,pad=0.02,rounding_size=0.1",
                           facecolor='#4A5568', edgecolor=disk_color,
                           linewidth=2)
ax.add_patch(disk_box)
ax.text(10.25, 5.2, 'Disk', fontsize=11, fontweight='bold',
        color=disk_color, ha='center', va='center')

# Data area in disk
data_disk = FancyBboxPatch((9.2, 3.5), 2.1, 1.3,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#C6F6D5', edgecolor=data_color,
                            linewidth=1.5, alpha=0.8)
ax.add_patch(data_disk)
ax.text(10.25, 4.15, 'Datenblöcke', fontsize=9, color='#1A202C',
        ha='center', va='center', fontweight='bold')

# Metadata area in disk
meta_disk = FancyBboxPatch((9.2, 1.3), 2.1, 1.8,
                            boxstyle="round,pad=0.01,rounding_size=0.05",
                            facecolor='#4A5568', edgecolor=metadata_color,
                            linewidth=1.5)
ax.add_patch(meta_disk)
ax.text(10.25, 2.2, 'Metadaten', fontsize=9, color=metadata_color,
        ha='center', va='center', fontweight='bold')

# Arrows
# Step 1 -> Disk Data
arrow1 = FancyArrowPatch((3.3, 4.7), (9.2, 4.15),
                          arrowstyle='->', mutation_scale=15,
                          color=data_color, linewidth=2.5)
ax.add_patch(arrow1)

# Step 2 -> Journal (adjusted for moved journal box)
arrow2 = FancyArrowPatch((3.3, 3.3), (5.5, 2.8),
                          arrowstyle='->', mutation_scale=15,
                          color=journal_color, linewidth=2)
ax.add_patch(arrow2)

# Journal -> Disk Metadata (Step 4) (adjusted for moved journal box)
arrow4 = FancyArrowPatch((8.0, 2.3), (9.2, 2.2),
                          arrowstyle='->', mutation_scale=15,
                          color=metadata_color, linewidth=2,
                          connectionstyle="arc3,rad=0.2")
ax.add_patch(arrow4)

# ===== Guarantee box =====
guarantee_box = FancyBboxPatch((4.5, 0.2), 7.2, 0.8,
                                boxstyle="round,pad=0.02,rounding_size=0.1",
                                facecolor='#4A5568', edgecolor=border_color,
                                linewidth=1.5)
ax.add_patch(guarantee_box)

ax.text(4.8, 0.6, 'Garantie:', fontsize=10, fontweight='bold', 
        color=title_color, ha='left', va='center')
ax.text(6.0, 0.6, 'Metadaten zeigen nie auf ungeschriebene Datenblöcke', 
        fontsize=9, color=text_color, ha='left', va='center')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/ordered-mode.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created ordered-mode.png")
