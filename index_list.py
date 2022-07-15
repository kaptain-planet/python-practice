
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

print("Numbers in the list: 1, 2, 3, 4, 5\n")
usrnum = int(input("Enter number to replace middle number in the list above: "))

hat_list[2] = usrnum # Store usrnum in hat_list

del hat_list[4] # Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.
print("\nList's length:", len(hat_list))
print(hat_list)
