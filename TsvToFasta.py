import os
import glob

def tab_to_fasta(input_tsv, output_fasta):
    with open(input_tsv, 'r') as infile, open(output_fasta, 'w') as outfile:
        first_line = infile.readline()
        # Check if header is present
        has_header = first_line.lower().startswith('id\t') or first_line.lower().startswith('id,')
        if not has_header:
            infile.seek(0)  # No header, rewind
        for line in infile:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            seq_id, sequence = parts[0], parts[1]
            outfile.write(f">{seq_id}\n")
            # Optionally wrap sequence lines to 60 chars (FASTA standard)
            for i in range(0, len(sequence), 60):
                outfile.write(sequence[i:i+60] + '\n')

def process_directory():
