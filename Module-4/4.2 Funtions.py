#Parameterized functions
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")

# Positional parameter passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

#Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

#Mixing positional and keyword arguments
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)
adding(4, 3, c = 2)

#Parametrized functions – more details
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)

introduction("James", "Doe")
introduction("Henry") #last name is already defined
introduction(first_name="William")

def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction() #frist and last name already defined
introduction(last_name="Hopkins") #replace the last name

#An example of a three-parameter function:
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

#positional arguments mustn't follow keyword arguments
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
#subtra(a=5, 2) Syntax Error


