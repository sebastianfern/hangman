import random


class Hangman():
    def __init__(self):
        self.guessed_letters = []
        self.char_indexes = []
        self.correct_guesses = []

    def main(self):
        print("Let's play Hangman.")
        number_of_tries = 26
        filename = 'RandomEnglishWords.txt'
        target_line = self.generate_targetline()
        selected_word = self.find_word(filename, target_line)
        while True:
            user_guess = input("Enter a letter: ").lower()
            if user_guess in self.guessed_letters:
                print(f"{user_guess} has been guessed already")
                continue  # Skip the rest of the loop and prompt for a new letter
            self.find_position(selected_word, user_guess, self.correct_guesses, self.char_indexes)
            print(f"\n{self.char_line(selected_word, self.correct_guesses)}")
            print(f"Letters you guessed so far are: {self.guessed_letters}")
            number_of_tries -= 1

            # Check for win condition
            if set(self.correct_guesses) == set(range(len(selected_word))):
                print(f"\nYou won! The word was '{selected_word}'.")
                return True

            if number_of_tries < 0:
                print(f"You are out of guesses. The word was '{selected_word}'.\n")
                return False


    
    def find_word(self, filename, targetline):
        with open(filename, 'r') as file:
            for current_line_number, word in enumerate(file):
                if current_line_number == targetline:
                    return word.strip()
                
    def generate_targetline(self):
        return random.randint(0,20)
    
    def char_line(self, selected_word, char_indexes):
        """This fucntion will take the word the user is guessing and a list of the indexes of letters already guessed.
        initially this function will show underscores in the console the length of the given word to represent spaces not yet guessed correctly.
        
        as letters are guessed the characters will be filled in to the word by there position in the list.
        """
        spaces_displayed = ""
        for ch in range(len(selected_word)):
            if ch in char_indexes:
                spaces_displayed = spaces_displayed + str(selected_word[ch])
            else:
                spaces_displayed = spaces_displayed + "_"
        return spaces_displayed
            
    def find_position(self, selected_word, user_guess, correct_guesses, char_indexes):
        """ This function will be used to find the location of the newly guessed letter, and add it to the list of 
        previously correctly guessed letter positions to be returned. """
        for ch in range(len(selected_word)):
            if selected_word[ch] == user_guess:
                    correct_guesses.append(ch)
        char_indexes.append(user_guess)
        self.guessed_letters.append(user_guess)
        return None
    

if __name__ == '__main__':
    game = Hangman()
    game.main()