
#This calculator will receive your height and weight and calculate your BMI

height = input("Hello and welcome to the BMI calculator.\nPlease enter your height in meters:\n")
float_height = float(height)

while float_height > 3:
    print("Please enter your height in meters, not cm:\n")
    height = input()
    float_height = float(height)

weight = input("Now please enter your weight in kg:\n")
float_weight = float(weight)
bmi = round(float_weight/(float_height**2), 3)
print(f"Your BMI is: {bmi}")
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are slightly overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")