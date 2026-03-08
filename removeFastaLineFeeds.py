import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all line feeds
    content = content.replace('\r', '').replace('\n', '')

    # Insert a line feed after the word 'translated' (case-insensitive)
    content = re.sub(r'(translated)', r'\1\n', content, flags=re.IGNORECASE)

    # Insert a line feed before every '>'
    content = re.sub(r'>', r'\n>', content)

    # Remove possible double line feeds (optional)
    content = re.sub(r'\n+', r'\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    directory = input("Enter the path to the folder you want to process: ").strip()
    if not os.path.isdir(directory):
        print("Invalid directory. Exiting.")
        return

    script_path = os.path.abspath(__file__)

    for entry in os.scandir(directory):  # Efficiently iterate over files[2][5][6]
        if entry.is_file():
            # Skip processing the script itself if it is in the same folder
            if os.path.abspath(entry.path) == script_path:
                continue
            process_file(entry.path)
            print(f"Processed: {entry.name}")

if __name__ == "__main__":
    main()
