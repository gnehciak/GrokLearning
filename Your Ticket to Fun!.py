def buy_slinkies(tickets):
    return int(tickets / 3)


ctest = {}

# Get Names

print("Who's here at the carnival today?")

while True:

    name = input("Name: ")
    if not name:
        break
    ticket = int(input("Starting tickets: "))
    if name not in ctest:
        ctest[name] = ticket
    print(f"{name}'s here, starting with {buy_slinkies(ticket)} slinkies worth of tickets!")

# Begin

print("Let the games begin!")
while True:
    name = input("Who played? ")
    if not name:
        break
    if name not in ctest:
        ctest[name] = 0
    ticket = int(input("Tickets won/lost: "))
    ctest[name] += ticket

#End

print("End of the day! Let's see how everyone did!")
for i in ctest:
    print(i, "can buy", buy_slinkies(ctest[i]), "slinkies.")
