#!/usr/bin/env python

__author__      = "kaptain planet"

secret_word = "chupacabra"

usrword = str(input("Please enter the secret word: "))

while True:
    if usrword == secret_word:
        break
    usrword = str(input("Please enter the secret word: "))
print("You've successfully left the loop.")
