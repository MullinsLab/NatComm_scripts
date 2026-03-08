#!/usr/bin/env python3
"""
Parse TSV file and remove '0' if it's the only non-blank value in a row.
"""

import sys

def process_tsv(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        # Split by tab
        columns = line.rstrip('\n').split('\t')

        # Find non-blank values
        non_blank_values = [col for col in columns if col.strip() != '']

        # If there's exactly one non-blank value and it's "0", replace it with blank
        if len(non_blank_values) == 1 and non_blank_values[0] == '0':
            # Find the index of "0" and replace it
            columns = ['' if col == '0' else col for col in columns]

        # Join back with tabs
        processed_lines.append('\t'.join(columns) + '\n')

    # Write to output file
    with open(output_file, 'w') as f:
        f.writelines(processed_lines)

    print(f"Processed {len(lines)} rows")
    print(f"Output written to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_shannon_entropy_tsv.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_tsv(input_file, output_file)
