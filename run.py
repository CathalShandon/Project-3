import random
import time

# Initial steps to start game #
print("Welcome to the Hangman game")
name = input("Enter your name: ")
print("Hello " + name + " Best of luck in this Hangman game!" )

# The game #
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["Chelsea", "Liverpool", "Burnley", "Watford", "Everton", "Arsenal", "Wolves", "Tottenham", "Brentford", "Newcastle"]
    word = random.choice(words_to_guess) 
    length = len(word)
    count = 0
    display = ' ' * length
    already_guessed = []
    play_game = ''
 
# A loop to re-excute when the first rounds ends #

def play_loop():
    global play_game
    play_game = input("Do You want to play game again? y = yes, n = no \n ")
    while play_game not in ["y", "n", "Y", "N"]
        play_game input("Do You want to play game again? y = yes, n = no \n ")
    if play_game == 'y':
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

# Conditions required to play game #
def Hangman():
    global count 
    global display
    global word
    global already_guessed
    global play_game 
    limit = 5 
    guess = input("This is the Hangman word: " + display + "Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) == 2 or guess == 9:
        print("Invalid Input, Try a letter\n")
        hangman()

