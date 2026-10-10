#!/usr/bin/env python3
"""Preview: CPU Problem - Many programs, one CPU"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'
cpu_color = '#E53E3E'       # Red for CPU (bottleneck)
program_color = '#4299E1'   # Blue for programs
frame_color = '#4A5568'     # Dark gray for frame

fig, ax = plt.subplots(1, 1, figsize=(10, 7))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

# Main frame
frame = FancyBboxPatch((0.3, 0.3), 9.4, 6.4,
                        boxstyle="round,pad=0.02,rounding_size=0.2",
                        facecolor='none', edgecolor=frame_color, linewidth=3)
ax.add_patch(frame)

# Title
ax.text(5, 6.3, 'REALITÄT', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Programs at top
programs = ['Browser', 'Editor', 'Musik', 'Mail', 'System', '...']
program_x = [1.2, 2.7, 4.2, 5.7, 7.2, 8.5]

for i, (prog, x) in enumerate(zip(programs, program_x)):
    if prog != '...':
        box = FancyBboxPatch((x, 4.8), 1.3, 0.7,
                              boxstyle="round,pad=0.02,rounding_size=0.1",
                              facecolor=program_color, edgecolor=border_color, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + 0.65, 5.15, prog, ha='center', va='center',
                fontsize=9, fontweight='bold', color=text_light)
    else:
        ax.text(x + 0.3, 5.15, '...', ha='center', va='center',
                fontsize=12, fontweight='bold', color=text_outside)

# Arrows converging to CPU
for x in program_x[:-1]:  # Skip '...'
    ax.annotate('', xy=(5, 2.7), xytext=(x + 0.65, 4.8),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# CPU at bottom
cpu_box = FancyBboxPatch((3.8, 1.5), 2.4, 1.2,
                          boxstyle="round,pad=0.02,rounding_size=0.15",
                          facecolor=cpu_color, edgecolor=border_color, linewidth=2)
ax.add_patch(cpu_box)
ax.text(5, 2.25, 'CPU', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_light)
ax.text(5, 1.85, '(1 Kern)', ha='center', va='center',
        fontsize=10, color=text_light)

# Annotation
ax.text(7.2, 2.1, '← Nur EINE CPU!', ha='left', va='center',
        fontsize=10, color=text_outside, style='italic')

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-cpu-problem.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
