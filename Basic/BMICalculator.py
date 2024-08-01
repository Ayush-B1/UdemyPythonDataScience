height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kgs: "))

BMI = weight/(height ** 2)

if BMI < 18.5:
    print("you are underweight")
elif 18.5 <= BMI < 25:
    print("you have a normal weight")
elif 25 <= BMI < 30:
    print("you are slightly over weight")
elif 30 <= BMI < 35:
    print("you are obese")
else:
    print("seek help")
