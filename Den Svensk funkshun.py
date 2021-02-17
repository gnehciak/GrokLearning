

def eng2chef(line):
    translate = {'tion': 'shun', 'an': 'un', 'th':'z','v':'f','w':'v','c':'k','o':'oo','i':'ee',}
    for value in translate.keys():
        line = line.replace(value, translate[value])
    if(line[-1] == '!'):
        line = line.replace('!', '. bork bork bork!!')
    return line

print(eng2chef('action!'))






"""
Input	Output
tion	shun
an	un
th	z
v	f
w	v
c	k
o	oo
i	ee
"""