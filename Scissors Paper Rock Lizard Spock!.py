RULES = {
    ('scissors', 'paper'): 'scissors',
    ('paper', 'rock'): 'paper',
    ('rock', 'scissors'): 'rock',
    ('rock', 'lizard'): 'rock',
}

hand1 = input('hand 1: ')
hand2 = input('hand 2: ')
winner = RULES.get((hand1, hand2), RULES.get((hand2, hand1)), 'tie')
print(winner)
"""

Scissors cut Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock melts Scissors
Scissors decapitate Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock breaks Scissors

"""