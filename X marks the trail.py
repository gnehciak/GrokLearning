size = int(input('Grid size: '))

pos = [0, 0]
table = []
for i in range(size):
    row = []
    for j in range(size):
        row.append('.')
    table.append(row)

line = ' '
while line:
    if(line == 'right'):
        pos[1] += 1
    elif(line == 'down'):
        pos[0] += 1
    elif(line == 'left'):
        pos[1] -= 1
    elif(line == 'up'):
        pos[0] -= 1
    table[pos[0]][pos[1]] = 'x'

    for row in table:
        for i in row:
            print(i, end='')
        print()
    line = input('Direction: ')