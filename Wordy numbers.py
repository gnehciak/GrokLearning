

def words2number(line):
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}
    for i in line.split():
        line = line.replace(i, dic[i])
        line = line.replace(' ', '')
    return int(line)


print(words2number('three two one'))
