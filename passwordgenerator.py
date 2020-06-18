'''
Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.

Examples:
# including the string module in our file
import string

# string.ascii_letters returns all upper and lower capital letters
letters = string.ascii_letters

print(letters)
# outcome: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
'''


#Modules
import random
import string

#Variables
password = ""
letters = string.ascii_letters
user_choice = int(input("What length would you like your random password to be? "))

#Logic
i = 0
while i < user_choice:
    i += 1
    password += random.choice(letters)
else:
    print(password)
