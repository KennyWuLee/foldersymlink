#!/usr/bin/env python

import sys
import os

if len(sys.argv) != 3:
    print("usage: symlink.py target pattern")
    sys.exit(1)

targetdir = os.path.normpath(sys.argv[1])
pattern = sys.argv[2]

if not os.path.isdir(targetdir):
    print("invalid target (must be directory)")
    sys.exit(1)

if pattern.count("%") != 1:
    print("invalid pattern (must contain %d once)")
    sys.exit(1)

files = []
for f in os.listdir(targetdir):
    files.append(os.path.relpath(targetdir + '/' + f))

files.sort()

i = 1
for f in files:
    target = f
    linkname = pattern % i
    os.symlink(target, linkname) 
    i += 1


