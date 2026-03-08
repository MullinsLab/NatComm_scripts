import csv

def is_blank_row(row):
    # True if every cell in row is an empty string or just whitespace
    return all(cell.strip() == '' for cell in row)

with open('file_with_blanks.tsv', 'r', encoding='utf-8', newline='') as blanks_f, \
     open('file_with_zeros.tsv', 'r', encoding='utf-8', newline='') as zeros_f, \
     open('zeros_replaced_with_blanks.tsv', 'w', encoding='utf-8', newline='') as out_f:

    reader_blanks = csv.reader(blanks_f, delimiter='\t')
    reader_zeros = csv.reader(zeros_f, delimiter='\t')
    writer = csv.writer(out_f, delimiter='\t')

    for blank_row, zero_row in zip(reader_blanks, reader_zeros):
        if is_blank_row(blank_row):
            writer.writerow([''] * len(zero_row))  # Write blank row with correct columns
        else:
            writer.writerow(zero_row)
