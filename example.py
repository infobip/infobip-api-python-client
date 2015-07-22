#!/usr/bin/env python
__author__ = 'nmaric'

import sys
import os
import glob

myfolder = os.path.dirname(__file__)

if sys.argv.__len__() < 2:
    print 'Please choose example to run:'
    files = glob.glob("examples/*.py")
    for file in files:
        if not file.startswith("examples/__"):
            print "* " + file.split("/")[1].rstrip(".py")
    print
    exit(1)

sys.path.append(myfolder)
example = __import__("examples", globals(), locals(), [sys.argv[1]])
