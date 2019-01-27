#!/usr/bin/env python

import os
import json

def compile():
    print("compiling...")


# TODO: break this out into a separate script inside tests folder which invokes compiler, don't have the complier test itself.
def test():
    print("Running test suite")
    for test in os.listdir("tests"):
        print('Running test: ' + test)
        with open("tests/" + test + "/program.tdl") as f:
            tdl = f.read()
            print("Testing program:")
            print(tdl)
            with open("tests/" + test + "/expectation.json") as j:
                print("evaluating against expectation:")
                expectation = json.loads(j.read())
                print(json.dumps(expectation))



test()
