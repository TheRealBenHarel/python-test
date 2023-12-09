#This program receives a choice of either rock, paper or scissors, and randomizes a rival response

import random

user_choice = input("Please choose Rock, Paper, or Scissors.\n").lower()
pc_choice = random.randint(0, 2)
if user_choice == "rock":
    user_num = 0
elif user_choice == "paper":
    user_num = 1
elif user_choice == "scissors":
    user_num = 2
else:
    print("You didn't choose one of the three, or you had a typo...\n")
    exit(1)
print(f"PC chose {pc_choice}\n")
if user_num == pc_choice:
    print("It's a tie!")
    exit(1)
elif pc_choice == user_num + 1:
    print("PC wins!\n")
    exit(1)
elif user_num == pc_choice + 2:
    print("PC wins!\n")
    exit(1)
else:
    print("You win!")
    exit(1)
    