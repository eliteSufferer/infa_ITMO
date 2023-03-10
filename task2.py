import json

import re

def main():
    source = open('timetable.xml', encoding="utf-8")
    out = open('timetable2.json', 'w', encoding="utf-8")
    source.readline()
    out.write('{\n')
    x = re.split(r'\n', source.read())
    count = 4
    for i in range(len(x)):
        tag = re.split(r'[<>]', x[i].strip())[1:-1]
        end = ''
        if i == len(x) - 1 or x[i + 1].strip()[:2] == '</':
            end = ''
        else:
            end = ','
        if len(tag) > 2:
            tag = tag[:-1]
        if len(tag) == 1:
            if tag[0][0] == '/':
                out.write(' ' * (count-4) + '}' + end + '\n')
                count -= 4
            else:
                out.write(' ' * count + '"' + tag[0] + '": {\n')
                count += 4
        else:
            out.write(' ' * count + '"' + tag[0] + '" : "' + tag[1].strip() + '"' + end + '\n')


main()