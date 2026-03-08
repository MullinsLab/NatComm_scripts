#!/usr/bin/python
# In a directory holding all input .csv files, run the command:
# "for file in *.csv; do python3 add_filename_to_csv_header.py $file; done"
#It will output .csv files with the name of _filename.csv in the same directory.

import sys
import re

usage = "usage: python add_filename_to_header.py incsvfile"

if len(sys.argv) < 2:
    sys.exit(usage)

infile = sys.argv[1]

outfile = infile.replace(".csv", "_filename.csv")
removenamestatus = {}
count, removecount, remaincount, flag = 0, 0, 0 ,0
print("=== processing "+infile+" ===")
filename = infile.split('/')[-1]
with open(infile, "r") as ifp:
    with open(outfile, "w") as ofp:
        for line in ifp:
            line = line.strip()
            if line:
                count += 1
                if count == 1:  # headers
                    headers = line.split(',')
                    newheaders = []
                    for header in headers:
                        newheaders.append(header+"_"+filename)
                    ofp.write(','.join(newheaders)+"\n")
                else:
                    ofp.write(f"{line}\n")

