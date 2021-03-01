
plants = {}
print("Let's get planting everyone!")
plant = input("What kind of flower did you plant? ")
total = 0
while plant:

    num = int(input("How many did you plant? "))
    if(plant not in plants):
        print(f"Our first {plant}s! We just planted {num} of them!")
        plants[plant] = num
    else:
        print(f"Fantastic! We just planted {num} more {plant}s!")
        plants[plant] += num
    total += num
    plant = input("What kind of flower did you plant? ")
print(f"Nice work, everyone! We planted {total} flowers!")
print("These are all the kinds of flowers we planted today:")

plants = {'flower':12, 'plant':5}
for i in sorted(plants):
    print("🏵️", i)