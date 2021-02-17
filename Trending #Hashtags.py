import collections
import string

h_counts = collections.defaultdict(int)

line = input("Tweet: ").split()
while line:
    for word in line:
        if (word[0] == '#'):
            h_counts[word.strip(string.punctuation).lower()] += 1
    line = input("Tweet: ").split()

for hashtag in h_counts:
    print(f"#{hashtag} {h_counts[hashtag]}")



"""
Tweet: #Python is #AWESOME!
Tweet: This is #So_much_fun #awesome
"""