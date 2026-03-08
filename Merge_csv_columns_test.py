import csv
import os

def merge_columns(env, output, 2, separator=",", new_column_name="Merged"):
    """
    Merge specified columns in a CSV file into a single column.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the output CSV file.
        columns_to_merge (list): List of column indices to merge (0-based).
        separator (str): String to separate the merged values. Default is a space.
        new_column_name (str): Name of the new merged column.
    """
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        headers = next(reader)

        # Create a new list of headers, replacing the merged columns with the new column name
        new_headers = [col for idx, col in enumerate(headers) if idx not in columns_to_merge]
        new_headers.append(new_column_name)

        rows = []
        for row in reader:
            merged_value = separator.join(row[idx] for idx in columns_to_merge)
            new_row = [val for idx, val in enumerate(row) if idx not in columns_to_merge]
            new_row.append(merged_value)
            rows.append(new_row)

    # Write the modified data to the output file
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(new_headers)
        writer.writerows(rows)

# Example usage:
if __name__ == "__main__":
    input_csv = "env.csv"
    output_csv = "output.csv"
    columns = [0, 1]  # Indices of columns to merge (e.g., merge the first two columns)
    merge_columns(input_csv, output_csv, columns, separator=", ", new_column_name="MergedColumn")
    print(f"Merged columns saved to {output_csv}")
