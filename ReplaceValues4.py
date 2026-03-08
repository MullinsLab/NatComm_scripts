import pandas as pd

def replace_values_in_csv_pandas(input_file, output_file, min_val, max_val, replacement_value):
    df = pd.read_csv(input_file)
    print("Data types before replacement:")
    print(df.dtypes)
    print("\nSample data before replacement:")
    print(df.head())
    # Convert columns to numeric if possible to ensure comparisons work
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')
        
    for col in df.select_dtypes(include=['number']).columns:
        condition = (df[col] >= min_val) & (df[col] <= max_val)
        print(f"\nValues in column '{col}' to replace based on condition:")
        print(df.loc[condition, col])
        df.loc[condition, col] = replacement_value
        
    print("\nSample data after replacement:")
    print(df.head())
    df.to_csv(output_file, index=False)
    print(f"\nReplacement complete. Saved to {output_file}")

# Example usage - adjust inputs accordingly
replace_values_in_csv_pandas(
    input_file="input.csv",
    output_file="output.csv",
    min_val=0.001,
    max_val=0.99999,
    replacement_value=1
)
