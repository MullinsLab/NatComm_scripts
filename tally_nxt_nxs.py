import os
import re

# Patterns: NXT and NXS, where X is any letter except P (case-insensitive)
pattern_nxt = re.compile(r'N[^Pp]T')
pattern_nxs = re.compile(r'N[^Pp]S')

output_filename = 'nxt_nxs_tally.txt'

with open(output_filename, 'w', encoding='utf-8') as output_file:
    output_file.write("Filename,NXT_Count,NXS_Count,Line_Count\n")
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename != output_filename:
            nxt_count = 0
            nxs_count = 0
            line_count = 0
            try:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    nxt_count = len(pattern_nxt.findall(content))
                    nxs_count = len(pattern_nxs.findall(content))
                    # Count lines
                    line_count = content.count('\n') + (1 if content and not content.endswith('\n') else 0)
            except Exception as e:
                # Optionally, log or print error
                pass
            output_file.write(f"{filename},{nxt_count},{nxs_count},{line_count}\n")

print(f"Results written to {output_filename}")
