# Python code to pick a random word from the text file
import random


# Function to randomly select a word from the file
def word_to_guess (file_name):
    # open file as read
    with open (file_name, "r") as f:
        # creates a list with the different words in the file
        all_words = f.read().splitlines()
        # randomly selects the word from the list above
        random_word = random.choice(all_words)
    return (random_word)


#following func plays the game
def gameplay(secret_word):
    # creates a serie of underscores as per the secret word length
    word_random_len = "_" * len(secret_word)
    # initial variable guessed set to False. It will be changed to True if user wins
    initial_default_guess = False
    # defined empty list to save the multiple guesses by the user, to be filled in loops below
    guessed_letters = []
    attemps_left = 6 #defined by default
    print("A ramdom word was selected, let's play!. By default you have " + str(attemps_left) + " attemps")
    print (word_random_len)
    # Loop that will continue running until the initial_default_guess becomes "True" or user runs out of "attemps"
    while not initial_default_guess and attemps_left > 0:
        # Request input from user
        guess_by_user = input ("Please guess a letter: ")
        # Conditional to check if input is lower case
        # This check goes first as the input for the user, although correct, shall be compared with previous input
        if guess_by_user.islower():
            # Conditional to check if input was used before
            if guess_by_user in guessed_letters:
                print ("You already guessed the letter", guess_by_user)
                print ("It is okay, it will not affect your attemps")
                print ("Remember, you still have " + str(attemps_left) + " attemps left")
            # Conditional to check if the input guess "is not" in the secret word
            elif guess_by_user not in secret_word:
                # In this case, the user looses one attemp, thus decreasing its value
                attemps_left -= 1
                print (guess_by_user, "it is not in the secret word")
                print ("You have " + str(attemps_left) + " attemps left")
                # User guess input is added to the list of guessed letters
                guessed_letters.append(guess_by_user)
            # If input does not meet the previous two conditional, it means guess is part of the secret word
            else:
                print ("Nicely done, the letter", guess_by_user, "is part of the secret word")
                # print ("Remember, you still have " + str(tries) + " tries left")
                # User guess input is added to the list of guessed letters
                guessed_letters.append(guess_by_user)
                # convert the word completion to a list, then find where the input guess appears in the secret word
                word_as_list = list (word_random_len)
                index_check = [i for i, letter in enumerate(secret_word) if letter == guess_by_user]
                for index in index_check:
                    word_as_list[index] = guess_by_user
                word_random_len = "".join(word_as_list)
                # when all leters are guessed, there wont be more underscores in "word_completion".
                # Hence "guessed" becomes "True" to exit the while loop
                if "_" not in word_random_len:
                    initial_default_guess = True
        # All non-lower case input from the user will fall into this "else"
        else:
            print ("Not a valid guess. Guess shall be lower case letters only")
            print ("It is okay, it will not affect your attemps, try harder!")

        # The variable "world_completion" is printed everytime after any input to show the state of it
        print (word_random_len)
    # Conditional that modifies variable "initial_default_guess" to "True", meaning that the user have won
    if initial_default_guess:
        print ("You have officially won!")
    # If user runs out of attemps, "guessed" remains as "false" hence game over
    else:
        print ("Sorry, you've lost. The secret word was " + secret_word)


#Function below is the master one.
def master():
    print ("Welcome to the 'Jeu du Pendu'")
    # Asks the user for the name of the TXT file. It should include the extension .txt
    # intended to allow user to change or update the "file" containing random words
    # All words is the reference file shall be lower case
    file_name = input("First, please type the txt file name (including the .txt extension) containing secrets words: ")
    secret_word = word_to_guess(file_name)
    gameplay(secret_word)


master()
