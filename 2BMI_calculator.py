weight = "Enter your weight in kg: "
height = "Enter your height in meters: "
weight = float(input(weight))
height = float(input(height))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi :.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
elif bmi < 34.9:
    print("You are obese (Class I).")
elif bmi < 39.9:
    print("You are obese (Class II).")
else:
    print("You are obese (Class III).")