freq = {}

with open('novel.txt', 'r') as file:
    for line in file:
        for word in line.split():
            if(word.lower() != word and word[0].lower != word[0] and word not in freq):
                freq[word] = 1
            elif(word.lower() != word and word[0].lower != word[0] and word in freq):
                freq[word] += 1
freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
top = 0
while top < 3:
    print(freq[top][1], freq[top][0])
    top += 1
