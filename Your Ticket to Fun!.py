def buy_slinkies(tickets):
    return int(tickets / 3)

ctest = {}

print("Who's here at the carnival today?")
name = input("Name: ")
while name:
    ctest[name] = int(input("Starting tickets: ")) if name not in ctest else None
    print(f"{name}'s here, starting with {buy_slinkies(ctest[name])} slinkies worth of tickets!")
    name = input("Name: ")

print("Let the games begin!")
name = input("Who played? ")
while name:
    ctest[name] = int(input("Tickets won/lost: ")) if name not in ctest else ctest[name] + int(input("Tickets won/lost: "))
    name = input("Who played? ")

print("End of the day! Let's see how everyone did!")
for i in ctest:
    print(i, "can buy", buy_slinkies(ctest[i]), "slinkies.")










