racers = ['Dash', 'Speedy', 'Lightning', 'Flash', 'Sonic']
print("And the line up is:", ', '.join(racers))
sleep = input("Who's gone to sleep? ")
if(sleep in racers):
    print(sleep, 'has been disqualified!')
    index = racers.index(sleep)
    racers[index] = 'Disqualified'
else:
    print("All snails still awake.")
print("Remaining racers:", ', '.join(racers))
