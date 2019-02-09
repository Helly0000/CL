import re
from tqdm import tqdm
import csv
import codecs
import hashlib

with codecs.open("4th.csv", "r", encoding="utf-8-sig") as csvFile:
    reader = csv.reader(csvFile)
    x = {}
    for item in reader:
#        if reader.line_num == 1:
#            continue
        x[item[0]] = item[-1]#x[原文MD5]=译文

newlines = []
md5 = hashlib.md5()
with codecs.open("Assembly-CSharp-NoHH.il", "r", encoding="utf-8-sig") as file:

    lines = file.readlines()
    i = 0
    for line in tqdm(lines):
        #pattern = r'\s+IL_[\s\S]+:\s+ldstr\s+"([\s\S]*)"'
        pattern = r'\s+IL_[\s\S]+:\s+ldstr\s+bytearray\s+([\s\S]*)'
        item = re.findall(pattern, line)
        if item:
            md5.update(item[0].encode('utf-8'))
            for s in x:
                if md5.hexdigest() == s and x[s]:
                    i += 1
                    #print(item[0], x[s])
                    #print('Before', line)
                    #line = line.replace(s, x[s], 1)
                    #print (line.find(r')'))
                    #print (line[line.find(r')'):])
                    line = line[:25]+"\""+x[s]+ "\"\r\n"+line[line.find(r')')+1:]
                    print('After', line)
        newlines.append(line)

    print(i)

with codecs.open("Assembly-CSharp-NoHH-B.il", "w", encoding="utf-8-sig") as file:
    for newline in newlines:
        file.write(newline)
