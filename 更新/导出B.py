import re
from tqdm import tqdm
import csv
import codecs
import hashlib
        
def BtoE(ByteArray):
    English = ""
    ByteArray = ByteArray[1:-3]
    while len(ByteArray)>1:
        try:
            if (int('0x'+str(ByteArray[0:2]),16)> 20 and int('0x'+str(ByteArray[0:2]),16)<126 and int('0x'+str(ByteArray[3:5]),16)==0):
                English = English + chr(int('0x'+str(ByteArray[0:2]),16))
        except ValueError:
            break
        ByteArray = ByteArray[6:]
    return English

newlines = []
md5 = hashlib.md5()
with codecs.open("Assembly-CSharp-NoHH.il", "r", encoding="utf-8-sig") as file:
    lines = file.readlines()
    i = 0
    for line in tqdm(lines):
        item = re.findall(r'\s+IL_[\s\S]+:\s+ldstr\s+bytearray\s+([\s\S]*)', line)
        if(item):
            md5.update(item[0].encode('utf-8'))
            newlines.append([md5.hexdigest(),BtoE(item[0])])
            if (md5.hexdigest()=='39fd4f707a30748ab4054eaa3c2ddbd7'):
                print(item)

    print(i)

with codecs.open("extract.il", "w", encoding="utf-8-sig") as file:
    for newline in newlines:
        file.write(newline[0] + ","+ newline[1] +"\n")
#with codecs.open("4nd.csv", "w", encoding="utf-8-sig") as file:
    #f_csv = csv.writer(file)
    #f_csv.writerow(['MD5','原文', '翻译'])
    #f_csv.writerows(newlines)
    #for newline in newlines:
    #    f_csv.writerows([newline[0],newline[1],''])

