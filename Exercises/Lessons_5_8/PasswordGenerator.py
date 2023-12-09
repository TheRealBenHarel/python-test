import random
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o", "p", "q", "r", "s", "t", \
    "u", "v", "w", "x", "y", "z"]
letters_amount = int(input("How many letters would you like in your password?\n"))
symbols_amount = int(input("How many symbols would you like in your password?\n"))
numbers_amount = int(input("How many numbers would you like in your password\n"))

password_length =int(letters_amount + symbols_amount + numbers_amount)
gen_password = []

for place in range(0, symbols_amount):
    gen_password.append(symbols[random.randint(0, len(symbols) - 1)])

for place in range(0, letters_amount):
    upper_lower = random.randint(0, 1)
    if upper_lower == 0:
        gen_password.append((letters[random.randint(0, len(letters) -1)]).upper())
    else:
        gen_password.append((letters[random.randint(0, len(letters) -1)]).lower())

for place in range(0, numbers_amount):
    gen_password.append(str(random.randint(0, 9)))

random.shuffle(gen_password)
str_password = ""
for i in range(0, len(gen_password)):
    str_password += gen_password[i]
print("Your password is: " + str_password)
                                   
            