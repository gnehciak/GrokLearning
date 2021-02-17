songnum = int(input('How many more songs? '))

with open('songlist.txt', 'r') as file:
    lines = file.readlines()
    while songnum > 0:
        print(lines.pop().strip())
        songnum -= 1