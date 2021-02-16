from itertools import combinations

dct = {}
line = input('Line: ')
while line:
    line = line.lower().split()
    i = 0
    while i + 1 < len(line):
        bigram = line[i] + ' ' + line[i + 1]
        if(bigram in dct):
            dct[bigram] = int(dct[bigram]) + 1
        else:
            dct[line[i] + ' ' + line[i + 1]] = 1
        i += 1
    line = input('Line: ')
for i in dct:
    if(dct[i] > 1):
        print(f"{i}: {dct[i]}")

"""
The big red ball
The big red ball is near the big red box
I am near the box
"""