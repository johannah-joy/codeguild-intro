'''Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

what is the distance in feet? 12
12 ft is 3.6576 m
'''


# #Modules
# from decimal import Decimal
#
# #Variables
# user_input = int(input("How many feet do you want to convert to meters? "))
# x = Decimal(0.3048 * user_input)
# meters = round(x,4)
#
# #Logic
# print(f"{user_input} feet is {meters} meters.")



'''
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
1 yard is 0.9144 m
1 inch is 0.0254 m
'''


#Modules

#Variables
distance = int(input("What is the distance? "))
units = input("What is the unit (ft, mi, m, km, yd, in)? ")
conversion = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}

#Logic
x = conversion[units] * distance
print(x)
