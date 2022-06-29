#!/usr/bin/env python

__author__      = "kaptain planet"


print("What is your favorite flower? Spathiphyllum or spathiphyllum\n")

optionA = 'Spathiphyllum'
optionB = 'spathiphyllum'

name = input('Please Enter flower name: ')

if name == optionA:
  print('Yes - Spathiphyllum is the best plant ever!')
elif name == optionB:
  print('No, I want a big Spathiphyllum!')
else:
  print('Spathiphyllum! Not', name + '!')

print('\nThanks for playing!')
