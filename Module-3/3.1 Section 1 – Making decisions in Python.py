n = int(input("Enter number: "))
print( n >= 100 )

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
 
largest_number = max(number1, number2, number3) #max is built-in function for find maximum number
smallest_number = min(number1, number2, number3) #min is built-in function for find minimum number
 
print("The largest number is:", largest_number)
print("The samllest number is:", smallest_number)

# Comparison operators and conditional execution

name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")

#Essentials of the if-else statement

income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else: 
    tax = 14839.02 + (income - 85528) * 0.32

if tax < 0.0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#Essentials of the if-elif-else statement

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")

