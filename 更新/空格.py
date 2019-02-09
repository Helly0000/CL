import re
from tqdm import tqdm
import csv
import codecs
newlines = []
with codecs.open("jingjian.csv", "r", encoding="utf-8-sig") as csvFile:
    reader = csv.reader(csvFile)
    for item in reader:
        try:
            item[2] = ' '.join(item[2])
            print (item[2])
            newlines.append([item[0],item[1],item[2]])
        except: 
            newlines.append([item[0],item[1]])



with codecs.open("5.csv", "w", encoding="utf-8-sig") as file:
    f_csv = csv.writer(file)
    f_csv.writerows(newlines)
