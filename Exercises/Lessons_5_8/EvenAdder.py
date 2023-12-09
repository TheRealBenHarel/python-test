
choice = int(input("Please choose a number between 1 and 1000 (including):\n"))
if choice > 1000 or choice < 1:
    print("The number is not in the required range...")
    exit(1)
choice_sum = 0
for i in range(0, choice + 1, 2):
    choice_sum += i
print(f"The sum is {choice_sum}")
