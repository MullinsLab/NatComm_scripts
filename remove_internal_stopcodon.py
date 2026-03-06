#!/usr/bin/python

# for the intact gene, the script searches the stop codon that is before the regular 
# stop codon, changes it to "---"

import sys
import re

usage = "usage: python remove_internal_stopcodon.py infastfile"

if len(sys.argv) < 2:
    sys.exit(usage)

infile = sys.argv[1]

outfile = infile.replace(".fasta", "_rm_internal_stopcodon.fasta")
nameSeq, nameStatus = {}, {}
count, remaincount = 0, 0
refname, refseq = '', ''
names = []
print("=== processing "+infile+" ===")
with open(infile, "r") as ifp:   
    for line in ifp:
        line = line.strip()
        if line.startswith('>'):
            count += 1
            name = line[1:]
            names.append(name)
            if name not in nameStatus:
                nameSeq[name] = ''
            else:
                sys.exit(f"Duplicate sequence name: {name}")
        else:
            nameSeq[name] += line

alignlen = len(nameSeq[names[0]])

with open(outfile, "w") as ofp:
    flag = 0
    for name in names:
        remaincount += 1
        seq = nameSeq[name]
        nts = list(seq)
        stopcodonflag = 0
        if len(seq) != alignlen:
            sys.exit(f"align length not same for {name}: {len(seq)} vs {alignlen}")
        for i in range(0, alignlen, 3):
            if stopcodonflag == 1:
                nts[i], nts[i+1], nts[i+2] = '-', '-', '-'
            else:
                codon = nts[i] + nts[i+1] + nts[i+2]
                if codon in ["TAA", "TAG", "TGA"]:
                    nts[i], nts[i+1], nts[i+2] = '-', '-', '-'
                    print(f"sequence {name}: internal stop codon at {i}")
                    flag = 1
                    stopcodonflag = 1
        ofp.write(f">{name}\n")
        ofp.write(''.join(nts)+"\n")
    if flag == 0:
        print("No internal stop codon")
    
print(f"total {count} sequences, checked {remaincount} sequences.\n")
