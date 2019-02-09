import re
from tqdm import tqdm
import csv
import codecs

with codecs.open("jingjian.csv", "r", encoding="utf-8-sig") as csvFile:
    reader = csv.reader(csvFile)
    x = {}
    for item in reader:
#        if reader.line_num == 1:
#            continue
        x[item[1]] = item[-1]

newlines = []
with codecs.open("Assembly-CSharp-NoHH-B.il", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()
    i = 0
    for line in tqdm(lines):
        pattern = r'\s+IL_[\s\S]+:\s+ldstr\s+"([\s\S]*)"'
        item = re.findall(pattern, line)
        if item:
            for s in x:
                if item[0] == s and x[s]:
                    i += 1
                    #print(item[0], x[s])
                    #print('Before', line)
                    line = line.replace(s, x[s], 1)
                    #print('After', line)
        newlines.append(line)
        

    print(i)


with codecs.open("Assembly-CSharp.il", "w", encoding="utf-8-sig") as file:
    for newline in newlines:
        file.write(newline)
