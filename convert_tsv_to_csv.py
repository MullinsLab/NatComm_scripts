import os
import csv

def convert_tsv_to_csv():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all .tsv files in the current directory
    tsv_files = [f for f in os.listdir(current_directory) if f.endswith('.tsv')]

    # Loop through each .tsv file and convert it to .csv
    for tsv_file in tsv_files:
        tsv_path = os.path.join(current_directory, tsv_file)
        csv_file = tsv_file.replace('.tsv', '.csv')
        csv_path = os.path.join(current_directory, csv_file)

        # Read the .tsv file and write to a .csv file
        with open(tsv_path, 'r', newline='', encoding='utf-8') as tsv_in, \
             open(csv_path, 'w', newline='', encoding='utf-8') as csv_out:
            tsv_reader = csv.reader(tsv_in, delimiter='\t')
            csv_writer = csv.writer(csv_out)

            for row in tsv_reader:
                csv_writer.writerow(row)

        print(f"Converted: {tsv_file} -> {csv_file}")

# Call the function to convert all .tsv files to .csv in the current directory
convert_tsv_to_csv()
