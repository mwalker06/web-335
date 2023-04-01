
 # Title: bill.js
 # Author: Megan Walker
 # Date: 04/01/23
 # Description: calculator.py for Web 335 Assign_3
 # References: WEB 335 GitHub, & WEB 335 Assign_3,

# Create a function named add with two parameters and in the body of the method return the total
def add(num1, num2):
    return num1 + num2

# Create a function named subtract with two parameters and in the body of the method return the total
def subtract(num1, num2):
    return num1 - num2

# Create a function named divide with two parameters and in the body of the method return the total
def divide(num1, num2):
    return num1 / num2

# Create a function named multiply with two parameters and in the body of the method return the total
def multiply(num1, num2):
    return num1 * num2

# Create variables to test each function
num1_add = 4
num2_add = 4

num1_subtract = 10
num2_subtract = 6

num1_divide = 8
num2_divide = 2

num1_multiply = 10
num2_multiply = 2

# Use a variable to build a string for the results
addition_result = "{} + {} is {}".format(num1_add, num2_add, add(num1_add, num2_add))
subtraction_result = "{} - {} is {}".format(num1_subtract, num2_subtract, subtract(num1_subtract, num2_subtract))
division_result = "{} / {} is {}".format(num1_divide, num2_divide, divide(num1_divide, num2_divide))
multiplication_result = "{} * {} is {}".format(num1_multiply, num2_multiply, multiply(num1_multiply, num2_multiply))

# Print the results of each arithmetic operation to the console
print(addition_result)
print(subtraction_result)
print(division_result)
print(multiplication_result)
