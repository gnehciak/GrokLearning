import csv
win = input('Winning title: ')
with open('nominees.csv', 'r') as file:
    for line in csv.DictReader(file):
        if(line['title'] == win):
            print(f"Congratulations: {line['director(s)']}")