"""
Sentence: Where is my dog? ROVER, COME HERE!
Number of shouted words: 3
"""
line, num = input('Sentence: '), 0
for i in line.split():
    if(i.upper() == i):
        num += 1
print(f"Number of shouted words: {num}")