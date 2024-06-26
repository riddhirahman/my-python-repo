# Riddhi's Impossible Number Guessing Game
import random
print('To guess a number between your given range, you also have customizable chances to guess the number')
start = int(input('Enter your starting range number: '))
end = int(input('Enter your ending range number: '))
chances = int(input('How many chances?'))
guess_number = random.randint(start, end)
if chances > end-start:
    print(f'Chances are more than the given ({end-start}) numbers!')
elif chances == 0:
    print('Chances cannot be 0!')
else:
    print('---------------------------------  Begin!  ---------------------------------')
    chance_count = 0
    while chance_count < chances:
        guess = int(input('Your Guess: '))
        if guess < start or guess > end:
            print('Out of range!')
        else:
            chance_count += 1
            if guess == guess_number:
                print(f'Congratulations! {guess} is the number!')
                break
            else:
                print(f'{guess} is not the number. Try again...')
                print(f'You have {chances-chance_count} out of {chances} chances left...')
    if chance_count == chances:
        print(f'Out of chances!')
        enabler = input('Do you want to enable Brute-Force finder? (Y/N) ')
        if enabler == 'Y' or enabler == 'y':
            chance_count = 0
            chances = int(end - start)
            guess = start
            while chance_count < chances:
                while guess != guess_number:
                    guess += 1
                chance_count += 1
                if guess == guess_number:
                    print('Found!')
                    print(f'{guess} was the number!')
                    count = guess-start
                    print(f'{count} numbers counted')
                    break
                else:
                    print(f'{guess} is not the number. Try again...')
        elif enabler == 'N' or enabler == 'n':
            print('Exiting...')
        else:
            print('Invalid choice!')
