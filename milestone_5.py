import random
from all_words import word_list

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    #fix me, first letter never matches
    def __substitute_letter(self,guess):
        for letter in self.word:
            if letter == guess or letter == guess.upper():
                index_of_letter = self.word.index(letter)
                self.word_guessed[index_of_letter] = guess
        self.num_letters -= 1
        print(f"Good guess! {guess} is in the word.")

    #fix me, first letter 
    def _check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            self.__substitute_letter(guess)
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if not(len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
        
            else:
                self._check_guess(guess)
                self.list_of_guesses.append((guess))
            
            #These print statements are for testing purposes, Delete afterwords
            print(self.word)               
            print(self.word_guessed)
            print(self.num_letters)
            print(self.list_of_guesses)
            break


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")
            break

play_game(word_list)



