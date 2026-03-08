import pandas as pd
import glob

# List all .csv files
csv_files = glob.glob('*.FUBAR_filename.csv')

# Initialize an empty list to store the DataFrames of the extracted columns
extracted_columns = []

# Loop through each file, read it, and extract the desired column
for file in csv_files:
    # Read the .tsv file into a pandas DataFrame
    df = pd.read_csv(file, usecols=range(7), header=None)
    
    # Extract the desired column (adjust the index as needed)
    extracted_columns.append(df.iloc[:, 2])  # 1 for second column

# Concatenate the extracted columns side by side (as separate columns)
merged_df = pd.concat(extracted_columns, axis=1)

# Save the merged columns to a new file (as a .csv)
merged_df.to_csv('merged_columns_higherBeta.tsv', index=False, header=False)

