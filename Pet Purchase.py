line = input('What animal would you like? ')
num = int(input('How many? '))
if(line == line.upper()):
    print("Woah! No need to shout, you'll scare the animals!")
else:
    if(num == 0):
        print("That's sad. No pet for you today.")
    elif(num == 1):
        print(f"Great, here's your {line.lower()}!")
    elif(num > 1):
        print(f"Ok! {num} {line.lower()}s coming right up!")