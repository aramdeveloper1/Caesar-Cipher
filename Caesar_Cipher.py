# def add_time(start, duration, starting_day=None):
#     # Days of the week to handle optional day input
#     days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     # Parse the start time
#     start_time, period = start.split()  # e.g., "3:00 PM" -> "3:00", "PM"
#     print("start_time ",start_time,"period ", period)
#     start_hour, start_minute = map(int, start_time.split(':'))  # e.g., "3:00" -> 3, 0
#     print("start_hour ",start_hour,"start_minute ", start_minute)
    
#     # Convert to 24-hour format
#     if period == "PM" and start_hour != 12:
#         start_hour += 12  # Convert PM to 24-hour format
#         print("start_hour after adding 12 ",start_hour)
#     elif period == "AM" and start_hour == 12:
#         start_hour = 0  # Midnight is 00 in 24-hour format

#     # Parse the duration
#     duration_hour, duration_minute = map(int, duration.split(':'))  # e.g., "3:10" -> 3, 10
#     print("duration_hour ",duration_hour,"duration_minute ", duration_minute)
#     # Add duration to the start time
#     end_minute = start_minute + duration_minute
#     print("end_minute ",end_minute)
#     print("end_minute // 60 ",end_minute // 60)
#     end_hour = start_hour + duration_hour + (end_minute // 60)  # Handle extra hours from minutes
#     print("end_hour ",end_hour)
#     end_minute %= 60
#     print("end_minute ",end_minute)
#     days_later = end_hour // 24  # How many days later
#     print("days_later ",days_later)
#     end_hour %= 24
#     print("end_hour ",end_hour)

#     # Convert back to 12-hour format
#     if end_hour == 0:
#         new_hour = 12
#         new_period = "AM"
#     elif end_hour < 12:
#         new_hour = end_hour
#         new_period = "AM"
#     elif end_hour == 12:
#         new_hour = 12
#         new_period = "PM"
#     else:
#         new_hour = end_hour - 12
#         new_period = "PM"

#     # Calculate the new day of the week (if given)
#     if starting_day:
#         starting_day_index = days_of_week.index(starting_day.capitalize())
#         new_day_index = (starting_day_index + days_later) % 7
#         new_day = days_of_week[new_day_index]
#     else:
#         new_day = None

#     # Prepare the final result string
#     new_time = f"{new_hour}:{end_minute:02d} {new_period}"

#     if new_day:
#         new_time += f", {new_day}"

#     if days_later == 1:
#         new_time += " (next day)"
#     elif days_later > 1:
#         new_time += f" ({days_later} days later)"

#     return new_time

# # Examples to test the function:
# print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
# print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
# print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
# print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
# print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
# print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)



#***************************************************************************************************#



# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# nr_letters = (input("How many letters would you like in your password?\n"))
# nr_numbers = (input("How many numbers would you like?\n"))
# nr_symbols = (input("How many symbols would you like?\n"))

# if not nr_letters.isdigit() or not nr_numbers.isdigit() or not nr_numbers.isdigit():
#     print("Please enter a number")
# else:
#     password = []

    

#     for i in range(int(nr_letters)):
#         random_letters = random.randint(0,51)
#         password.append(letters[random_letters])
#     print("password with letters:",password)

    
#     for i in range(int(nr_numbers)):
#         random_numbers = random.randint(0,9)
#         password.append(numbers[random_numbers])
#     print("password with numbers:",password)

    
#     for i in range(int(nr_symbols)):
#         random_symbols = random.randint(0,8)
#         password.append(symbols[random_symbols])
#     print("password with symbols:",password)

#     random.shuffle(password)
#     print("".join(password))

#     if password <= 10:
#         print("Your password is too short")
#     elif password == 11:
#         print("it is medium")
#     else:
#         print("it is strong")




# Initialize:
#   Word to guess
#   Number of chances (e.g. 6)
#   Guessed letters
#   Display word (with underscores for unknown letters)
# guess_word = input("Enter a word: ").lower()
# nr_chances = 6
# guessed_letters = []
# display_word = "_" * len(guess_word)
# hungman_gallows = ""

# while nr_chances > 0:
#     guess = input("Guess a letter: ").lower()
#     if guess in guessed_letters:
#         print("You've already guessed that letter. Try again.")
#     else:
#         guessed_letters.append(guess)
#         if guess in guess_word:
#             for i in range(len(guess_word)):
#                 if guess == guess_word[i]:
#                     display_word = display_word[:i] + guess + display_word[i+1:]
#         else:
#             nr_chances -= 1
#             hungman_gallows += "  |  " * (nr_chances - 1)
#             if nr_chances == 1:
#                 hungman_gallows += "  O  "
#             elif nr_chances == 2:
#                 hungman_gallows += " /|  "  
#             elif nr_chances == 3:
#                 hungman_gallows += " / \ "
#             elif nr_chances == 4:
#                 hungman_gallows += " / \ "
#             elif nr_chances == 5:
#                 hungman_gallows += " / \ "
#             elif nr_chances == 6:
#                 hungman_gallows += " / \ "


#     print(display_word)
# While number of chances > 0:
#   Ask user to guess a letter
#   If letter is in word:
#     Update display word with correct letter
#     Remove letter from word
#   Else:
#     Decrement number of chances
#     Draw a part of the hangman's gallows

#   If word is fully guessed:
#     Print "You won!"
#     Exit

#   If number of chances = 0:
#     Print "You lost! The word was [word]."
#     ExitInitialize:
#       Word to guess (randomly select from a list of words)
#       Number of chances (e.g. 6)
#       Guessed letters (empty list)
#       Display word (with underscores for unknown letters)
#       Hangman's gallows (empty string)
    
#     While number of chances > 0:
#       Print display word and hangman's gallows
#       Ask user to guess a letter
#       If letter is in word:
#         Update display word with correct letter
#         Remove letter from word
#         Add letter to guessed letters list
#       Else:
#         Decrement number of chances
#         Add a part to the hangman's gallows
#         Print "Incorrect guess!"
    
#       If word is fully guessed:
#         Print "You won!"
#         Exit
    
#       If number of chances = 0:
#         Print "You lost! The word was [word]."
#         Print hangman's gallows
#         Exit
    
#       If user wants to quit:
#         Print "Thanks for playing!"
#         Exit

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# word_list = [
# 'abruptly', 
# 'absurd', 
# 'abyss', 
# 'affix', 
# 'askew', 
# 'avenue', 
# 'awkward', 
# ]
# import random
# chosen_word = random.choice(word_list)
# print("chosen_word *****",chosen_word)
# word_length = len(chosen_word)
# print("word_length *****",word_length)
# end_of_game = False
# lives = 6

# display = []
# wrong_guesses = []
# for i in range(word_length):
#     display += "_"
# print("display *****",display)


# while not end_of_game:
#     print(not end_of_game)
#     guess = input("guess a letter: ").lower()
#     if guess in wrong_guesses:
#         print(f"{''.join(display)}")
#         print(f"You've already guessed {guess}")
#         print("stage of live remaining:",stages[lives])
#     else:
#         wrong_guesses.append(guess)
#         print("wrong_guesses ",wrong_guesses)
#         for position in range(word_length):
#             letter =chosen_word[position]
#             print("letter ",letter, "guess ",guess)
#             if letter == guess:
#                 display[position] = letter
#         print(f"{''.join(display)}")
     
#         if '_' not in display:
#             end_of_game = True
#             print("You win")
#         if guess not in chosen_word:
#             lives-=1
#             print("lives ",lives)

#         if not end_of_game:
#              print("stages of live remaining:",stages[lives],"lives left", lives)
#         if guess not in chosen_word:
#           print(f"'{guess}' is not in the word, you lost 1 life.")

#         if lives == 0:
#             end_of_game = True
#             print("The man has been hung, you lose.")
#             print(f"\nThe word was '{chosen_word}'")
#********************************************************************************#

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def Caesar_Cipher(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
      if char.isalpha():
       position = alphabet.index(char)
       new_position = position + shift_amount
       end_text += alphabet[new_position]
      else:
        end_text+=char
    
    print(f"The {cipher_direction}d result is: {end_text}")
start_game = True
while start_game:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = shift % 26
    Caesar_Cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
    if choice == 'no':
        start_game = False
        print("Goodbye.")