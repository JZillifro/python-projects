import sys
import os

query = sys.argv[1]
path = sys.argv[2]

if os.path.isabs(path):
    directory = path
else:
   directory = os.getcwd() + "\\" + path

for (root, dirs, files) in os.walk(directory):
    for file in files:
        location = root + "\\" + file
        text = open(location, "r").read()
        linenum = 1
        for line in text.split("\n"):
            if query in line:
                print(location, linenum, "\t", line.strip())
            linenum += 1