# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Declare password as empty string
password = []

# Create a range for the nr of letters input and choice a random letter from the letters list
# append value to password list
for i in range(1, nr_letters + 1):
    password.append(random.choice(letters))

# Same process for symbols
for j in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

# Same process for numbers
for k in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

# Use shuffle function to randomize the list and join the elements to create a string
random.shuffle(password)
final_password = ''.join(password)

print(f"Your password is: {final_password}")
