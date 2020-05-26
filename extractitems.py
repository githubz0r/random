#!/usr/bin/python3

## extracting items from a warcraftlogs file saved somehow through the website ##
import re
import sys

file_name = sys.argv[1]
items = []
with open(file_name) as input:
    lines = input.readlines()
    for line in lines:
        line = line.strip()
        match_obj = re.match("\<span\>(.+?)\<\/span\>", line)
        if match_obj:
            item = match_obj.group(1)
            items.append(item)

with open("items.txt","w") as output:
    for item in items:
        output.write("%s\n" %item)
