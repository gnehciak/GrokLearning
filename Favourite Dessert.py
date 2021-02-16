foods = {}
line = input('Name:vote ')
while line:
  name, food = line.split(':')
  if food not in foods:
    foods[food] = [1, name]
  else:
    foods[food].append(name)
    foods[food][0] += 1
  line = input('Name:vote ')

for food in foods:
  print(f"{food} {foods[food][0]} vote(s): {' '.join(foods[food][1:])}")

"""

Name:vote Greg:chocolate
Name:vote Teena:macaroons
Name:vote Georgina:apple pie
Name:vote Will:chocolate
Name:vote Sophia:gelato
Name:vote Sam:ice cream
Name:vote James:chocolate
Name:vote Kirsten:gelato
Name:vote 
apple pie 1 vote(s): Georgina
gelato 2 vote(s): Sophia Kirsten
chocolate 3 vote(s): Greg Will James
macaroons 1 vote(s): Teena
ice cream 1 vote(s): Sam

"""