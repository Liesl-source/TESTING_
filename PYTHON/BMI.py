Height= float(input("Enter your height in centimeters:"))
Weight= float(input("Enter your weight in kilograms:"))
Bmi= Weight / (Height/100)**2
print (f"Your Bmi is {Bmi}")
if Bmi <= 18.5:
    print("You are underweight...")
elif Bmi <= 24.9:
    print("You are normal weight :)")
elif Bmi <= 29.9:
    print("You are overweight!")
elif Bmi <= 34.9:
    print("You are obese...")
else:
    print("You are severly obese...please exercise!!!")