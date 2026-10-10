#!/usr/bin/env python3
"""Preview: Time Slicing - How the CPU illusion works"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# Theme-agnostic colors
text_outside = '#A0AEC0'
text_light = '#F7FAFC'
border_color = '#718096'
process_a_color = '#48BB78'   # Green
process_b_color = '#4299E1'   # Blue
process_c_color = '#ED8936'   # Orange
empty_color = '#4A5568'       # Dark gray for empty slots

fig, ax = plt.subplots(1, 1, figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')

# Title
ax.text(6, 5.7, 'Wie funktioniert die Illusion?', ha='center', va='center',
        fontsize=14, fontweight='bold', color=text_outside)

# Time arrow
ax.annotate('', xy=(11.5, 4.8), xytext=(0.5, 4.8),
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=2))
ax.text(6, 5.1, 'Zeit', ha='center', va='center',
        fontsize=10, color=text_outside)

# Time slice boxes - top row (actual execution)
colors = [process_a_color, process_b_color, process_c_color] * 4 + [text_outside]
labels = ['A', 'B', 'C'] * 4 + ['...']
slice_width = 0.75
start_x = 0.8

for i, (color, label) in enumerate(zip(colors, labels)):
    x = start_x + i * (slice_width + 0.1)
    if label != '...':
        box = Rectangle((x, 3.8), slice_width, 0.8,
                         facecolor=color, edgecolor=border_color, linewidth=1)
        ax.add_patch(box)
        ax.text(x + slice_width/2, 4.2, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color=text_light)
        # Tick marks
        ax.plot([x + slice_width/2, x + slice_width/2], [4.6, 4.75], 
                color=text_outside, lw=1)
    else:
        ax.text(x + 0.2, 4.2, '...', ha='center', va='center',
                fontsize=12, fontweight='bold', color=text_outside)

# Annotation for time slice
ax.annotate('Jede "Zeitscheibe"\n~10-100ms', xy=(1.2, 3.8), xytext=(0.3, 2.8),
            fontsize=9, color=text_outside,
            arrowprops=dict(arrowstyle='->', color=text_outside, lw=1))

# Separator
ax.text(6, 2.3, 'Aus Sicht von Prozess A:', ha='center', va='center',
        fontsize=10, color=text_outside, style='italic')

# Process A view - bottom row (with gaps)
for i in range(13):
    x = start_x + i * (slice_width + 0.1)
    if i % 3 == 0 and i < 12:  # Only A slots
        box = Rectangle((x, 1.0), slice_width, 0.8,
                         facecolor=process_a_color, edgecolor=border_color, linewidth=1)
        ax.add_patch(box)
        ax.text(x + slice_width/2, 1.4, 'A', ha='center', va='center',
                fontsize=10, fontweight='bold', color=text_light)
    elif i < 12:  # Empty slots (where B and C run)
        box = Rectangle((x, 1.0), slice_width, 0.8,
                         facecolor='none', edgecolor=border_color, linewidth=1, 
                         linestyle='--', alpha=0.5)
        ax.add_patch(box)
    else:
        ax.text(x + 0.2, 1.4, '...', ha='center', va='center',
                fontsize=12, fontweight='bold', color=text_outside)

# Quote
ax.text(6, 0.4, '"Ich laufe die ganze Zeit, nur etwas langsamer"', 
        ha='center', va='center', fontsize=10, color=text_outside, style='italic')

# Save preview
output_path = "/media/andhue/Wissen/open-lectures/tmp/preview-timeslicing.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight', 
            transparent=True, pad_inches=0.2)
plt.close()
print(f"Preview saved: {output_path}")
