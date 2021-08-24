from math import pow
weight=int(input("enter your weight: "))
height=float(input("enter your height: "))
bmi=weight/(pow(height,2))
if bmi<18.5:
    print("Underweight")

elif bmi>=18.5 and bmi<25:
    print("Normal")

elif bmi>=25 and bmi<30:
    print("Overweight")

else:
    print("Obesity")