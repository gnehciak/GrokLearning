times, step = int(input("Times table: ")), int(input("Step: "))

curstep = 3
while 3 <= curstep <= 12:
    print(f"{times} x [ ] = {times * curstep}")
    curstep += step
