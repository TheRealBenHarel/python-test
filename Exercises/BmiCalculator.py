
#This calculator will receive your height and weight and calculate your BMI

height = input("Hello and welcome to the BMI calculator.\nPlease enter your height in meters:\n")
float_height = float(height)

while float_height > 3:
    print("Please enter your height in meters, not cm:\n")
    height = input()
    float_height = float(height)

weight = input("Now please enter your weight in kg:\n")
float_weight = float(weight)
bmi = str(round(float_weight/(float_height**2), 3))
print("Your BMI is: " + bmi)
