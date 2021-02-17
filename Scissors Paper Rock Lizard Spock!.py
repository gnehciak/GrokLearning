RULES = {
    ('scissors', 'paper'): 'Scissors cut Paper',
    ('scissors', 'lizard'): 'Scissors decapitate Lizard',
    ('paper', 'rock'): 'Paper covers Rock',
    ('paper', 'spock'): 'Paper disproves Spock',
    ('rock', 'scissors'): 'Rock breaks Scissors',
    ('rock', 'lizard'): 'Rock crushes Lizard',
    ('lizard', 'spock'): 'Lizard poisons Spock',
    ('lizard', 'paper'): 'Lizard eats Paper',
    ('spock', 'scissors'): 'Spock melts Scissors',
    ('spock', 'rock'): 'Spock vaporizes Rock',
}
hand1 = input('Hand 1: ')
hand2 = input('Hand 2: ')
winner = RULES.get((hand1, hand2), RULES.get((hand2, hand1), 'Tie'))
print(winner)
