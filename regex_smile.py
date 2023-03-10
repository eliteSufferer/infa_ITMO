import re

with open("Test_1") as f:
    s = f.readlines()
    for i in s:
        print(len(re.findall(r';<{\(', i)))
