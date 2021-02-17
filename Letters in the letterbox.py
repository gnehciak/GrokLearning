name = input('Name: ')
letter, package = [0, 0]
with open('mail.txt', 'r') as file:
    for line in file:
        if line.split(',')[0] == name and line.split(',')[1].strip() == 'Letter':
            letter += 1
        elif line.split(',')[0] == name and line.split(',')[1].strip() == 'Package':
            package += 1

num = {'l1': 'Letter', 'p1': 'Package'}

if letter == 0 and package == 0:
    print('No mail')
elif letter == 0:
    print("No Letters")
    print(f"{package} {num.get('p'+str(package), 'Packages')}")
elif package == 0:
    print(f"{letter} {num.get('l'+str(letter), 'Letters')}")
    print("No Packages")
else:
    print(f"{letter} {num.get('p'+str(letter), 'Letters')}")
    print(f"{package} {num.get('p'+str(package), 'Packages')}")

