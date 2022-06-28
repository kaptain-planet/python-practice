#!/usr/bin/env python

__author__      = "kaptain planet"

# Read four numbers
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))
number4 = int(input("Please enter the fourth number: "))
fname = input("Please enter your first name: ")

# Assume number1 is the largest and store
largest_number = number1

if number2 > largest_number:
  largest_number = number2
if number3 > largest_number:
  largest_number = number3
if number4 > largest_number:
  largest_number = number4

print("\nThe largest number is:", largest_number)

print("Thanks for playing!", fname)
