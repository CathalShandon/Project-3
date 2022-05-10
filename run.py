import random
import time

#Initial steps to start game
print("Welcome to the Hangman game")
name = input("Enter your name: ")
print("Hello " + name + " Best of luck in this Hangman game!" )

#The game
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = &#91; "Chelsea", "Liverpool", "Burnley", "Watford", "Everton", "Arsenal", "Wolves", "Tottenham", "Brentford", "Newcastle"]
    word = random.choice(words_to_guess) 
    length = len(word)
    count = 0
    display = ' ' * length
    already_guessed = &#91;]
    play_game = ''
 
