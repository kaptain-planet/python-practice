
usremail = str(input("Please enter your email address here: "))

for ch in usremail:
    if ch == "@":
        break
    print(ch, end="")
