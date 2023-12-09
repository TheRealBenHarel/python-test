#This program will decide which of the people on the list will pay for dinner
import random
my_list = ["Ben", "Shir", "Tal", "John", "Maya"]
name_amount = len(my_list)
print(name_amount)

random_person = random.randint(0, name_amount - 1)
print(f"The person who is paying for dinner is: {my_list[random_person]}")




