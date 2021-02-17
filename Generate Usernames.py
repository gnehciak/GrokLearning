
dic = []
username = []
with open('classlist.txt', 'r') as file:
    for line in file:
        first, mid, last = '', '', ''
        if(len(line.split()) == 2):
            first, last = line.lower().split()
            dic.append([first, '', last])
        else:
            first, mid, last = line.lower().split()
            dic.append([first, mid, last])

for name in dic:
    n1 = ''.join(name[0:2])
    n2 = n1+name[2][0]
    num = 1
    if n1 not in username:
        username.append(n1)
    elif n1 in username and n2 not in username:
        username.append(n2)
    elif n1 in username and n2 in username:
        created = False
        while created == False:
            if n2 + str(num) not in username:
                username.append(n2 + str(num))
                created = True
            else:
                num += 1

for name in username:
    print(name)
