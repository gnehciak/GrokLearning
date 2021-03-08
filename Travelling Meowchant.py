dic = {}


while True:
    item = input("Item: ")
    if not item:
        break
    num = int(input("Number sold: "))
    if (item in dic):
        dic[item] += num
    else:
        dic[item] = num

print("Total sales for today:")
for i in dic:
    print(i, dic[i], sep=" : ")



"""
Item: Griffin Milk
Number sold: 1
Item: Cabbage
Number sold: 3
Item: Griffin Milk
Number sold: 1
Item: Shadow Parsley
Number sold: 7
Item: Elixir
Number sold: 2
Item: Elixir
Number sold: 3
Item: Griffin Milk
Number sold: 1
Item: 
Total sales for today:
Griffin Milk : 3
Cabbage : 3
Shadow Parsley : 7
Elixir : 5
"""