#!/usr/bin/env python

__author__      = "kaptain planet"


income = float(input("Enter the annual income: "))

# Write your code here.
threshold = 85528

if income <= threshold:
    tax = (income * 0.18) - 556.2 # tax relief
elif income > threshold:
    tax = 14839.2 + (income - threshold)*0.32

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("\nThe tax is:", tax, "thalers")
