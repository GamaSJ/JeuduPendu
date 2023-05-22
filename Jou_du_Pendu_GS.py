# Load modules section
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
    # this will be updated afterwards
    word_random_len = "_" * len(secret_word)
    # initial variable "initial_defautl_guess" set to False. It will be changed to True if user wins
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
        # If not, then a message will appear, see else below
        if guess_by_user.islower():
            # Conditional to check if current input was used before
            if guess_by_user in guessed_letters:
                print ("You already guessed the letter", guess_by_user)
                print ("It is okay, it will not affect your attemps")
                print ("Remember, you still have " + str(attemps_left) + " attemps left")
            # Conditional to check if the input guess "is not" in the secret word
            elif guess_by_user not in secret_word:
                # In this case, the user looses one attemp, thus decreasing the number of attemps left
                attemps_left -= 1
                print (guess_by_user, "it is not in the secret word")
                print ("You have " + str(attemps_left) + " attemps left")
                # User guess input is added to the list of guessed letters
                guessed_letters.append(guess_by_user)
            # If input does not meet the previous two conditional, it means the input is part of the secret word
            else:
                print ("Nicely done, the letter", guess_by_user, "is part of the secret word")
                # User guess input is added to the list of guessed letters
                guessed_letters.append(guess_by_user)
                # Following function checks the input of the user and compares with the characters of the secret word.
                # Read comments on block below for details with regards to the function itself
                check_underscores = word_underscores(guess_by_user,secret_word,word_random_len)
                # Output of the function is then changed back to variable "word_random_len"
                # Thus the next iteration will consider the updated version of that variable
                word_random_len = check_underscores
                # when all leters are guessed, there wont be more underscores in "word_completion".
                # Hence, "initial_default_guess" becomes "True" to exit the while loop
                if "_" not in word_random_len:
                    initial_default_guess = True
        # All non-lower case input from the user will fall into this "else"
        else:
            print ("Not a valid guess. Guess shall be lower case letters only")
            print ("It is okay, it will not affect your attemps, try harder!")

        # The variable "world_random_len" is printed  after any input to show the state of it.
        # It is updated by function "word_underscores" that returns "check_underscores"
        print (word_random_len)
    # Conditional that modifies variable "initial_default_guess" to "True", meaning that the user have won
    if initial_default_guess:
        print ("You have officially won!")
    # If user runs out of attemps, "guessed" remains as "false" hence game over
    else:
        print ("Sorry, you've lost. The secret word was " + secret_word)



# Function below updates the underscores,
def word_underscores (guess_by_user,secret_word,word_random_len):
    update_word_underscores = ""
    for i in range(len(secret_word)):
        # Selects one character from the string to encrypt. Being a loop "for", it takes one character at the time
        letter_to_check = secret_word[i]
        current_character = word_random_len[i]
        # if the current character is already a "letter" it will keep it as is
        # it will enter this conditional after the second time the user do guess a correct letter
        if current_character != "_":
            character_to_print = current_character
            update_word_underscores += character_to_print
        # if the guess of the user is similar to the letter to check in the secret word AND that character still has
        # an underscores, then it will update such character to shown the guessed letter by the user
        elif guess_by_user == letter_to_check and current_character == "_":
            character_to_print = letter_to_check
            update_word_underscores += character_to_print
        # all other cases would go to the else
        else:
            character_to_print = "_"
            update_word_underscores += character_to_print
    return(update_word_underscores)


#Function below is the master one.
def master():
    print ("Welcome to the 'Jeu du Pendu'")
    # Asks the user for the name of the TXT file. It should include the extension .txt
    # intended to allow user to change or update the "file" containing random words
    # All words is the reference file shall be lower case
    file_name = input("First, please type the txt file name (including the .txt extension) containing secrets words: ")
    secret_word = word_to_guess(file_name)
    #secret_word = "bebea"
    gameplay(secret_word)


master()
