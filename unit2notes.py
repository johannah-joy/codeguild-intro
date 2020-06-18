fruits = [] # empty list OR
fruits = ["apple", "banana", "cherry"] # initialized list with three items
print(fruits) #outcome: ["apple", "banana", "cherry"]

# print the item at this index position
print(fruits[0]) #outcome: "apple"
print(fruits[1]) #outcome: "banana"
print(fruits[2]) #outcome: "cherry"
print(fruits[-1]) #outcome: "cherry" (last item in list)
print(fruits[-3]) #outcome: "apple"
print(fruits[-4]) #outcome: "list index out of range"

fruits.append("kiwi")
print(fruits) #outcome: "['apple', 'banana', 'cherry', 'kiwi']"
fruits.insert(1, "watermelon")
print(fruits) #outcome: "['apple', 'watermelon', 'banana', 'cherry', 'kiwi']"

# for each item in the fruit list, print the item and its index
for fruit in fruits:
  print(f"{fruit} has an index of {fruits.index(fruit)}")


# include the random module in our file
import random

# a list of fruits
fruits = ["apple", "banana", "cherry"]

# randomly choose a fruit and save it to a variable, chosen_fruit
# choice() is a function inside the random module. we use it by writing random.choice()
# the list in which you want the program to choose from, needs to go inside the parenthesis of choice()
chosen_fruit = random.choice(fruits)

# print the value of variable chosen_fruit
print(chosen_fruit)
print(random.choice(fruits))



x = 1 # integer
y = 2.8 # float

# what is their datatype?
print(type(x)) # outcome: integer
print(type(y)) #outcome: float

#converting an int to a float
float_x = float(x)
print(float_x)

#converting an float to an int
int_x = int(float(x))
print(int_x)

print(int(24/4)) # to get output of 6 rather than 6.0 **6.0 outcome would come from print(24/4)


# PYTHON OPERATORS

# Modulus
remainder = 8%3
print(remainder)

# Exponential
ex_result = 5**3
print(ex_result)

# Floor Division
floor_d = 8//3
print(floor_d)

# Comparison Operators
x = 3
y = 7
# ==  Equal
print("Does 3 equal 7?")
print(x == y) # outcome: False
# !=  Not equal
print("Is it true that 3 does not equal 7")
print(x != y) # Outcome: True
# > Greater than
print("Is 3 greater than 7?")
print(x > y) # Outcome: False
# < Less than
print("Is 3 less than 7?")
print(x < y) # Outcome: True
# >=  Greater than or equal to
print("Is 3 greater than OR equal to 7?")
print(x >= y) # Outcome: False
# <=  Less than or equal to
print("Is 3 less than OR equal to 7?")
print(x <= y) # Outcome: True

# if/else
x = 7
y = 7
### if/else statement
# print(x == y)
if x == y: # if statement True
  # run this line
  print("The numbers are equal!")
else: # statement is False
  # run this line
  print("The numbers are NOT equal!")

### if/else
# only checks 2 statements
x = 7
y = 7
### if/else statement
# print(x == y)
if x == y: # if statement True
  # run this line
  print("The numbers are equal!")
else: # statement is False
  # run this line
  print("The numbers are NOT equal!")
### pie example
pie_flavors = ["apple", "pumpkin", "raspberry", "peach", "pecan", "rhubarb", "lemon", "marionberry", "blackberry"]
print("Welcome to our pie shop!")
print("\nHere are our pie flavors:")
for pie in pie_flavors:
  print(pie)
customer_order = input("\nWhat would you like to order? ")
### if/else statement to check 2 situations ###
# if customer chooses pumpkin
  # say, "Sorry, we're out"
if customer_order == "pumpkin":
  print("Sorry we're out!")
else:
  print("Great, coming right up!")

### elif example
pie_flavors = ["apple", "pumpkin", "raspberry", "peach", "pecan", "rhubarb", "lemon", "marionberry", "blackberry"]
print("Welcome to our pie shop!")
print("\nHere are our pie flavors:")
for pie in pie_flavors:
  print(pie)
customer_order = input("\nWhat would you like to order? ")
### elif statement to check 2+ situations ###
if customer_order == "pumpkin":
  print("Sorry we're out!")
elif customer_order == "marionberry":
  print("that will be an extra 10 minutes!")
elif customer_order == "apple":
  print("it aint apple season!")
else: # catch all
  print("Great, coming right up!") 
