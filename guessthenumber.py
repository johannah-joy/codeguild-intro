'''
- The computer will choose a random int between 1 and 10
    - import random
    for x in range(1)
            print random.randint(1,11)
- The user will then try to guess the number
    - input()
- The program will tell them whether they're right or wrong
    - print()
'''

# Modules
import random

# Variables
user_input = int(input("Guess the number that the computer will randomly generate 1-10: "))
computer = random.randint(1,10)

# Logic
print(computer)
if user_input == computer:
    print("You guessed correctly!")
elif user_input > computer:
    print("Sorry, your guess too high.")
else:
    print("Sorry, your guess is too low.")
        # comp_score +=1
    # again = input("Would you like to play again? ").lower()
# else:
#     print(f"Final Score: Player {user_score}, Computer {comp_score}.")
