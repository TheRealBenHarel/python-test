import random


user_choice = input("Welcome to Rock Paper Scissors! Please choose either one and continue:\n").lower()
choice_array = ["rock", "paper", "scissors"]
if choice_array.count(user_choice) == 0:
    print("You either had a typo or you wrote something wrong on purpose... bye bye\n")
    exit(1)
pc_choice = random.randint(0, 2)
user_choice_index = choice_array.index(user_choice)

print(f"PC chose {pc_choice}\n")
if user_choice_index == pc_choice:
    print("It's a tie!")
    exit(1)
elif pc_choice == user_choice_index + 1:
    print("PC wins!\n")
    exit(1)
elif user_choice_index == pc_choice + 2:
    print("PC wins!\n")
    exit(1)
else:
    print("You win!")
    exit(1)  
    
    
    
    
    