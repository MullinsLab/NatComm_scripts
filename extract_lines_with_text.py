import os
import shutil
import sys

def extract_files_with_text(search_text, input_directory='.'):
    try:
        # Define the name of the output folder
        output_folder = os.path.join(input_directory, f"extracted_{search_text}_files")
        
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Iterate through all files in the input directory
        for filename in os.listdir(input_directory):
            # Construct full file path
            file_path = os.path.join(input_directory, filename)
            
            # Check if it's a file and contains the search text in its name
            if os.path.isfile(file_path) and search_text in filename:
                # Move the file to the output folder
                shutil.move(file_path, os.path.join(output_folder, filename))
                print(f"Moved: {filename} -> {output_folder}")
        
        print(f"All matching files have been moved to '{output_folder}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a search text argument is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <search_text>")
        sys.exit(1)
    
    # Get the search text from command-line arguments
    search_text = sys.argv[1]
    
    # Call the function with default input directory (current directory)
    extract_files_with_text(search_text)
