
height = float(input("Enter your height."))
weight = float(input("Enter your weight."))

if height > 3:
    raise ValueError("Human height should not exceed 3 metres!")

if weight < 25:
    raise ValueError("Please check your weight!")

bmi = weight/height**2

print(f"Your BMI: {bmi}")


