# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = weight / height ** 2
print(f'BMI - {bmi:.2f}')

if bmi < 18.5:
    print(f"BMI - {bmi:.2f}, you are underweight.")
elif bmi < 25:
    print(f"BMI - {bmi:.2f}, you have a normal weight.")
elif bmi < 30:
    print(f"BMI - {bmi:.2f}, you are slightly overweight.")
elif bmi < 35:
    print(f"BMI - {bmi:.2f}, you are obese.")
else:
    print(f"BMI - {bmi:.2f}, you are clinically obese.")
