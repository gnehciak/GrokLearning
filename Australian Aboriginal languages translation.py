dic = {}
with open('dictionary.txt', 'r') as file:
    for i in file:
        word, definition = i.strip().split(',')
        dic[word] = definition

line = input('English: ')
output = []
while line:
    for i in line.split():
        output.append(dic[i])
    print(' '.join(output))
    output.clear()
    line = input('English: ')
