#!/usr/bin/env python3
"""Preview: CPU Abstraction - Virtual CPUs through processes"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'
cpu_color = '#E53E3E'         # Red for physical CPU
process_color = '#48BB78'     # Green for processes
os_color = '#9F7AEA'          # Purple for OS/Scheduler
frame_color = '#4A5568'

fig, ax = plt.subplots(1, 1, figsize=(10, 9))
ax.set_xlim(0, 10)
ax.set_ylim(0, 9)
ax.set_aspect('equal')
ax.axis('off')

# Main frame
frame = FancyBboxPatch((0.3, 0.3), 9.4, 8.4,
                        boxstyle="round,pad=0.02,rounding_size=0.2",
                        facecolor='none', edgecolor=frame_color, linewidth=3)
ax.add_patch(frame)

# Title
ax.text(5, 8.3, 'ABSTRAKTION (Illusion)', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Processes at top
processes = [('Prozess A', 1.0), ('Prozess B', 3.0), ('Prozess C', 5.0), ('Prozess D', 7.0)]
for label, x in processes:
    box = FancyBboxPatch((x, 6.3), 1.8, 1.4,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=process_color, edgecolor=border_color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x + 0.9, 7.2, label, ha='center', va='center',
            fontsize=9, fontweight='bold', color=text_light)
    ax.text(x + 0.9, 6.7, '"Meine\nCPU"', ha='center', va='center',
            fontsize=8, color=text_light)

# Arrows from processes down
for label, x in processes:
    ax.annotate('', xy=(5, 5.0), xytext=(x + 0.9, 6.3),
                arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))

# OS/Scheduler box
os_box = FancyBboxPatch((2.5, 3.5), 5, 1.2,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         facecolor=os_color, edgecolor=border_color, linewidth=2)
ax.add_patch(os_box)
ax.text(5, 4.3, 'Betriebssystem', ha='center', va='center',
        fontsize=12, fontweight='bold', color=text_light)
ax.text(5, 3.85, '(Scheduler)', ha='center', va='center',
        fontsize=10, color=text_light)

# Arrow from OS to CPU
ax.annotate('', xy=(5, 2.5), xytext=(5, 3.5),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))

# Physical CPU at bottom
cpu_box = FancyBboxPatch((3.5, 1.2), 3, 1.2,
                          boxstyle="round,pad=0.02,rounding_size=0.15",
                          facecolor=cpu_color, edgecolor=border_color, linewidth=2)
ax.add_patch(cpu_box)
ax.text(5, 1.95, 'Physische', ha='center', va='center',
        fontsize=11, fontweight='bold', color=text_light)
ax.text(5, 1.55, 'CPU', ha='center', va='center',
        fontsize=11, fontweight='bold', color=text_light)

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-cpu-abstraction.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
