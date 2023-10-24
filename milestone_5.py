import random
from all_words import word_list

class Hangman():
    '''
    This class is used to create a hangman game.

    Attributes:
        word (str): The word to be guessed, picked randomly from the word list.
        word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed.
        num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
        num_lives (int): The number of lives the player has at the start of the game.
        word_list (list): A list of words.
        list_of_guesses (int): A list of the guesses that have already been tried. Set this to an empty list initially.
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Date) for accurate signature
        '''
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def __substitute_letter(self,guess):
        #private method only to be called by the class
        for index, letter in enumerate(self.word):
            if letter == guess: 
                self.word_guessed[index] = guess
        self.num_letters -= 1
        print(f"Good guess! {guess} is in the word.")

       
    def _check_guess(self,guess):
        '''
        This function check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer.

        Args:
            guess (str): The letter guessed by the user.
        '''
        guess = guess.lower()
        if guess in self.word:
            self.__substitute_letter(guess)
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    
    def ask_for_input(self):
        '''
        This function continuously ask the user for a letter and validates it.

        Returns:
            str: The user input in form of a string
        '''
        while True:
            guess = input("Guess a letter: ")
            if not(len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
        
            else:
                self._check_guess(guess)
                self.list_of_guesses.append((guess))
            
            print(f"{self.word_guessed} \n")
            break


def play_game(word_list):
    '''
    This function is used to play an already created hangman game.

    Args:
        word_list (list): A list of words.
    '''
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print(f"Sorry, You have lost! The word was {game.word}")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters <= 0:
            print(f"Congratulations. Your word was {game.word}. You've won the game!")
            break

play_game(word_list)



