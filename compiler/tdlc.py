#!/usr/bin/env python

import sys
import os
import json

def compile(programFile):
    print("compiling " + programFile)
    with open(programFile) as f:
        tdl = f.read()
        print(tdl)

if __name__ == "__main__":
    compile(sys.argv[1])
