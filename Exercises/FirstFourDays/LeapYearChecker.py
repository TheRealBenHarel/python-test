#This program will receive a year and will tell whether it's a leap year or not.
year_to_check = int(input("Please enter the year you wish to check:\n"))
if (year_to_check % 4) == 0 and (year_to_check % 400) == 0:
    print("Leap Year")
elif (year_to_check % 4) == 0 and (year_to_check % 100) != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")