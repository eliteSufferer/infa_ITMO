"""import re
with open("Test_2", encoding="utf-8") as f:
    k = f.readlines()
    for s in k:
        s = re.sub(r'\s{2,}', ' ', s)
        a = re.split(r'\W', s)
        i = 0
        while i < len(a):
            w = a[i]
            if re.fullmatch(r'[a-zA-Zа-яА-Я]+', w):
                x = re.search(rf'{w}( {w})\W', s, flags=re.IGNORECASE)
                if x:
                    s = re.sub(x[0][:-1], w, s)
                    i += 1
            i += 1
        print(s)
"""

import re
with open("Test_2", encoding="utf-8") as f:
    k = f.readlines()
    for s in k:
        print(re.sub(r'\b(\w+)\b(?:\s+\1)+\b', r'\1', s, flags=re.IGNORECASE))
