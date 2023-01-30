## Input an intereger between min and max values (10,40)
## 3 chances to guess correct num
## if guess corect then print Correct!!
# if wrong print wrong!!
# print game over after 3rd guess
import random
num = random.randint(10, 40)


for guesses in range(3):
    guess = int(input("Guess a number between 10 and 40: "))
    print(guess)
    if guess == num:
        print("Correct!")
        break
    else: 
        print("Wrong!")
    if guesses == 2:
        print("Game over!")