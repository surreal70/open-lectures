#!/usr/bin/env python3
"""
Creates a metadata-only journaling diagram for 04-Journaling.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure with dark theme
fig, ax = plt.subplots(1, 1, figsize=(12, 6))

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
ax.set_ylim(1, 7)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 6.5, 'Metadata-Only Journaling (Writeback Mode)', 
        fontsize=18, fontweight='bold', color=title_color,
        ha='center', va='center')

# ===== Flow diagram =====
# Journal box
journal_box = FancyBboxPatch((1.5, 4.0), 3.0, 2.0,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor='#E9D8FD', edgecolor=journal_color,
                              linewidth=2)
ax.add_patch(journal_box)
ax.text(3.0, 5.5, 'Journal', fontsize=12, fontweight='bold',
        color='#1A202C', ha='center', va='center')
ax.text(3.0, 4.9, 'Metadata', fontsize=11, color='#553C9A',
        ha='center', va='center')
ax.text(3.0, 4.4, 'only', fontsize=11, color='#553C9A',
        ha='center', va='center')

# Filesystem box
fs_box = FancyBboxPatch((7.5, 2.0), 4.0, 4.0,
                         boxstyle="round,pad=0.02,rounding_size=0.1",
                         facecolor='#4A5568', edgecolor=fs_color,
                         linewidth=2)
ax.add_patch(fs_box)
ax.text(9.5, 5.7, 'Dateisystem', fontsize=12, fontweight='bold',
        color=fs_color, ha='center', va='center')

# Metadata section in FS
meta_fs = FancyBboxPatch((7.8, 4.3), 3.4, 1.2,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#4A5568', edgecolor=metadata_color,
                          linewidth=2)
ax.add_patch(meta_fs)
ax.text(9.5, 4.9, 'Metadaten', fontsize=11, color=metadata_color,
        ha='center', va='center', fontweight='bold')

# Data section in FS
data_fs = FancyBboxPatch((7.8, 2.3), 3.4, 1.7,
                          boxstyle="round,pad=0.01,rounding_size=0.05",
                          facecolor='#4A5568', edgecolor=data_color,
                          linewidth=2)
ax.add_patch(data_fs)
ax.text(9.5, 3.15, 'Datenblöcke', fontsize=11, color=data_color,
        ha='center', va='center', fontweight='bold')

# Arrow: Journal -> FS Metadata
arrow_j_meta = FancyArrowPatch((4.5, 5.0), (7.8, 4.9),
                                arrowstyle='->', mutation_scale=15,
                                color=metadata_color, linewidth=2.5)
ax.add_patch(arrow_j_meta)

# Data arrow (direct to FS, bypassing journal)
data_label_box = FancyBboxPatch((1.5, 2.0), 3.0, 1.5,
                                 boxstyle="round,pad=0.02,rounding_size=0.1",
                                 facecolor='#C6F6D5', edgecolor=data_color,
                                 linewidth=2)
ax.add_patch(data_label_box)
ax.text(3.0, 3.0, 'Daten', fontsize=12, fontweight='bold',
        color='#1A202C', ha='center', va='center')
ax.text(3.0, 2.4, '(direkt, ohne Journal)', fontsize=9, color='#276749',
        ha='center', va='center')

# Arrow: Data -> FS Data (bypassing journal)
arrow_data = FancyArrowPatch((4.5, 2.75), (7.8, 3.15),
                              arrowstyle='->', mutation_scale=15,
                              color=data_color, linewidth=2.5)
ax.add_patch(arrow_data)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/metadata-journaling.png',
            dpi=150, transparent=True, edgecolor='none', bbox_inches='tight')
plt.close()

print("Created metadata-journaling.png")
