import os
import pandas as pd

def convert_csv_to_tsv_in_batch():
    """
    Converts all .csv files in the current directory to .tsv files
    and removes the original .csv files after conversion.
    """
    # Get list of all files in the current directory
    files = os.listdir()
    
    # Loop through each file in the directory
    for file in files:
        # Check if the file has a .csv extension
        if file.endswith('.csv'):
            # Create a corresponding .tsv filename
            tsv_file = file.replace('.csv', '.tsv')
            
            try:
                # Read the CSV file using pandas
                df = pd.read_csv(file)
                
                # Write the DataFrame to a TSV file
                df.to_csv(tsv_file, sep='\t', index=False)
                
                # Remove the original CSV file
                os.remove(file)
                
                print(f"Converted {file} to {tsv_file} and removed the original .csv file.")
            except Exception as e:
                print(f"Error processing {file}: {e}")

# Run the function
convert_csv_to_tsv_in_batch()
