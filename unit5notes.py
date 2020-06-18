# The syntax of a dictionary: variable_name = {key: value}

# you can create an empty dictionary
employee_availability = {}

# or initialize a dictionary that contains data

employee_availability = {
"lisa": "Mon", # string
"al": ["Tues", "Wed", "Thurs"], # list
"anthony": ["Mon", "Tues", "Wed", "Thurs", "Fri"] # list
}
# keys: "lisa", "al", "anthony"
# value: "Mon", ["Tues", "Wed", "Thurs"], ["Mon", "Tues", "Wed", "Thurs", "Fri"]

# how many days will Al work in a year?
# 365 days divided by the len of Al's list of availability (3)
worked_days = 365 / len(employee_availability["al"])
print(worked_days)
