"""import xml.etree.ElementTree as Xet
import pandas as pd

source = open('timetable.xml', encoding="utf-8")
source.readline()
x = source.read().split('\n')
cols = []
rows = []
rows1 = []
for i in range(len(x)):
    tag = x[i].strip().replace('<', '>').split('>')[1:-1]
    if len(tag) != 3:
        pass
    else:
        cols.append(tag[0])
        rows.append(tag[1].strip())


xmlparse = Xet.parse('timetable.xml')
rows1.append(dict(zip(cols, rows)))
df = pd.DataFrame(rows1, columns=cols)
df.to_csv('timetable.csv', index=False)"""

import csv
from collections import OrderedDict
source = open('timetable.xml', encoding="utf-8")
source.readline()
x = source.read().split('\n')
header = []
info = []
for i in range(len(x)):
    tag = x[i].strip().replace('<', '>').split('>')[1:-1]
    if len(tag) != 3:
        pass
    else:
        header.append(tag[0])
        info.append(tag[1].strip())

new_header = list(OrderedDict.fromkeys(header))
csvfile = open("data2.csv", 'w', encoding='utf-8')
csvfile_writer = csv.writer(csvfile, lineterminator='\n')
csvfile_writer.writerow(new_header)

a = []
for i in info:
    a.append(i)
    if len(a) == len(new_header):
        csvfile_writer.writerow(a)
        a = []

source.close()
csvfile.close()

