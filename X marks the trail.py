size = int(input('Grid size: '))

table = []
for i in range(size):
  row = []
  for j in range(size):
    row.append('.')
  table.append(row)

for row in table:
  print(row)