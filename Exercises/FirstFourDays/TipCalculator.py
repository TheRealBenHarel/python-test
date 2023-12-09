#This program will calculate the amount each person needs to pay, while calculating also the relevant tip


bill = float(input("Welcome to the tip calculator\nWhat was the total bill?\n"))
tip_percent = (float(input("What percentage tip would you like to give?\n"))+100)/100
num_of_people = int(input("How many people to split the bill?\n"))
print(f"Each person should pay: ${round(bill*tip_percent/num_of_people, 2)} ")



