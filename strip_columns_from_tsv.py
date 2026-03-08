import os
import csv

def strip_columns_from_tsv(input_folder, output_folder, columns_to_strip):
    """
    Remove specific columns from all TSV files in a folder.

    Parameters:
        input_folder (str): Path to the folder containing input TSV files.
        output_folder (str): Path to the folder to save output TSV files.
        columns_to_strip (list): List of column indices to remove (0-based indexing).
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each TSV file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".tsv"):  # Only process .tsv files
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)

            with open(input_file, 'r', encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter='\t')
                rows = list(reader)

            # Remove the specified columns from each row
            stripped_rows = [
                [value for idx, value in enumerate(row) if idx not in columns_to_strip]
                for row in rows
            ]

            # Write the modified data to the output file
            with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                writer = csv.writer(outfile, delimiter='\t')
                writer.writerows(stripped_rows)

    print(f"Specified columns stripped from all files. Modified files saved in '{output_folder}'.")

# MAIN FUNCTION
if __name__ == "__main__":
    # 1. Path to folder containing the input .tsv files
    input_folder = "input_folder"  # Replace with the folder containing your .tsv files

    # 2. Path to folder where modified .tsv files will be saved
    output_folder = "output_folder"  # Replace with your desired output folder

    # 3. Columns to strip (0-based indices)
    # To remove columns 1-7 (inclusive), use range(0, 7), which generates [0, 1, 2, 3, 4, 5, 6]
    # range(7, 9) produces [7, 8], which includes both columns 7 and 8 (0-based indexing).
	# range(7, 8) produces [7], which includes only column 7, excluding column 8.
    columns_to_strip = list(range(7, 9))  # Update this as needed

    # Call the function
    strip_columns_from_tsv(input_folder, output_folder, columns_to_strip)
