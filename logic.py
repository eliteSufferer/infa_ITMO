x = ['I', 'like', 'to', 'study', 'at', 'ITMO']
print(x[6:0:-3])
print(None and 42)

x = "a"
res = "AAA" if ord(x) > 129 else "BBB"
print(res)

import re
s = 'int[][] arr = new int[10][10]'
print(re.search(r'\[.*?\]', s))

s = ["АннаXVIII", "АннаXX", "АннаXXL", "АннаXVI", "АннаLXVII", "Анна"]
for i in s:
    res = re.search(r'Анна(?=(X|IV|V?I{1,3})(?=[IX]))', i)
    print(res.group(0) if res else None)

s = 'Слова "регулярка" и "отдебажить" являются жаргоном.'
res = re.search(r'\".*?\"', s)
print(res.group(0))

s = ["XI век", "V век", "IV век", "XX век", "X век", "IX век"]
for i in s:
    res = re.search(r'(?<=(IV|XV|VI|IX|XI)) век', i)
    print(res.group(0) if res else None)

s = 'Слова "ИТМО" и "ВТ" вы запомните на всю жизнь.'
res = re.search(r'\".*?\"', s)
print(res.group(0))

s = ["Карл", "КарлXX", "КарлXVIII", "КарлXVI", "КарлLXVII", "КарлXXL"]
for i in s:
    res = re.search(r'Карл(?=X(IX|IV|V?I{,3})(?![XVI]))', i)
    print(res.group(0) if res else None)

s = ["Карл", "КарлXX", "КарлXVIII", "КарлXVI", "КарлLXVII", "КарлXXL"]
for i in s:
    res = re.search(r'Карл(?=X(IX|IV|V?I{,3})(?![XVI]))', i)
    print(res.group(0) if res else None)