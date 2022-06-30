
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

usrnum = int(input("Please enter a number: "))

while usrnum != secret_number:
    print("Ha ha! You're stuck in my loop!")
    usrnum = int(input("Please enter a number: "))
else:
    print("\nWell done, muggle! You are free now.\n")

print("See ya next time!")
