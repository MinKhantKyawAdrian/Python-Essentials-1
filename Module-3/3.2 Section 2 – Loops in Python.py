secret_number = 777
#use triple quotes to print strings on multiple lines 
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

number = int(input("Guess the secret number: "))

while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("Guess the secret number: "))
    
print("Secret nmuber is:",number) 
print("Well done, muggle! You are free now.")

#time count
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

secret_exit_word = "chupacabra"

while True:
    word = input("Enter a secret exit word: ")
    if word != secret_exit_word:
        continue
    print("You've successfully left the loop.")
    break

#Alternative way

secret_exit_word = "chupacabra"

word = input("Enter a secret exit word: ")

while word != secret_exit_word:
    print("Ha ha! You're stuck in my loop!")
    word = input("Enter a word: ")

    if word == secret_exit_word:
        print("You've successfully left the loop.")
        break   

#the Vowel Eater

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter, end='')

#Collatz's hypothesis

c0 = int(input("Enter any non-negative and non-zero integer number: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("Steps = ", steps)

