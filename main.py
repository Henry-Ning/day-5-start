#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#1 password string variable
#2 add 4 letters, 2 symbols, 2 numbers to password

password = []
password_len = nr_letters + nr_symbols + nr_numbers

for n in range(1, nr_letters+1):
  password.append(letters[random.randint(0, len(letters)-1)])

for n in range(1, nr_symbols+1):
  password.append(symbols[random.randint(0, len(symbols)-1)])

for n in range(1, nr_numbers+1):
  password.append(numbers[random.randint(0, len(numbers)-1)])

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_password = []
for n in range(1, password_len+1):
  added_character = password[random.randint(0, len(password)-1)]
  random_password.append(added_character)
  password.remove(added_character)

print(random_password)

final_password = ""
for n in range(0, password_len):
  final_password = final_password+random_password[n]

print(final_password)