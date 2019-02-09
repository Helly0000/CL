import re
from tqdm import tqdm
import csv
import codecs

newlines = []
with codecs.open("Assembly-CSharp-NoHH.il", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()
    i = 0
    for line in tqdm(lines):
        item = re.findall(r'\s+IL_[\s\S]+:\s+ldstr\s+"([\s\S]*)"', line)
        if(item):
            if re.match(r'[A-Za-z0-9-/.?,()%: \'\"\\<>]+$', item[0]):
                newlines.append(item[0])

    print(i)

with codecs.open("extract.il", "w", encoding="utf-8-sig") as file:
    for newline in newlines:
        file.write(newline + "\n")
