'''
-Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirty room.

-Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.
    -check letters in each password

Convert the strings into lists (list)
Sort the letters of each word (sort)
Check if the two are equal
>>> enter the first word: dormitory
>>> enter the second word: dirtyroom
>>> 'dormitory' and 'dirtyroom' are anagrams
'''


one = input("Please enter a word: ")
two = input("Please enter another word: ")
print(one.lower(), two.lower())
print(sorted(one.lower()), sorted(two.lower()))
if sorted(one.lower()) == sorted(two.lower()):
    print(f"{one} and {two} are anagrams")
else:
    print(f"{one} and {two} are not anagrams")



'''
Advanced Version 1:
-Convert each word to lower case (lower)
-Remove all the spaces from each word by replacing them with empty strings (replace)

def say_hello(name, rsvp="Maybe?"):
  print(f"{name} has a plus one? {rsvp}")
name = "Bob"
say_hello(name, "yes")

# A simple Python function to check whether x is even or odd
def evenOdd( x ):
    if (x % 2 == 0):
        print "even"
    else:
        print "odd"

# Driver code
evenOdd(2)
evenOdd(3)
'''

def anagram(word):
    word = word.lower().replace(" ", "")
    return word

def sort_word(word):
    word = list(word)
    word.sort()
    word = str(list_word)
    return word
one = input("Please enter a word: ")
two = input("Please enter another word: ")
anna1 = annagram(one)
anna2 = annagram(two)

sorted_anna1 = sort_word(anna1)
sorted_anna2 = sort_word(anna2)
print(one, two)
print(anna1, anna2)

if sorted_anna1 == sorted_anna2:
    print(f"{one} and {two} are anagrams")
else:
    print(f"{one} and {two} are not anagrams")
