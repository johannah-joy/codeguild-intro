'''
-The computer will ask the user for their choice (rock, paper, scissors)
    input()
-The computer will randomly choose rock, paper or scissors
    import random
    make a list: rock, paper, scissors
-Determine who won and tell the user
    use if/elif statements to determine winner
All the cases:
rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors
'''


# Modules
import random

# Variables
# outcomes = ['rock', 'paper', 'scissors']
again = 'yes'

# Logic
while again == "yes":
    player = input("Type rock, paper, or scissors: ").lower()
    outcomes = ['rock', 'paper', 'scissors']
    computer = random.choice(outcomes)
    print(computer)
    if player == computer:
        print('Tie')
    elif player == 'rock' and computer == 'paper':
        print('Sorry, you lost')
    elif player == 'rock' and computer == 'scissors':
        print('You won!')
    elif player == 'paper' and computer == 'rock':
        print('You won!')
    elif player == 'paper' and computer == 'scissors':
        print('Sorry, you lost')
    elif player == 'scissors' and computer == 'rock':
        print('Sorry, you lost')
    elif player == 'scissors' and computer == 'paper':
        print('You won!')
    again = input("Would you like to play again? ")
else:
    print("Thanks for playing!")



'''
# print friendly msg
print(f"{player_choice} vs. {computer_choice}")

if player_choice == computer_choice:
    print("it's a tie")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("you lose")
    else:
        print("you win")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("you win")
    else:
        print("you lose")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("you lose")
    else:
        print("you win")
else:
    print("Invalid input.")
'''


'''
# Modules
import random

# Variables
choices = ["rock", "paper", "scissors"]
player_lose = ["rock vs paper", "paper vs scissors", "scissors vs rock"]
player_win = ["rock vs scissors",   "paper vs rock", "scissors vs paper"]
# ties = ["paper vs paper", "rock vs rock", "scissors vs scissors"]

# Logic

# ask user for input
player_choice = input("Rock, paper, or scissors?").lower()

# computer randomly chooses
computer_choice = random.choice(choices)
outcome = player_choice + " vs " + computer_choice

# print friendly msg
print(outcome)
if player_choice == computer_choice:
    print("it's a tie")
elif outcome in player_win:
    print("You win!")
elif outcome in player_lose:
    print("You lose!")
else:
    print("Invalid input.")
'''


'''
while player_choice not in choices:
    player_choice = input("Invalid input. Rock, paper, or scissors?").lower()
else:
    # create outcome variable
    outcome = player_choice + " vs " + computer_choice
    # print friendly msg
    print(outcome)
    if player_choice == computer_choice:
        print("it's a tie")
    elif outcome in player_win:
        print("You win!")
    else:
        print("You lose!")
'''
