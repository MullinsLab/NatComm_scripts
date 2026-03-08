from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def translate_nucleotide_to_protein(nucleotide_sequence):
    """Translate a nucleotide sequence to a protein (amino acid) sequence."""
    return nucleotide_sequence.translate()  # Automatically handles stop codons

def process_alignment(input_file, output_file):
    """Read a nucleotide alignment from a file and write a translated amino acid alignment."""
    
    # Read in nucleotide sequences from input file (FASTA format)
    nucleotide_records = list(SeqIO.parse(input_file, "fasta"))
    
    # Create a list to store the translated sequences
    protein_records = []
    
    # Process each nucleotide sequence
    for record in nucleotide_records:
        print(f"Translating sequence {record.id}...")
        
        # Translate nucleotide sequence to protein (amino acid sequence)
        protein_seq = translate_nucleotide_to_protein(record.seq)
        
        # Create a new SeqRecord for the protein sequence
        protein_record = SeqRecord(protein_seq, id=record.id, description="Translated")
        
        # Add to the list of protein records
        protein_records.append(protein_record)
    
    # Write the translated sequences to output file in FASTA format
    SeqIO.write(protein_records, output_file, "fasta")
    print(f"Protein sequences written to {output_file}")

def batch_translate(input_folder, output_folder):
    """Batch process nucleotide alignments in a folder."""
    from os import listdir
    from os.path import join, isfile

    # Get all nucleotide alignment files in the input folder
    files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    
    for file in files:
        if file.endswith(".fasta"):
            input_path = join(input_folder, file)
            output_path = join(output_folder, file.replace(".fasta", "_translated.fasta"))
            print(f"Processing file: {input_path}")
            process_alignment(input_path, output_path)

if __name__ == "__main__":
    # Example usage: Provide the folder paths where the input and output files are located
    input_folder = "nucleotide_alignments"  # Folder containing nucleotide FASTA files
    output_folder = "amino_acid_alignments"  # Folder to save translated FASTA files
    
    # Batch process nucleotide alignments
    batch_translate(input_folder, output_folder)
