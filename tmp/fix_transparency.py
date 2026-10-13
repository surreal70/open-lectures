#!/usr/bin/env python3
"""
Fix transparency issues in all scripts by:
1. Removing dark_background style
2. Setting transparent background
3. Adjusting text colors for visibility on both themes
"""

import os
import re

scripts = [
    # 03-Implementierung
    'create_bitmap.py',
    'create_buffer_cache.py',
    'create_contiguous_alloc.py',
    'create_dir_hash.py',
    'create_dir_linear.py',
    'create_disk_layout.py',
    'create_fat_alloc.py',
    'create_freelist.py',
    'create_hard_vs_soft_links.py',
    'create_inode_alloc.py',
    'create_linked_alloc.py',
    'create_mount_concept.py',
    'create_open_file_tables.py',
    'create_unix_permissions.py',
    'create_vfs.py',
    # 02-Grundlagen
    'create_dateisystem_abstraktion.py',
    'create_verzeichnis_evolution.py',
    # 01-Historie
    'create_chs_addressing.py',
    'create_hdd_aufbau_iso.py',
    'create_hdd_aufbau_with_sectors.py',
    'create_hdd_vs_ssd.py',
    'create_hdd_zugriffszeit.py',
    'create_ssd_architektur.py',
]

base_path = '/media/andhue/Wissen/open-lectures/tmp/'

for script in scripts:
    filepath = os.path.join(base_path, script)
    if not os.path.exists(filepath):
        print(f"Skipping {script} - not found")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Remove dark_background style (keep other imports intact)
    content = re.sub(r"plt\.style\.use\('dark_background'\)\n?", '', content)
    
    # 2. Make background transparent instead of using bg_color
    content = re.sub(r"fig\.patch\.set_facecolor\(bg_color\)", "fig.patch.set_facecolor('none')", content)
    content = re.sub(r"fig\.patch\.set_facecolor\('[^']+'\)", "fig.patch.set_facecolor('none')", content)
    content = re.sub(r"ax\.set_facecolor\(bg_color\)", "ax.set_facecolor('none')", content)
    content = re.sub(r"ax\.set_facecolor\('[^']+'\)", "ax.set_facecolor('none')", content)
    
    # 3. Update savefig to use transparent background
    content = re.sub(
        r"(plt\.savefig\([^)]+),\s*facecolor=bg_color",
        r"\1, transparent=True",
        content
    )
    content = re.sub(
        r"(plt\.savefig\([^)]+),\s*facecolor='[^']+'",
        r"\1, transparent=True",
        content
    )
    # If no facecolor specified, add transparent=True before bbox_inches
    if "transparent=True" not in content:
        content = re.sub(
            r"(plt\.savefig\([^)]+)(,\s*bbox_inches='tight'\))",
            r"\1, transparent=True\2",
            content
        )
    
    # 4. Replace dark box backgrounds with light ones
    content = re.sub(r"facecolor='#2D3748'", "facecolor='#E2E8F0'", content)
    content = re.sub(r"facecolor='#1D1D2E'", "facecolor='#EDF2F7'", content)
    content = re.sub(r"facecolor='#2D2424'", "facecolor='#FED7D7'", content)
    content = re.sub(r"facecolor='#2D3724'", "facecolor='#C6F6D5'", content)
    content = re.sub(r"facecolor='#22543D'", "facecolor='#C6F6D5'", content)
    content = re.sub(r"facecolor='#742A2A'", "facecolor='#FED7D7'", content)
    content = re.sub(r"facecolor='#553C9A'", "facecolor='#E9D8FD'", content)
    content = re.sub(r"facecolor='#276749'", "facecolor='#C6F6D5'", content)
    content = re.sub(r"facecolor='#1a202c'", "facecolor='#F7FAFC'", content)
    content = re.sub(r"facecolor=highlight_bg", "facecolor='#E2E8F0'", content)
    
    # 5. Replace light text colors (designed for dark bg) with darker ones
    content = re.sub(r"color='white'", "color='#1A202C'", content)
    content = re.sub(r"color='#FFFFFF'", "color='#1A202C'", content)
    content = re.sub(r"color='#A0AEC0'", "color='#4A5568'", content)
    content = re.sub(r"color='#E2E8F0'", "color='#4A5568'", content)
    content = re.sub(r"color='#CBD5E0'", "color='#4A5568'", content)
    content = re.sub(r"color='#9AE6B4'", "color='#276749'", content)
    content = re.sub(r"color='#B794F4'", "color='#553C9A'", content)
    content = re.sub(r"color='#FEB2B2'", "color='#9B2C2C'", content)
    content = re.sub(r"color='#FEEBC8'", "color='#C05621'", content)
    content = re.sub(r"color='#90CDF4'", "color='#2B6CB0'", content)
    content = re.sub(r"color='#81E6D9'", "color='#285E61'", content)
    content = re.sub(r"color='#FBD38D'", "color='#C05621'", content)
    
    # 6. Update text_color variable if defined
    content = re.sub(r"text_color\s*=\s*'#A0AEC0'", "text_color = '#4A5568'", content)
    content = re.sub(r"text_color\s*=\s*'#E2E8F0'", "text_color = '#4A5568'", content)
    content = re.sub(r"text_color\s*=\s*'#CBD5E0'", "text_color = '#4A5568'", content)
    
    # 7. Update highlight_bg for lighter theme
    content = re.sub(r"highlight_bg\s*=\s*'#2D3748'", "highlight_bg = '#E2E8F0'", content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Fixed {script}")

print("\nAll scripts fixed!")
