flavours = {}
line = input('name and flavour: ')
while line:
  name, flavour = line.split()
  if flavour not in flavours:
    # add it to our dictionary as a list with one element
    flavours[flavour] = [name]
  else:
    flavours[flavour].append(name)
  line = input('name and flavour: ')

for flavour in flavours:
  print(flavour, ':', ' '.join(flavours[flavour]))
