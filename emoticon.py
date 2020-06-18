'''
Goal: generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

-Define a list of eyes
-Define a list of noses
-Define a list of mouths
-Randomly pick a set of eyes
-Randomly pick a nose
-Randomly pick a mouth
-Assemble and display the emoticon


import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
print(fruit)
'''

# Modules
import random

# Variables
eyes = ['blue eyes', 'green eyes', 'brown eyes']
nose = ['narrow nose', 'wide nose']
mouth = ['small mouth', 'wide mouth']
# chosen_eyes = random.choice(eyes)
# chosen_nose = random.choice(nose)
# chosen_mouth = random.choice(mouth)
# print(f"\n{chosen_eyes} \n{chosen_nose} \n{chosen_mouth}")

# Logic
i = 0
while i < 5:
    chosen_eyes = random.choice(eyes)
    chosen_nose = random.choice(nose)
    chosen_mouth = random.choice(mouth)
    print(f"\n{chosen_eyes} \n{chosen_nose} \n{chosen_mouth}")
    i += 1
