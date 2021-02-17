def fix_yz(line):
    replace = {'y': 'z', 'z': 'y', 'Y': 'Z', 'Z': 'Y'}
    output = ''
    for i in line:
        output += (replace.get(i, i))
    return output


print(fix_yz('Zour tip about the yoo was a great one!'))
