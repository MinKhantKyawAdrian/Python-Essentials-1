#Sorting a list
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
 
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)

# Bubble sort interactive

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = int(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

#python's buil-in funtion sort() and reverse()
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]
 
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

# reverse() does not sort the list. It simply flips the order.
a = "A"
b = "B"
c = "C"
d = " "
 
lst = [a, b, c, d]
lst.reverse()
 
print(lst)

# Copying the entire list. Powerful slices
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# the list is empty because python only move forward left to right
# [start:end] -1 index already at the end, it cannot move right anymore 
# cannot reach to index 1
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

#my_list[0:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

#my_list[start:len(my_list)]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

#deleting all the elements in list
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#delete the list

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)

#creating new list without repetition numbers: 
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for number in my_list:
    if number not in new_list:
        new_list.append(number)

print("The list with unique elements only:")
print(new_list)
