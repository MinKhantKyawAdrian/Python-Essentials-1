#combine text and variables using the + operator
var = "3.8.5"
print("Python version: " + var) #using + operator work because both are string

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print("Total number of apples:", total_apples) #need to use "," because of str and integer
#change inter with str so can use + operator
total_apples = john + mary + adam
print("Total number of apples: " + str(total_apples)) 

#Variables ‒ a simple converter

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
#round means take decmial places
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 3), "miles")

USD = 12.25
EUR = 7.38

usd_to_eur = USD / 1.12
eur_to_usd = EUR * 1.12

print(USD, "USD is", round(usd_to_eur, 3), "EUR" )
print(EUR, "EUR is", round(eur_to_usd, 4), "USD")

#Operators and expressions 

x = 0
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x -1 
print("y =", y)

seat = None
guest = None
 
both_empty = seat is None and guest is None

print('seat =', seat)
print('guest =', guest)
print('both_empty :', both_empty)