"""Instructions
Let's write a program to simulate the classic "Magic Eight Ball"

-Print a welcome screen to the user.
    - print()
-Prompt the user to ask the 8-ball a question.
    - input()
    -For example: "Will I win the lottery tomorrow?"
-Use the random module's random.choice() to choose a prediction.
    - import random
Display the result of the prediction.
    - print()
"""



# Modules
import random

# Variables
question = input("Please ask a Yes/No style question.")
responses = [
"It is certain",
"It is decidedly so",
"Without a doubt",
"Yes - definitely",
"You may rely on it",
"As I see it, yes",
"Most likely",
"Outlook good",
"Yes",
"Signs point to yes",
"Reply hazy, try again",
"Ask again later",
"Better not tell you now",
"Cannot predict now",
"Concentrate and ask again",
"Don't count on it",
"My reply is no",
"My sources say no",
"Outlook not so good",
"Very doubtful"
]
chosen_response = random.choice(responses)
print(chosen_response)
# Logic
print("Welcome to the Magic 8 Ball Game!")
