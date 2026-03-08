import sys
import os
import string

def sanitize_filename(s):
    """
    Convert the search string into a safe filename by:
    - Removing characters not allowed in filenames.
    - Replacing spaces with underscores.
    - Defaulting to 'output.txt' if the result is empty.
    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    cleaned = ''.join(c for c in s if c in valid_chars)
    cleaned = cleaned.replace(' ', '_')
    if not cleaned:
        cleaned = "output"
    return cleaned + ".txt"

def extract_lines_to_file(input_filename, search_string):
    output_filename = sanitize_filename(search_string)
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
             open(output_filename, 'w', encoding='utf-8') as outfile:
            matched_lines = 0
            for line in infile:
                if search_string in line:
                    outfile.write(line)
                    matched_lines += 1

        if matched_lines == 0:
            print(f"No lines containing '{search_string}' found in '{input_filename}'.")
        else:
            print(f"Extracted {matched_lines} lines containing '{search_string}' to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <filename> <search_string>")
        sys.exit(1)

    input_filename = sys.argv[1]
    search_string = sys.argv[2]

    if not os.path.isfile(input_filename):
        print(f"Error: File '{input_filename}' does not exist in the current directory.")
        sys.exit(1)

    extract_lines_to_file(input_filename, search_string)
