my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique = []

# Write your code here.
for i in my_list:
    if i not in unique:
        unique.append(i)
print("The list with unique elements only:", unique)
print(my_list)
