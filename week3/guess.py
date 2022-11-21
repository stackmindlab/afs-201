import random
import math

#SECRET WORD
secret_word = "PLAYSTATION"

#LIST TO STORE THE USERS GUESSES
user_guesses_list = []

#USER CHANCES VARIABLE
user_guesses_list_of_indexes = ""

#WORD BOARD 
wordBoard = ["_"] * len(secret_word)

#RETURNS A RANDOM ELEMENT FROM THE DEFINED WORDS BELOW.
def random_word_generator():
    return 

def show_board():
    #Prints the current board state.
    print(" ".join(wordBoard))

def return_next_index_duplicate(word, letter, board):
    for x in range(len(word)):
        if(board[x] == "_" and word[x] == letter.upper()):
            board[x] = letter.upper()
        
def check_guess(guessed_letter):
    global user_guesses_list_of_indexes
    #user_guesses_list.append(guessed_letter)

    position_of_found_letter = secret_word.find(guessed_letter.upper())

    if(position_of_found_letter == -1):
        return False

    if(str(position_of_found_letter) in user_guesses_list_of_indexes or secret_word.count(guessed_letter) != 1):
        return_next_index_duplicate(secret_word, guessed_letter, wordBoard)
    else:
        #LOGIC FOR THE CORRECT INDEXING OF WORD BOARD AND REPEATING OF LETTERS IN WORD.
        user_guesses_list_of_indexes += str(position_of_found_letter) 
        wordBoard[position_of_found_letter] = guessed_letter
    
    return guessed_letter in secret_word

#Validate the input is a string helper function.
def validate_the_string(letter):
    return type(letter) == str

#Helpoer function to print message to the user.
def message_function(attempt_passed, chances, letter,word = ""):
    if(attempt_passed == 'No'):
        print(f"I'm sorry but there is no letter {letter.upper()} in the word")
        print(f"You have {chances}s left!")
        if(chances <= 0):
            print(f"You Lost. The secret word was {word}")
        else:
            return

def check_for_board_win(word, board):
    #Using list comprehension to fill the returned list.
    return [letter for letter in word if letter] == board

def init():
    player_win = False
    user_chance_variable = 5
    negative_string = "No"
    while(user_chance_variable > 0 and player_win != True ):
        user_guess = input("Can you guess the secret word? ").upper()
        letter_in_secert_word = check_guess(user_guess.upper())
        dict = {"letter_count": secret_word.count(user_guess.upper())}
        
        if(letter_in_secert_word == False):
            if(user_guess in user_guesses_list):
                print(f"You already guessed that letter{user_guess.upper()}")
                continue
            user_chance_variable -= 1
            message_function(negative_string,user_chance_variable, user_guess, secret_word)
            # user_guesses_list.append(user_guess.upper())

        else:
            if(user_guess in user_guesses_list):
                print(f"You already guessed that letter{user_guess.upper()}")
                continue
            if(dict["letter_count"] > 1):
                print(f"""Yes there are {dict["letter_count"]} {user_guess.upper()}'s""")
            else:
                print(f"Yes there is a {user_guess}!")
            show_board()
            
            winner_found = check_for_board_win(secret_word, wordBoard)
            if(winner_found == True):
                player_win = True
                print("You Won the secret word was!")
                print("".join(secret_word))
        user_guesses_list.append(user_guess.upper())
            
init()

     

