## Input an intereger between min and max values (10,40)
## 3 chances to guess correct num
## if guess corect then print Correct!!
# if wrong print wrong!!
# print game over after 3rd guess
import random
# num = random.randint(10, 40)


# for guesses in range(3):
#     guess = int(input("Guess a number between 10 and 40: "))
#     print(guess)
#     if guess == num:
#         print("Correct!")
#         break
#     else: 
#         print("Wrong!")
# print("Game over!")

import random

# Prompt user for minimum and maximum values
min_val = int(input("Enter the minimum value: "))
max_val = int(input("Enter the maximum value: "))
num_guesses = int(input("Enter the number of guesses: "))

# Generate random number between min and max values
num = random.randint(min_val, max_val)

# Allow user to make specified number of guesses
for guesses in range(num_guesses):
    guess = int(input("Guess a number between {} and {}: ".format(min_val, max_val)))
    if guess == num:
        print("Correct!")
        break
    else: 
        print("Wrong.. guess again..")
        if guesses == num_guesses-1:
            print("Game Over.")
        if abs(guess-num) < 5:
            print("Hot")
        else:
            print("Cold")
