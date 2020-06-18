'''
Goal: convert a number grade (int) to a letter grade (str)
Method: using if and elif statements and comparisons.

-Have the user enter a number representing the grade (0-100)
    - input()
-Convert the number grade to a letter grade
    - if/elif to compare
    Numeric Ranges
    90 - x - 100: A
    range of 80-89 = B
    70-79: C
    60-69: D
    0-59: F
'''


# Variables
print("Welcome to the score converter.")
student_score = int(input("What is your score? (0-100)")) #message
#input is always saved as a String

# Logic
if student_score >= 90 and student_score <= 100:
    print("A")
elif student_score >= 80 and student_score < 90:
    print("B")
elif student_score >= 70 and student_score < 80:
    print("C")
elif student_score >= 60 and student_score < 70:
    print("D")
elif student_score >= 0 and student_score < 60:
    print("F")
else:
    print("Your score must be in the range of 0-100")
