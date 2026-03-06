#!/usr/bin/python3

import sys, os, re
import glob
import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="directory to hold input sequence fasta file", nargs="?", const=1, type=str, default=".")
    args = parser.parse_args()
    dir = args.dir

    files = []
    for file in glob.glob(os.path.join(dir, '*.fasta')):
        files.append(file)
    files.sort()

    for file in files:
        nwkfile = file + ".nwk"
        if os.path.isfile(nwkfile):
            fubarfile = file + ".FUBAR.json"
            if os.path.isfile(fubarfile):
                print(f"= skip {file} =")
            else:
                print(f"= processing {file} =")
                subprocess.run(["hyphy", "fubar", file, nwkfile])
        else:
            sys.exit(f"No newick tree for {file}")

