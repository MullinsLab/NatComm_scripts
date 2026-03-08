import os
import csv

def change_headers_in_tsv(input_folder, output_folder, new_headers):
    """
    Replace headers in all TSV files within a folder.

    Parameters:
        input_folder (str): Path to the folder containing input TSV files.
        output_folder (str): Path to the folder to save output TSV files.
        new_headers (list): List of new header names.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each TSV file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".tsv"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)

            with open(input_file, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter='\t')
                rows = list(reader)

            # Replace the headers with the new ones
            rows[0] = new_headers

            # Write the modified data to the output file
            with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                writer = csv.writer(outfile, delimiter='\t')
                writer.writerows(rows)

    print(f"Headers updated in all files. Modified files saved in '{output_folder}'.")

# Example usage:
if __name__ == "__main__":
    input_folder = "path/to/input/folder"  # Folder containing input TSV files
    output_folder = "path/to/output/folder"  # Folder to save output TSV files
    new_headers = ["Column1", "Column2", "Column3", "Column4"]  # Replace with your desired headers
    
    change_headers_in_tsv(input_folder, output_folder, new_headers)
