import re
from tqdm import tqdm
import csv
import codecs

newlines = []
with codecs.open("Assembly-CSharp.il", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()
    i = 0
    for line in tqdm(lines):
        item = re.findall(r'\s+IL_[\s\S]+:\s+ldstr\s+"([\s\S]*)"', line)
        if(item):
            if re.match(r'[A-Za-z0-9-/.?,()%:\'\"\\<>!]+ [A-Za-z0-9-/.?,()%:\'\"\\<>!]+ [A-Za-z0-9-/.?,()%: \'\"\\<>!]+$', item[0]):
                if ('!' in item[0]):
                    newlines.append([item[0]])

    print(i)

with codecs.open("extract-x.csv", "w", encoding="utf-8-sig") as file:
    f_csv = csv.writer(file)
    f_csv.writerow(['原文', '翻译'])
    f_csv.writerows(newlines)
