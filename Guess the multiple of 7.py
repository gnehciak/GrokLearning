ans = {42: True}
life = 9
mistake = 0
guess = int(input('Guess a multiple of 7: '))
while guess and life != 0:
    if guess % 7 == 0:
        if ans.get(guess, False):
            print('You won!')
            break
        else:
            print('Nope!')
            life -= 1
    else:
        if mistake == 0:
            print("Mistake! That number isn't a multiple of 7.")
            mistake = 1
            life -= 1
        else:
            print('Another mistake. Too bad.')
            break
    guess = int(input('Guess a multiple of 7: '))
if(life == 0):
    print('Nope!')
    print('No guesses left!')
print('That was fun.')