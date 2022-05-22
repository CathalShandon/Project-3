import random
import time
import os


def welcome():
    """
    Show welcome message and ask user if they would like to see instructions.
    """


# A welcome to the game
    name = input("Enter your username: ")
    os.system("cls" if os.name == "nt" else "clear")
    print("Hello " + name + " Best of luck in this Hangman game!\n")
    print("Before you start would you like to see the rules to play or are you"
          " ready to play?")
    see_instructions = input(
        "Please type 1 to see the instructions, " "or 2 play game:\n"
        )
# Make sure users input is valid.
    while see_instructions != "1" and see_instructions != "2":
        see_instructions = input(
            "\nInvalid input, Please type 1 to "
            "see the instructions, or 2 to skip them "
            "and\nstart the game:\n"
        )
    # Take user to relevant page.
    if see_instructions == "1":
        instructions()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        hangman()


def instructions():
    """
    Instructions to explain to the user how to play
    """

    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # print instructions
    print("To play this preimer league hangman game, all you need to "
          "do is guess the word one letter at a time. \n\n1. "
          "Type a letter of your choice and hit enter.\n2. If your guess is"
          " correct the letter will show within the hidden word.\n3. If your"
          " guess is incorrect a section of the hangman picture will appear."
          "\n4. Keep guessing until you guess the correct word or you run"
          "out of tries.\n")

    # Ask user if they are ready to play.
    print("Are you ready to play?")
    ready = input("Please type y for yes or any button to go"
                  "back to welcome page:\n")
    if ready == "y":
        os.system("cls" if os.name == "nt" else "clear")
        hangman()
    else:
        os.system("cls" if os.name == "nt" else "clear")
        welcome()


# The game
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["chelsea", "liverpool", "leeds", "watford", "everton",
                      "asrsenal", "wolves", "tottenham", "norwich",
                      "newcastle"]
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
        os.system("cls" if os.name == "nt" else "clear")
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

    # Game starts.
    print(
        "Hint: The word has", len(word), "letters")
    guess = input("This is the word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter.\n")
        os.system("cls" if os.name == "nt" else "clear")
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
            print("The word was: ", already_guessed, word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()


main()
welcome()
instructions()

hangman()