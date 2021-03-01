start = float(input('Start (g): '))
finish = float(input('Finish (g): '))
hours = 0
while start < finish:
    start = start + 0.6 * start
    hours += 1
print(f"The loaf would need to rise for {hours} hours.")