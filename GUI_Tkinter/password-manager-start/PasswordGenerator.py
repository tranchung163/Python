#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_letters = random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

password_list = [letters[i] for i in range(nr_letters) ] + [numbers[i] for i in range(nr_symbols)]+ [symbols[i] for i in range(nr_symbols)]
random.shuffle(password_list)
passwords_str = ""
for i in password_list:
  passwords_str = passwords_str + i
print(passwords_str)

# passwords_list = []
# for letter in range(nr_letters):
#   random_letters = random.randint(0, len(letters)-1)
#   passwords = passwords + letters[random_letters]

# for symbol in range(nr_symbols):
#   random_symbold = random.randint(0,len(symbols) - 1)
#   passwords = passwords + symbols[random_symbold]

# for number in range(nr_numbers):
#   random_numbers = random.randint(0,len(numbers) - 1)
#   passwords = passwords + numbers[random_numbers]


# for i in passwords:
#   passwords_list.append(i)
# random.shuffle(passwords_list)

# passwords_str = ""
# for i in passwords_list:
#   passwords_str = passwords_str + i


  
