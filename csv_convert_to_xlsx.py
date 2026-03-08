import pandas as pd
import os

# Use current directory (where script is located)
directory = os.getcwd()  # Gets current working directory

# Loop through all files in current directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Read CSV file
        csv_path = os.path.join(directory, filename)
        df = pd.read_csv(csv_path)
        
        # Create new filename with .xlsx extension
        xlsx_path = os.path.join(directory, filename[:-4] + ".xlsx")
        
        # Write to Excel
        df.to_excel(xlsx_path, index=False)
        print(f"Converted {filename} to Excel")