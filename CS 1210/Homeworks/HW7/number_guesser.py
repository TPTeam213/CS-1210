"""
Ben Frederick
CS 1210
"""

import random        # Don't change this line!
import sys           # Don't change this line!

MAX_GUESSES = 10     # Don't change this line!
UPPER_BOUND = 1024   # Don't change this line!

def guess(target, guesses):
    g = int(input('Enter your guess: '))
    while g < 1 or g > UPPER_BOUND:
        print(f'INVALID! Guesses must be in the range [1, 1024]. Try again.')
        g = int(input('Enter your guess: '))
    while g in guesses:
        print(f'INVALID! You have already guessed {g}. Try again.')
        g = int(input('Enter your guess: '))
    else:
        guesses.append(g)
        if g == target:
            return True
        else:
            return False

def play(target):
    guesses = []
    c = 1
    num = MAX_GUESSES
    for i in range(MAX_GUESSES):
        print(f'You have {num} guesses remaining.')
        a = guess(secret_number, guesses)
        if a:
            print(f'You WIN! The secret number was {secret_number} and it took you {c} guesses.')
            break
        else:
            if guesses[len(guesses) - 1] > target:
                print('Guess is too HIGH!')
            elif guesses[len(guesses) - 1] < target:
                print('Guess is too LOW!')
            c += 1
            num -= 1
    if num == 0:
        print('You LOSE!')

if __name__ == '__main__':
    if len(sys.argv) > 1:                # Don't change this line!
        random.seed(sys.argv[1])         # Don't change this line!
    print(f"Try to guess the secret number from 1 to {UPPER_BOUND}.")     
    secret_number = random.randint(1 , UPPER_BOUND)   # Use random.randint() here.
    play(secret_number)                  # Don't change this line!