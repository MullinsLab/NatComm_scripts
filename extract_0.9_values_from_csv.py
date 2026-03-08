import csv
import argparse

def extract_values_from_csv(input_file, output_file="extracted_values.csv", threshold=0.9):
    extracted_data = []

    # Read the input CSV file
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Extract headers
        next(reader)  # Skip the first data row (row 1)
        rows = list(reader)  # Extract remaining rows

        # Iterate through rows and columns to find values >= threshold
        for row_index, row in enumerate(rows, start=2):  # Start row index at 2 (data starts after row 1)
            for col_index, value in enumerate(row):
                try:
                    numeric_value = float(value)  # Convert value to float
                    if numeric_value >= threshold:
                        extracted_data.append([
                            row_index,  # Row number in the file
                            headers[col_index],  # Column header
                            numeric_value  # The value itself
                        ])
                except ValueError:
                    # Skip non-numeric values
                    pass

    # Write the extracted data to an output file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Row Number", "Column Header", "Value"])  # Write headers for extracted data
        writer.writerows(extracted_data)

    print(f"Extracted {len(extracted_data)} values >= {threshold} from {input_file}.")
    print(f"Results saved to {output_file}.")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Extract values >= threshold from a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("--output_file", default="extracted_values.csv", help="Path to the output CSV file (default: extracted_values.csv)")
    parser.add_argument("--threshold", type=float, default=0.9, help="Threshold value for extraction (default: 0.9)")

    args = parser.parse_args()

    # Call the function with command-line arguments
    extract_values_from_csv(args.input_file, args.output_file, args.threshold)
