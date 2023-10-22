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

    def __substitute_letter(self,guess):
        for letter in self.word:
            if letter == guess:
                index_of_letter = self.word.index(letter)
                self.word_guessed[index_of_letter] = guess
            self.num_letters -= 1
        print(f"Good guess! {guess} is in the word.")


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


hangman_game = Hangman(word_list)
hangman_game.ask_for_input()
