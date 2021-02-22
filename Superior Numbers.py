arrogant_numbers = [3, 6, 7, 23, 25, 35, 39, 66, 68, 112, 119, 254, 259, 732, 737, 4565, 4663, 13330, 13730, 29880, 29998, 79670, 80015, 230054, 239068, 1534301, 1607352, 2060587, 21700891, 99167753, 99873125]

def find_personality(number):
  traits = ''
  # Find the traits of the number
  if number % 2 != 0:
    traits = traits + 'odd '
  # Check for other traits after this
  if number >= 10000:
      traits = traits + 'excessive '
  if '3' in str(i):
     traits = traits + 'irksome '
  if number in arrogant_numbers:
      traits = traits + 'arrogant '
  if number == traits:
      return False
  return traits

# Write the rest of your program after this
dull = 0
num = input("Enter numbers: ").split()
for i in num:
    if find_personality(int(i)):
        print(f"{i} is an {find_personality(int(i))}number.")
    else:
        dull += 1
print(f"Dull numbers: {dull}")