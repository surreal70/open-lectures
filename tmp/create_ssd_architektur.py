#!/usr/bin/env python3
"""
SSD Architecture Diagram
Shows layers: Host -> Controller (FTL, DRAM, Cache) -> NAND Flash
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Colors (theme-agnostic, matching project style)
box_fill = '#3182CE'        # Blue for main components
text_color = '#4A5568'      # Gray for labels
host_color = '#9F7AEA'      # Purple for host
controller_color = '#38A169'  # Green for controller
ftl_color = '#D69E2E'       # Gold for FTL
nand_color = '#ED8936'      # Orange for NAND
dram_color = '#4299E1'      # Light blue for DRAM
highlight_bg = '#E2E8F0'    # Dark background

fig, ax = plt.subplots(1, 1, figsize=(12, 10), facecolor='none')
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 13)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('none')

# Title
ax.text(6, 12.3, 'SSD-Architektur', ha='center', va='center',
        fontsize=18, color=text_color, fontweight='bold')

# ============ HOST ============
host_box = FancyBboxPatch((1, 10.5), 10, 1.2,
                          boxstyle="round,pad=0.05,rounding_size=0.2",
                          facecolor=host_color, edgecolor=text_color, linewidth=2)
ax.add_patch(host_box)
ax.text(6, 11.1, 'Host (Computer)', ha='center', va='center',
        fontsize=14, color='#1A202C', fontweight='bold')

# Arrow: Host -> Controller
ax.annotate('', xy=(6, 9.3), xytext=(6, 10.4),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=3))
ax.text(7, 9.85, 'SATA / NVMe', ha='left', va='center',
        fontsize=10, color=text_color)

# ============ SSD CONTROLLER ============
controller_outer = FancyBboxPatch((0.5, 4.5), 11, 4.6,
                                  boxstyle="round,pad=0.05,rounding_size=0.2",
                                  facecolor='#4A5568', edgecolor=controller_color, linewidth=3)
ax.add_patch(controller_outer)
ax.text(6, 8.8, 'SSD Controller', ha='center', va='center',
        fontsize=14, color=controller_color, fontweight='bold')

# FTL Box (main component)
ftl_box = FancyBboxPatch((1.2, 6.2), 9.6, 2.2,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         facecolor=ftl_color, edgecolor=text_color, linewidth=2, alpha=0.9)
ax.add_patch(ftl_box)
ax.text(6, 7.9, 'Flash Translation Layer (FTL)', ha='center', va='center',
        fontsize=12, color='#1A202C', fontweight='bold')

# FTL details
ftl_details = [
    '• Logical → Physical Mapping',
    '• Wear Leveling',
    '• Garbage Collection',
]
for i, text in enumerate(ftl_details):
    ax.text(2, 7.2 - i * 0.4, text, ha='left', va='center',
            fontsize=10, color='#1A202C')

# DRAM and Cache boxes side by side
dram_box = FancyBboxPatch((1.5, 5), 3.5, 1,
                          boxstyle="round,pad=0.05,rounding_size=0.1",
                          facecolor=dram_color, edgecolor=text_color, linewidth=1.5)
ax.add_patch(dram_box)
ax.text(3.25, 5.5, 'DRAM (Map Table)', ha='center', va='center',
        fontsize=10, color='#1A202C', fontweight='bold')

cache_box = FancyBboxPatch((7, 5), 3.5, 1,
                           boxstyle="round,pad=0.05,rounding_size=0.1",
                           facecolor=dram_color, edgecolor=text_color, linewidth=1.5)
ax.add_patch(cache_box)
ax.text(8.75, 5.5, 'Cache', ha='center', va='center',
        fontsize=10, color='#1A202C', fontweight='bold')

# Arrow: Controller -> NAND
ax.annotate('', xy=(6, 3.3), xytext=(6, 4.4),
            arrowprops=dict(arrowstyle='->', color=text_color, lw=3))

# ============ NAND FLASH CHIPS ============
nand_outer = FancyBboxPatch((0.5, 0.5), 11, 2.6,
                            boxstyle="round,pad=0.05,rounding_size=0.2",
                            facecolor='#4A5568', edgecolor=nand_color, linewidth=3)
ax.add_patch(nand_outer)
ax.text(6, 2.8, 'NAND Flash Chips', ha='center', va='center',
        fontsize=12, color=nand_color, fontweight='bold')

# Individual NAND dies
die_width = 1.6
die_height = 1.2
die_labels = ['Die 0', 'Die 1', 'Die 2', 'Die 3', '...']
start_x = 1.2

for i, label in enumerate(die_labels):
    x = start_x + i * (die_width + 0.4)
    die_box = FancyBboxPatch((x, 1), die_width, die_height,
                             boxstyle="round,pad=0.03,rounding_size=0.08",
                             facecolor=nand_color, edgecolor=text_color, linewidth=1.5, alpha=0.85)
    ax.add_patch(die_box)
    ax.text(x + die_width/2, 1.6, label, ha='center', va='center',
            fontsize=10, color='#1A202C', fontweight='bold')

plt.tight_layout()
plt.savefig('/media/andhue/Wissen/open-lectures/L-Betriebssysteme, Rechnernetze und verteilte Systeme/02-Betriebssysteme/07-Dateisysteme/assets/ssd-architektur.png',
            dpi=150, bbox_inches='tight', transparent=True)
plt.close()

print("Created: ssd-architektur.png")
