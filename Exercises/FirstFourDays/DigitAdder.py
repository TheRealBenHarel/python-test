

#This program receives a two digit number, then prints the sum of the digits

num = input("Please enter your number:\n")
new_num = int(num)

if new_num > 99:
    print("Error! This is not a two digit number!")
    exit(1)
elif new_num < 10:
    print("Error! This is not a two digit number!")
    exit(1)
    

new_first_digit = int(num[0])
new_second_digit = int(num[1])
print(new_first_digit + new_second_digit)

