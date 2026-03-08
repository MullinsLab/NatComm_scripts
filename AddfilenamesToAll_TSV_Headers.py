import os
import csv
from pathlib import Path

def modify_headers_and_remove_original():
    # Get directory where the script is located
    script_dir = Path(__file__).resolve().parent
    
    # Process all .tsv files in the script's directory
    for tsv_file in script_dir.glob('*.tsv'):
        with open(tsv_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile, delimiter='\t')
            headers = next(reader)
            rows = list(reader)
            
            # Get filename without extension
            file_stem = tsv_file.stem
            
            # Add filename to each header
            modified_headers = [f"{header}_{file_stem}" for header in headers]
        
        # Create output filename with '_modified' suffix
        output_file = tsv_file.with_name(f"{tsv_file.stem}_modified.tsv")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, delimiter='\t')
            writer.writerow(modified_headers)
            writer.writerows(rows)
            
        print(f"Processed: {tsv_file.name} -> {output_file.name}")
        
        # Remove the original file
        try:
            tsv_file.unlink()  # Deletes the original file
            print(f"Deleted original file: {tsv_file.name}")
        except Exception as e:
            print(f"Error deleting {tsv_file.name}: {e}")

if __name__ == "__main__":
    modify_headers_and_remove_original()
