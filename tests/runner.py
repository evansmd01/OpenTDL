#!/usr/bin/env python

import os
import json

def test():
    cwd = os.path.dirname(os.path.realpath(__file__))
    print("Running test suite")
    for test in os.listdir(cwd):
        if test == "runner.py":
            continue
        print('Running test: ' + test)
        with open(cwd + "/" + test + "/program.tdl") as f:
            tdl = f.read()
            print("Testing program:")
            print(tdl)
            with open(cwd + "/" + test + "/expectation.json") as j:
                print("evaluating against expectation:")
                expectation = json.loads(j.read())
                print(json.dumps(expectation))

test()
