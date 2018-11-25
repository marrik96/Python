# Guess game
import random
print('Hello, name?')
name = input()
secretNum = random.randint(1,20)
print(name + ' I\'m thinking of number between 1 and 20')

# Ask player for gueses 6 times
for guessesTaken in range(1,4):
    print('Take guess.')
    guess = int(input())
    if guess < secretNum:
        print('too low')
    elif guess > secretNum:
        print('too high')
    else:
        break # this condition is correct guess

if guess == secretNum:
    print('good job! ' + name)
else:
    print('No, the number was ' + str(secretNum))