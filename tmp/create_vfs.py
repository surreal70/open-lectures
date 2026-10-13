#!/usr/bin/env python3
"""
Virtual File System (VFS) Diagram
Shows: Applications -> VFS -> Different FS drivers -> Storage
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
app_color = '#3182CE'        # Blue for application
vfs_color = '#805AD5'        # Purple for VFS
fs_impl_color = '#38A169'    # Green for FS implementation
driver_color = '#DD6B20'     # Orange for driver
storage_color = '#718096'    # Gray for storage

fig, ax = plt.subplots(1, 1, figsize=(12, 10), facecolor='none')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 13)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(6, 12.3, 'Virtual File System (VFS)', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# Layer 1: Applications
app_box = FancyBboxPatch((1, 10), 10, 1.5,
                         boxstyle="round,pad=0.05,rounding_size=0.2",
                         facecolor=app_color, edgecolor=text_color, linewidth=2)
ax.add_patch(app_box)
ax.text(6, 11, 'Anwendungen', ha='center', va='center',
        fontsize=14, color='#1A202C', fontweight='bold')
ax.text(6, 10.4, 'open(), read(), write(), close()', ha='center', va='center',
        fontsize=10, color='#1A202C', family='monospace')

# Arrow
ax.annotate('', xy=(6, 8.8), xytext=(6, 9.9),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=3))
ax.text(7, 9.35, 'System Calls', ha='left', va='center', fontsize=9, color=text_color)

# Layer 2: VFS
vfs_box = FancyBboxPatch((1, 7), 10, 1.6,
                         boxstyle="round,pad=0.05,rounding_size=0.2",
                         facecolor=vfs_color, edgecolor=text_color, linewidth=2)
ax.add_patch(vfs_box)
ax.text(6, 8.1, 'VFS (Virtual File System)', ha='center', va='center',
        fontsize=14, color='#1A202C', fontweight='bold')
ax.text(6, 7.4, 'Einheitliche API für alle Dateisysteme', ha='center', va='center',
        fontsize=10, color='#1A202C')

# Arrows to drivers (fan out)
for x in [2.5, 6, 9.5]:
    ax.annotate('', xy=(x, 5.8), xytext=(6, 6.9),
                arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Layer 3: FS Drivers
drivers = [
    ('ext4', 2.5, driver_color),
    ('NTFS', 6, '#4299E1'),
    ('NFS', 9.5, '#D69E2E'),
]
for name, x, color in drivers:
    driver_box = FancyBboxPatch((x-1.5, 4.3), 3, 1.3,
                                boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=color, edgecolor=text_color, linewidth=2)
    ax.add_patch(driver_box)
    ax.text(x, 5.2, name, ha='center', va='center', fontsize=11, color='#1A202C', fontweight='bold')
    ax.text(x, 4.6, 'Treiber', ha='center', va='center', fontsize=9, color='#1A202C')

# Arrows to storage
for x in [2.5, 6, 9.5]:
    ax.annotate('', xy=(x, 2.8), xytext=(x, 4.2),
                arrowprops=dict(arrowstyle='->', color=text_color, lw=2))

# Layer 4: Physical Storage
storages = [
    ('SSD/HDD', 2.5),
    ('USB-Disk', 6),
    ('Netzwerk', 9.5),
]
for name, x in storages:
    storage_box = FancyBboxPatch((x-1.5, 1.3), 3, 1.3,
                                 boxstyle="round,pad=0.05,rounding_size=0.15",
                                 facecolor=storage_color, edgecolor=text_color, linewidth=2)
    ax.add_patch(storage_box)
    ax.text(x, 1.95, name, ha='center', va='center', fontsize=10, color='#1A202C', fontweight='bold')

# VFS Objects info
vfs_info = FancyBboxPatch((0.5, -0.5), 11, 1.2,
                          boxstyle="round,pad=0.1,rounding_size=0.2",
                          facecolor='#4A5568', edgecolor=vfs_color, linewidth=2, alpha=0.9)
ax.add_patch(vfs_info)
ax.text(6, 0.1, 'VFS-Objekte: Superblock (FS-Metadaten) | Inode (Datei-Metadaten) | Dentry (Name→Inode) | File (geöffnete Datei)', 
        ha='center', va='center', fontsize=9, color=text_color)

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/vfs.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: vfs.png")
