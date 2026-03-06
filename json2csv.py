#!/usr/bin/python

# Python program to convert JSON file from FUBAR program to CSV

import sys
import json
import csv

usage = "usage: python fubarjson2csv.py injasonfile"

if len(sys.argv) < 2:
    sys.exit(usage)

infile = sys.argv[1]
outfile = infile.replace(".json", ".csv")

# Opening JSON file and loading the data into the variable data
print(f"=== processing {infile} ===")
with open(infile, "r") as json_file:
	data = json.load(json_file)

header_data = data['MLE']['headers']
content_data = data['MLE']['content']['0']

# now we will open a file for writing
data_file = open(outfile, 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)
headers = []
headers.append('Site')
for header in header_data:
	h = header[0]
	headers.append(h)
csv_writer.writerow(headers)

count = 0
for cont in content_data:
    count += 1
    cont.insert(0, count)
    # Writing data of CSV file
    csv_writer.writerow(cont)

data_file.close()
