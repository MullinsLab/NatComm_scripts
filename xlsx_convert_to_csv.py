import pandas as pd
import os

# Use current directory (where script is located)
directory = os.getcwd()

# Loop through all files in current directory
for filename in os.listdir(directory):
    if filename.endswith(".xlsx"):
        # Read Excel file
        xlsx_path = os.path.join(directory, filename)
        df = pd.read_excel(xlsx_path)
        
        # Create new filename with .csv extension
        csv_path = os.path.join(directory, filename[:-5] + ".csv")
        
        # Write to CSV
        df.to_csv(csv_path, index=False)
        print(f"Converted {filename} to CSV")