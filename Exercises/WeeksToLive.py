
#This program will receive the user's age and will output the number of weeks the user has got left


age = input("Hello, please enter your age:\n")
total_weeks = 52*90
int_age = (int(age))
weeks_left = total_weeks - int_age*52
print(f"The number of weeks you have left is {weeks_left}")