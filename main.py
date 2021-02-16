# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


mono, multi = [], []

line = input('Line: ')
while line:
    line = (line.replace(line.partition(' ')[0], '').strip().split())
    for i in line:
        if i in mono and i not in multi:
            multi.append(i)
            mono.remove(i)
        elif i not in mono and i not in multi:
            mono.append(i)
    line = input('Line: ')
if mono:
    for i in mono:
        print(f"{i} is monolingual")
else:
    print("Everyone is multilingual!")
"""

"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
English Tim Nicky James Tara John Ben
Mandarin Tim John
German Nicky Tim
"""