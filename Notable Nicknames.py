def is_notable(name):
    if(len(name) == 5 and name[0] == 'N'):
        print("That nickname is notable!")
    else:
        print("That nickname is not so notable!")

line = input('Type a nickname: ')
is_notable(line)