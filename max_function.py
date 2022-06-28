#!/usr/bin/env python

__author__      = "kaptain planet"

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

largest_number = max(number1, number2, number3) # using max function

# Print the result.
print("The largest number is:", largest_number)
