numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###

numbers = [111, 7, 2, 1] #An element with an index equal to -1 is the last one in the list.
print(numbers[-1])

#The basics of lists

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
print("Original hat list", hat_list)

# Step 1: write a line of code that prompts the user
user = int(input("Enter a number: "))

# to replace the middle number with an integer number entered by the user.
hat_list[2] = user

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print("Lenght of hat list:", len(hat_list))

print(hat_list)
