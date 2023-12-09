print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name1_score = 0
name2_score = 0

combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = str(t + r + u + e)
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = str(l + o + v + e)
love_score = int(first_digit + second_digit)

print()
if love_score < 10 or love_score > 90:
    print(f"Your  score is {love_score}, you go together like Coke and Mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your  score is {love_score}, you are alright together.")
else:
    print(f"Your  score is {love_score}")