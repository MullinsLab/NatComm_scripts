import glob
import os

def fasta_to_tab(input_fasta, output_tab):
    with open(input_fasta, 'r') as infile, open(output_tab, 'w') as outfile:
        outfile.write("ID\tSequence\n")
        seq_id = None
        seq_lines = []
        for line in infile:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if seq_id is not None:
                    outfile.write(f"{seq_id}\t{''.join(seq_lines)}\n")
                seq_id = line[1:].split()[0]
                seq_lines = []
            else:
                seq_lines.append(line)
        if seq_id is not None:
            outfile.write(f"{seq_id}\t{''.join(seq_lines)}\n")

def process_directory(directory):
    fasta_files = glob.glob(os.path.join(directory, '*.fasta')) + glob.glob(os.path.join(directory, '*.fa'))
    if not fasta_files:
        print("No FASTA files found in the specified directory.")
        return
    for fasta_file in fasta_files:
        base = os.path.splitext(os.path.basename(fasta_file))[0]
        output_file = os.path.join(directory, base + '.tsv')
        fasta_to_tab(fasta_file, output_file)
        print(f"Converted {fasta_file} to {output_file}")

if __name__ == "__main__":
    directory = input("Enter the path to the directory containing FASTA files: ").strip()
    if not os.path.isdir(directory):
        print("The specified path is not a valid directory.")
    else:
        process_directory(directory)
