import json

import xmltodict


def main():
    source = open('timetable.xml', encoding="utf-8")
    out = open('timetable1.json', 'w', encoding="utf-8")
    x = source.read()
    o = xmltodict.parse(x)
    json.dump(o, out, indent=4, ensure_ascii=False)

main()