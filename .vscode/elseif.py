from time import sleep
from math import pi
shape=input("choose shape: ")
if shape=="circle" or "c" or C:
    radius=int(input("enter radius: "))
    area=pi * radius**2
    print(f"area = {area}")

elif shape=="rectangle" or "r" "R":
    length=int(input("enter length: "))
    width=int(input("enter width: "))
    area=length*width
    print(f"area = {area}")

elif shape=="triangle" or "t" or "T":
    base=int(input("enter base: "))
    height=int(input("enter height: "))
    area=height*base
    print(f"area = {area}")

else:
    print("wrong shape")