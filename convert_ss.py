'''def c(a, b):
    s = ''
    while a > 0:
        s += str(a % b)
        a //= b
    return s[::-1]


print(c(42, 2))

a, b, c, d, e, f, g, h = map(int, input().split())
a1, b1, c1, d1, e1, f1, g1, h1 = map(int, input().split())
a2, b2, c2, d2, e2, f2, g2, h2 = map(int, input().split())
a3, b3, c3, d3, e3, f3, g3, h3 = map(int, input().split())
s1 = a ^ b ^ c ^ d ^ e ^ f ^ g ^ h
s2 = a1 ^ b1 ^ c1 ^ d1 ^ e1 ^ f1 ^ g1 ^ h1
s3 = a2 ^ b2 ^ c2 ^ d2 ^ e2 ^ f2 ^ g2 ^ h2
s4 = a3 ^ b3 ^ c3 ^ d3 ^ e3 ^ f3 ^ g3 ^ h3
print(s1, s2, s3, s4)

print(int('111', 2))
'''


msg = input()
if len(msg) != 7 or set(msg) != {'0', '1'}:
    print("Невозможно декодировать строку!")
else:
    i = ['r1', 'r2', 'i1', 'r3', 'i2', 'i3', 'i4']
    s1 = int(msg[0]) ^ int(msg[2]) ^ int(msg[4]) ^ int(msg[6])
    s2 = int(msg[1]) ^ int(msg[2]) ^ int(msg[5]) ^ int(msg[6])
    s3 = int(msg[3]) ^ int(msg[4]) ^ int(msg[5]) ^ int(msg[6])
    s = (str(s1) + str(s2) + str(s3))[::-1]
    d = int(s, 2)
    if s == '000':
        print('Нет ошибок')
    else:
        print('Ошибка в бите', i[d - 1])
        msg_list = list(msg)
        if msg_list[d - 1] == '0':
            msg_list[d - 1] = '1'
        else:
            msg_list[d - 1] = '0'

        corr_mess = ''
        for i in msg_list:
            corr_mess += str(i)
        corr_mess = corr_mess.replace(corr_mess[0], '', 1)
        corr_mess = corr_mess.replace(corr_mess[0], '', 1)
        corr_mess = corr_mess.replace(corr_mess[1], '', 1)
        print('Исправленное сообщение:', corr_mess)