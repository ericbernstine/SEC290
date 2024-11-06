# Eric Bernstine
# SEC290
# Week 3 Assignment

import random
ran_num = random.randint(1, 20)
num_lives = 3
print('Welcome to the secret guessing game, are you ready to play?')
while num_lives > 0:
    guess = int(input('Guess a number between 1 and 20\n>'))
    if guess < 0 or guess > 20:
        print('Please guess a number between 1 and 20.')
        continue
    if guess > ran_num:
        num_lives = num_lives - 1
        print(f'Number too high\nLives left: {num_lives}')
    elif guess < ran_num:
        num_lives = num_lives - 1
        print(f'Number too low\nLives left: {num_lives}')
    else:
        print(f'Perfect! you guessed it. The secret number was {ran_num}')
        break;
if num_lives <= 0:
    print(f"Sorry you're all out of lives, the secret number was {ran_num}. better luck next time")
