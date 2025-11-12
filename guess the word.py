"""
Pseudocode:
1. Import random

2. Set max_attempts, wins, and losses to 0

3. Function: choose_difficulty_level:

    A. Globalize max attempts

    B. Print levels and the number of tries

    C. Create while loop

    D. Prompt user to choose a difficulty level

    E. Set max attempt based on users choice of difficulty level

    F. If user doesn’t enter easy, medium, or hard print error  message and prompt them to reenter
4. Function: choose_category:

    A. Set list of animals, foods, sports

    B. Create a while loop

    C. return value of category that user chooses

5. Function: Keep_score:

    A. Globalize wins and losses

    B. Increment wins if user wins game

    C. Increment losses if user loses game

6. Function: pick_random_word:

    A. Create a secret word according to chosen category each round using random.choice

    B. Return value so it can be used in game

7. Function: User_input:

    A. Create a while loop
    
    B. Prompt user to enter a letter

    C. Strip the users input and make it case insensitive

    D. Raise ValueError if more than one letter entered or character is not from alphabet

    E. Validate user input using try/except

8. Function print_status:

    A. Print guessed word

    B. Print the amount of remaining attempts

    C. Print a list of letters that the user guessed already

9. Function: fill_in_letters:

    A. Create a for loop

    B. Use enumerate to assign a number to each character

    C. If the character is the same as the guessed letter, switch the _ to that letter

10. Function: game:

    A. Assign category to category chose in choose_category

    B. Assign word to secret word by using the pick_random_word function

    C. Set attempts to 0

    D. Create an empty list of letters

    E. Set guessed word to the amount of underscores in the secret word

    F. Create a while loop

    G. Assign guessed letter to validate user input

    H. If the guessed letter was already guessed, print message and continue

    I. Otherwise, add guessed letter to list of letters.

    J. Call fill_in_letters

    K. If the guessed letter is not in the secret word, increment attempts

    L. Set remaining attempts to max attempts – attempts

    M. Call print_status function

    N. If there are no underscores left in guessed_word, print you won and break from loop

    O. If there are still underscores in guessed_word and there are no attempts remaining, print no more attempts remaining.

    P. Call keep_score

    Q. Prints wins and losses

11. Function: play_again:

    A. Create while loop

    B. Call choose_diificulty_level

    C. Call game()

    D. Create another while loop

    E. Ask user if they would like to play again

    F. If user enters y, break

    G. If user enters n, return

    H. Otherwise print message


reflection:

In the beginning, my game function was very long and had many parts, which made it hard to read and understand.
I split it into a few smaller functions, such as validate_user_input, fill_in_letters, and print_status, which made the code much clearer and easier to use.
I validated user input using try and except.
I checked that the users input was a single letter from the alphabet with len() and .isalpha().
I also handled repeated guesses by warning the user without adding an attempt.
One feature I added midway was the option to choose a category which makes the game more fun.
This gave th euser an oppurtunity to pick the topic that interests them. 
If I had more time, I would break the game function into even smaller functions and possibly add the hint,
which reveals one random unguessed letter at the cost of two attempts.
This would make it less frustrating for the user if they are having trouble figuring out the word. 

"""

import random

max_attempts = 0
wins = 0
losses = 0
  
def choose_difficulty_level():
  """
  Allows user to choose a level of difficulty according to the number of tries.
  """
  global max_attempts
  print("Easy: 10 tries  Medium: 8 tries  Hard: 6 tries")
  while True:
    difficulty_level = input("Enter Easy, Medium, or Hard: ").strip().lower()

    if difficulty_level == "easy":
      max_attempts = 10
      break
    elif difficulty_level == "medium":
      max_attempts = 8
      break
    elif difficulty_level == "hard":
      max_attempts = 6
      break 
    else:
      print("you did not enter easy, medium, or hard. Please reenter your choice.")

def choose_category():
  animals = ["zebra", "horse", "lion", "tiger", "puppy", "cat", "snake"]
  foods = ["pizza", "sushi", "bread", "cake", "carrot", "soup", "cereal"]
  sports = ["tennis", "hockey", "baseball", "basketball", "soccer", "football"]
  
  while True:
    category_choice = input("Choose a category: (animals, foods, sports)").strip().lower()
    if category_choice == "animals":
      return animals
    elif category_choice == "foods":
      return foods
    elif category_choice == "sports":
      return sports
    else:
      print("Category is invalid. Please try again.")
      
def keep_score(guessed_word):
  """
  Keeps score of wins and losses based on the game results.
  """
  global wins, losses # Globalizes wins and losses. 
  if "_" not in guessed_word:
      wins += 1 # If user wins, adds one point to wins.
  else:
    losses += 1 # if user loses, adds one point to losses. 
 

def pick_random_word(category):
  """
  Chooses a random word each game from given list.
  """
  secret_word = random.choice(category) # Picks a random word from the list of words. 
  return secret_word 

def validate_user_input():
  """
  Validates user input to make sure it's only one letter from alphabet.
  """

  while True:
    try:
      guessed_letter = input("Enter a letter: ").strip().lower() # Prompts user to enter a letter.

      if not (guessed_letter.isalpha()) or (len(guessed_letter) != 1): # VaueError is raised if user does not enter a letter or user enters more than one letter
        raise ValueError
      return guessed_letter # guessed_letter is returned so it can be used in another function. 
      
    except ValueError:
      print("Invalid input. Please enter only one letter from A-Z.")

def print_status(guessed_word, remaining_attempts, list_of_letters):
  """
  Prints guessed word, remaining attempts, and a list of letters that the user guessed.
  """
  print(guessed_word)
  print(f"You have {remaining_attempts} attempts left.")
  print(list_of_letters)

def fill_in_letters(guessed_letter, secret_word, guessed_word):
  """
  Switches _ to letters if the letter is in the word.
  """
  for index, character in enumerate(secret_word): # Gives a number to each character.
      if character == guessed_letter:
          guessed_word[index] = guessed_letter # Switches the _ at that index to the letter
  
def game():
  """
  Runs a single round of hangman.
    1. Chooses a random word from list of words.
    2. Checks if user still has remaining attempts.
    3. Prompts user to enter a letter and validates input. 
    4. Adds letter to list of letters if applicable.
    5. Calculates user's wins and losses according to game results.

  """
  category = choose_category()
  secret_word = pick_random_word(category)
  attempts = 0
  list_of_letters = []
  guessed_word = ["_"] * len(secret_word)

  while attempts < max_attempts: # This function will loop as long as the number of attempts is less than the max attmepts. 
      guessed_letter = validate_user_input()

      if guessed_letter in list_of_letters: 
         print("you already guessed that letter.")
         continue

      list_of_letters.append(guessed_letter) # Appends letter to list of letters.

      fill_in_letters(guessed_letter, secret_word, guessed_word)  

      if guessed_letter not in secret_word:
        attempts += 1
      
      remaining_attempts = max_attempts - attempts
      print_status(guessed_word, remaining_attempts, list_of_letters)


      if "_" not in guessed_word:
        print("You won!")
        break

  
  if '_' in guessed_word and attempts >= max_attempts:
    print("No more attempts remaining")

  keep_score(guessed_word)
  print(f"wins: {wins}")
  print(f"losses: {losses}\n")


def play_again():
  """
  After game is over, it will ask the user if they would like to play another round.
  """
  while True:
    choose_difficulty_level()
    game()
    while True:
        user_input = input("Would you like to play another round? (y/n) ").strip().lower()
      
        if user_input == "y":
          break
      
        elif user_input == "n":
          print("Game over")
          return

        else:
          print("you did not enter 'y' or 'n'")

play_again()


  




