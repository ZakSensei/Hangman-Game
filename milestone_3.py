from milestone_2 import word

def ask_for_input():
    '''
    This function continuously ask the user for a letter and validates it.

    Returns:
        str: The user input in form of a string
    '''
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
    

def check_guess(guess):
    '''
    This function check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.

    Args:
        guess (str): The letter guessed by the user.
    '''
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()