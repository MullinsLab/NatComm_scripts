import csv
import reprlib

with open('file_with_blanks.tsv', 'r', encoding='utf-8', newline='') as blanks_f:
    reader = csv.reader(blanks_f, delimiter='\t')
    for idx, row in enumerate(reader, 1):
        if all(cell.strip() == '' for cell in row):
            print(f"Row {idx}: BLANK as detected ({len(row)} columns)")
        else:
            # Print the real content for debugging
            print(f"Row {idx}: NOT BLANK -> {reprlib.repr(row)}")
