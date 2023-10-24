import numpy as np
import random
from all_words import word_list 

word = random.choice(word_list)

def user_guess():
    '''
    This function asks the user for a letter and validates it.

    Returns:
        str: The user input in form of a string
    '''

    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a vaild input.")

#user_guess()