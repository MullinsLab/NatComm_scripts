from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import os

def translate_alignment(input_file, output_file, table=1):
    """
    Translates nucleotide alignment to amino acid sequences while maintaining alignment.
    
    Args:
        input_file (str): Input FASTA file with nucleotide alignment
        output_file (str): Output FASTA file for amino acid alignment
        table (int): Genetic code table number (default: standard)
    """
    # Dictionary to store translated sequences
    translated_records = []
    
    for record in SeqIO.parse(input_file, "fasta"):
        # Convert gaps to N for translation, then restore alignment
        nucl_seq = str(record.seq).replace('-', 'N')
        
        # Split into codons while preserving frame
        codons = [nucl_seq[i:i+3] for i in range(0, len(nucl_seq), 3)]
        
        # Translate each codon, preserving gaps
        aa_seq = []
        for codon in codons:
            if len(codon) < 3:
                aa = ''  # Ignore incomplete codons
            else:
                aa = Seq(codon).translate(table=table, cds=False, gap='X')
                aa = aa.replace('*', 'X')  # Convert stops to X
            aa_seq.append(str(aa))
        
        # Create new record with translated sequence
        translated_record = SeqRecord(
            Seq(''.join(aa_seq)),
            id=record.id,
            description=f"Translated from {record.description}"
        )
        translated_records.append(translated_record)
    
    # Write translated alignment
    SeqIO.write(translated_records, output_file, "fasta")
    print(f"Translated alignment saved to {output_file}")

# Batch process all .fasta files in current directory
for f in os.listdir():
    if f.endswith(('.fasta', '.fa')):
        output_name = f"{os.path.splitext(f)[0]}_translated.fasta"
        translate_alignment(f, output_name)
