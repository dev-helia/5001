'''
CS5001 Lab 3
Brandan Yong
Fall 2024
'''
import random

def random_number():
    '''
    fxn wiil generate a random integer from 1 to 5, prompt user for a guess
    and let the user know if they were correct, along with what the random
    integer was.
    '''
    # ask user for their name
    name = input('Hello! What is your name?')
    print(f'Cool, great to meet you, {name}!')
    print('I\'m guessing a number between 1 and 5')
    guess = int(input('Enter your guess:'))
    number = random.randint(1, 5)
    
    
