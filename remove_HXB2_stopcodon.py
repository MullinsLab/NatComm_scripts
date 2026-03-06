#!/usr/bin/python

import sys
import re

usage = "usage: python remove_HXB2-stopcodon.py infastfile"

if len(sys.argv) < 2:
    sys.exit(usage)

infile = sys.argv[1]

outfile = infile.replace(".fasta", "_rmHXB2-stopcodon.fasta")
nameSeq, nameStatus = {}, {}
count, removecount, remaincount, trimnts = 0, 0, 0 ,0
refname, refseq = '', ''
names = []
print("=== processing "+infile+" ===")
with open(infile, "r") as ifp:
    
        for line in ifp:
            line = line.strip()
            if line.startswith('>'):
                count += 1
                name = line[1:]
                if re.search('HXB2', name):
                    refname = name              
                else:
                    names.append(name)
                if name not in nameStatus:
                    nameSeq[name] = ''
                else:
                    sys.exit(f"Duplicate sequence name: {name}")
            else:
                nameSeq[name] += line

refseq = nameSeq[refname]
alignlen = len(refseq)
lastcodon = refseq[alignlen - 3:]
if lastcodon in ['TAA', 'TAG', 'TGA']:
    trimnts = 3
else:
    sys.exit(f"last codon {lastcodon} is not stop codon in {infile}")

with open(outfile, "w") as ofp:
    for name in names:
        remaincount += 1
        seq = nameSeq[name]
        if len(seq) != alignlen:
            sys.exit(f"align length not same for {name}: {len(seq)} vs {alignlen}")
        remainseq = seq[:alignlen-trimnts]
        ofp.write(f">{name}\n{remainseq}\n")

print("total "+str(count)+" sequences, keep "+str(remaincount)+" sequences.\n")
