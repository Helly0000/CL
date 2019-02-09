import re
from tqdm import tqdm
import csv
import codecs

with codecs.open("replace.csv", "r", encoding="utf-8-sig") as csvFile:
    reader = csv.reader(csvFile)
    x = {}
    for item in reader:
        if reader.line_num == 1:
            continue
        x[item[0]] = item[1].strip('\n')

newlines = []
with codecs.open("extract.il", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()
    i = 0
    for item in tqdm(lines):
        CNitem = ''
        item = item.strip('\n')
        for s in x:
            if item == s:
                i += 1
                print('Before', item)
                CNitem = x[s]
                print('After', CNitem)
        newlines.append((item, CNitem))

    print(i)

with codecs.open("extract-x.csv", "w", encoding="utf-8-sig") as file:
    f_csv = csv.writer(file)
    f_csv.writerow(['原文', '翻译'])
    f_csv.writerows(newlines)