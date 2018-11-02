#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: {0} file1 [file2 [...filen]]".format(sys.argv[0]))
        sys.exit()

        
print("{0} file{1}".format((count if count != 0 else "No"),
                            ("s" if count != 1 else "")))

