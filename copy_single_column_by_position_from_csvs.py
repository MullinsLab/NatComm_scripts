import os
import pandas as pd

def copy_single_column_by_position_from_csvs(column_position, output_file):
    """
    Copies a single column (by position) from all .csv files in the current directory 
    and combines them into one output file.

    Args:
        column_position (int): The index (0-based) of the column to extract.
        output_file (str): Name of the output .csv file.
    """
    # Create an empty DataFrame to store combined data
    combined_data = pd.DataFrame()

    # Get list of all files in the current directory
    files = os.listdir()

    # Loop through each file in the directory
    for file in files:
        # Process only .csv files
        if file.endswith('.csv'):
            try:
                # Read the CSV file
                df = pd.read_csv(file)

                # Select the single column by its index position using .iloc
                selected_data = df.iloc[:, [column_position]]  # Use [column_position] for DataFrame format

                # Append to the combined DataFrame
                combined_data = pd.concat([combined_data, selected_data], ignore_index=True)
                print(f"Processed: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")

    # Save the combined data to the output file
    combined_data.to_csv(output_file, index=False)
    print(f"Combined data saved to {output_file}")

# Example usage
column_position = 2  # Replace with your desired column index (0-based)
output_file = 'combined_output.csv'  # Replace with your desired output filename
copy_single_column_by_position_from_csvs(column_position, output_file)
