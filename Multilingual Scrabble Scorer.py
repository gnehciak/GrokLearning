dic = {}
total = 0
with open('scrabble_letters.txt', 'r') as file:
    for line in file:
        point, word = line.split()
        dic[word] = point
word = input('Word: ')
for i in word:
    total += int(dic[i.upper()])
print(f"{total} points")