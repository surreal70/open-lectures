#!/usr/bin/env python3
"""Preview: Context Switch - Sequence diagram"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'
process_a_color = '#48BB78'   # Green
process_b_color = '#4299E1'   # Blue
kernel_color = '#9F7AEA'      # Purple

fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(5, 7.7, 'Kontextwechsel (Context Switch)', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Time arrow
ax.annotate('', xy=(9.5, 7.2), xytext=(0.5, 7.2),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
ax.text(5, 7.45, 'Zeit', ha='center', va='center',
        fontsize=9, color=text_outside)

# Column headers
columns = [('Prozess A', 1.5, process_a_color), 
           ('Kernel', 5, kernel_color), 
           ('Prozess B', 8.5, process_b_color)]

for label, x, color in columns:
    box = FancyBboxPatch((x - 0.8, 6.5), 1.6, 0.5,
                          boxstyle="round,pad=0.02,rounding_size=0.1",
                          facecolor=color, edgecolor=border_color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x, 6.75, label, ha='center', va='center',
            fontsize=10, fontweight='bold', color=text_light)

# Vertical lifelines
for label, x, color in columns:
    ax.plot([x, x], [6.5, 0.8], color=border_color, lw=1.5, linestyle='--')

# Process A running (active bar)
ax.add_patch(Rectangle((1.35, 5.0), 0.3, 1.4, facecolor=process_a_color, edgecolor=border_color))

# Interrupt arrow: A -> Kernel
ax.annotate('', xy=(4.7, 5.5), xytext=(1.65, 5.5),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))
ax.text(3.2, 5.7, 'Interrupt', ha='center', va='center',
        fontsize=9, color=text_outside)

# Kernel active bar
ax.add_patch(Rectangle((4.85, 2.5), 0.3, 3.0, facecolor=kernel_color, edgecolor=border_color))

# Kernel actions box
kernel_box = FancyBboxPatch((5.5, 3.2), 2.2, 1.8,
                             boxstyle="round,pad=0.02,rounding_size=0.1",
                             facecolor='none', edgecolor=border_color, linewidth=1)
ax.add_patch(kernel_box)
ax.text(6.6, 4.6, '1. PCB(A)', ha='center', va='center',
        fontsize=9, color=text_outside)
ax.text(6.6, 4.25, '   sichern', ha='center', va='center',
        fontsize=9, color=text_outside)
ax.text(6.6, 3.7, '2. PCB(B)', ha='center', va='center',
        fontsize=9, color=text_outside)
ax.text(6.6, 3.35, '   laden', ha='center', va='center',
        fontsize=9, color=text_outside)

# Dispatch arrow: Kernel -> B
ax.annotate('', xy=(8.35, 2.5), xytext=(5.15, 2.5),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1.5))
ax.text(6.75, 2.7, 'Dispatch', ha='center', va='center',
        fontsize=9, color=text_outside)

# Process B running (active bar)
ax.add_patch(Rectangle((8.35, 1.0), 0.3, 1.5, facecolor=process_b_color, edgecolor=border_color))

# Status labels
ax.text(1.5, 1.3, 'idle', ha='center', va='center',
        fontsize=9, color=text_outside, style='italic')
ax.text(8.5, 1.3, 'läuft', ha='center', va='center',
        fontsize=9, color=text_outside, style='italic')

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-context-switch.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
