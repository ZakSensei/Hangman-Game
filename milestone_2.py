import numpy as np
import random
from all_words import word_list 

word = random.choice(word_list)

def user_guess():

    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a vaild input.")


#user_guess()