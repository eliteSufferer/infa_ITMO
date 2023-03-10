import re


def f(a):
    g = "P3111"
    for w in a:
        if re.fullmatch(r'([А-Я])\w*([- ]\1\w*)? (\1\.){2} P3111', w):
            a.remove(w)
    return a


with open("Test_3", encoding="utf-8") as k:
    d = []
    while True:
        c = k.readline()
        if not c:
            break
        if c[-1] == '\n':
            d.append(c[:-1])
        else:
            d.append(c)
    fio1 = d[0:4]
    fio2 = d[4:8]
    fio3 = d[8:12]
    fio4 = d[12:16]
    fio5 = d[16:20]

    for x in range(1, 6):
        z = 'fio' + str(x)
        for i in f(eval(z)):
            print(i)
        print()



    #print(*[f(i[1]) for i in filter(lambda x: x[0].startswith('fio'), dict(f.__globals__).items())], sep='\n')