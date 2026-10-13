#!/usr/bin/env python3
"""
Updates all journaling diagram scripts to use:
- Transparent background
- Theme-agnostic colors (work on both dark and light mode)
"""

import os
import re

# Theme-agnostic color palette
# These colors have good contrast on both dark and light backgrounds
NEW_COLORS = '''
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
'''

scripts = [
    # 04-Journaling (already updated but include for completeness)
    'create_journaling_prinzip.py',
    'create_journal_transaktion.py', 
    'create_metadata_journaling.py',
    'create_ordered_mode.py',
    'create_full_data_journaling.py',
    'create_crash_recovery.py',
    'create_ext4_journal.py',
    'create_cow.py',
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
    
    # 1. Remove dark_background style
    content = re.sub(r"plt\.style\.use\('dark_background'\)\n?", '', content)
    
    # 2. Replace bg_color usage
    content = re.sub(r"bg_color\s*=\s*'#[0-9a-fA-F]+'\n?", '', content)
    content = re.sub(r"fig\.patch\.set_facecolor\(bg_color\)", "fig.patch.set_facecolor('none')", content)
    content = re.sub(r"ax\.set_facecolor\(bg_color\)", "ax.set_facecolor('none')", content)
    
    # 3. Update savefig to use transparent background
    content = re.sub(
        r"(plt\.savefig\([^)]+),\s*facecolor=bg_color,",
        r"\1, transparent=True,",
        content
    )
    content = re.sub(
        r"(plt\.savefig\([^)]+)facecolor=bg_color([^)]*)\)",
        r"\1transparent=True\2)",
        content
    )
    
    # 4. Replace old color definitions with theme-agnostic ones
    # First, find where colors are defined (after imports, before figure setup)
    color_pattern = r"# Colors\n.*?(?=\nfig)"
    if re.search(color_pattern, content, re.DOTALL):
        content = re.sub(color_pattern, NEW_COLORS.strip() + '\n', content, flags=re.DOTALL)
    
    # 5. Update specific color values that might be hardcoded
    # Dark backgrounds for boxes -> light backgrounds
    content = re.sub(r"facecolor='#2D3748'", "facecolor='#E2E8F0'", content)
    content = re.sub(r"facecolor='#1D1D2E'", "facecolor='#EDF2F7'", content)
    content = re.sub(r"facecolor='#2D2424'", "facecolor='#FED7D7'", content)  # Danger bg
    content = re.sub(r"facecolor='#2D3724'", "facecolor='#C6F6D5'", content)  # Success bg
    content = re.sub(r"facecolor='#22543D'", "facecolor='#C6F6D5'", content)  # Green bg
    content = re.sub(r"facecolor='#742A2A'", "facecolor='#FED7D7'", content)  # Red bg
    content = re.sub(r"facecolor='#553C9A'", "facecolor='#E9D8FD'", content)  # Purple bg
    content = re.sub(r"facecolor='#276749'", "facecolor='#C6F6D5'", content)  # Green data bg
    
    # Update text colors for visibility on light background
    content = re.sub(r"color='white'", "color='#1A202C'", content)
    content = re.sub(r"color='#A0AEC0'", "color='#4A5568'", content)  # Light gray text -> medium gray
    content = re.sub(r"color='#9AE6B4'", "color='#276749'", content)  # Light green -> dark green
    content = re.sub(r"color='#B794F4'", "color='#553C9A'", content)  # Light purple -> dark purple
    content = re.sub(r"color='#FEB2B2'", "color='#9B2C2C'", content)  # Light red -> dark red
    content = re.sub(r"color='#FEEBC8'", "color='#C05621'", content)  # Light orange -> dark orange
    content = re.sub(r"color='#E2E8F0'", "color='#4A5568'", content)  # Very light gray -> medium
    
    # Update highlight_bg references
    content = re.sub(r"facecolor=highlight_bg", "facecolor='#E2E8F0'", content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Updated {script}")

print("\nAll scripts updated!")
