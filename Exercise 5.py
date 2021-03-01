# 1
ing1, ing2 = input("Ingredient 1: "), input("Ingredient 2: ")
print(ing1, ing2)
# 2
card1, card2 = input("Card 1: "), input("Card 2: ")
while card1 != card2:
    print('Keep playing.')
    card1 = card2
    card2 = input("Card 2: ")
print("Snap")
# 3
print('$', round(float(input("Original Price: "))*0.8, 2), sep='')
# 4
test1, test2, test3 = float(input("test 1: ")), float(input("test 2: ")), float(input("test 3: "))
avg = round((test1 + test2 + test3)/3, 2)
print(f"Your average is: {avg}" if avg <= 90 else f"Congratulations, your result of {avg} is greater than 90!")
# 5
limit = int(input("Limit: "))
squarenum = 1
while squarenum ** 2 <= limit:
    print(squarenum ** 2)
    squarenum += 1
# 6
salesp = {}
peep = input("Sales Person: ")
while peep:
    price = float(input("Price: "))
    salesp[peep] = salesp[peep] + round(price*0.1, 2) if peep in salesp else round(price*0.1, 2)
    price = 0
    peep = input("Sales Person: ")
for i in salesp.keys():
    print(i, ' $', round(salesp[i], 2), sep='')