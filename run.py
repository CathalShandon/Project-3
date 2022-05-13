import random
import time

# Initial steps to start game #
print("Welcome to the Hangman game")
name = input("Enter your name: ")
print("Hello " + name + " Best of luck in this Hangman game!")
time.sleep(2)
print("The game is about to start!\nCan you guess this premier league team!")
time.sleep(2)

# The game #


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["chelsea", "Liverpool", "Leeds", "Watford", "Everton",
                      "asrsenal", "Wolves", "Tottenham", "Brentford",
                      "Newcastle"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
# A loop to re-excute when the first rounds ends #


def play_loop():
    global play_game
    play_game = input("Do You want to play game again? y = yes, n = no \n ")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play game again? y = yes, n = no \n")
    if play_game == 'y':
        main()
        hangman()
    elif play_game == "n":
        print("Thanks For Playing! We hope to see you back again!")
        exit()

# Conditions required to play game #


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter.\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter. \n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count)
                  + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count)
                  + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count)
                  + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count)
                  + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was: ", word, already_guessed)
            play_loop()


    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()


main()


hangman()