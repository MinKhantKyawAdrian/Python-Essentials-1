print("Multiplication", a * b)
print("Division", a / b)
print("\nThat's all, folks!")

x = float(input("Enter vlaue of x: "))
y = 1 / (x + 1 / (x + 1 / ( x + 1 / x )))
print("y", y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')