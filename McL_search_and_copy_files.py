import os
import shutil

def search_and_copy_files(search_string, destination_folder):
    """
    Search for files in the current directory containing a specific string in their filenames
    and copy them to a separate folder.

    Args:
        search_string (str): The string to search for in filenames.
        destination_folder (str): The folder where matching files will be copied.
    """
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get list of all files in the current directory
    files = os.listdir()

    # Loop through each file in the directory
    for file in files:
        # Check if the file contains the search string and is a file (not a directory)
        if search_string in file and os.path.isfile(file):
            # Copy the file to the destination folder
            shutil.copy(file, destination_folder)
            print(f"Copied: {file} to {destination_folder}")

# Example usage
search_string = "McL"  # Replace with your desired search string
destination_folder = "McL"  # Replace with your desired destination folder name
search_and_copy_files(search_string, destination_folder)
