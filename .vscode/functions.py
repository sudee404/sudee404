#calculates area of any shape given
from math import pi,pow

def tarea(h,b):
    print(0.5*h*b)

def carea(r):
    print(pi*pow(r,2))

def sarea(s):
    print(pow(s,2))

def rarea(l,w):
    print(l*w)

def setShape():
    shapes=["rectangle","square","triangle","circle"]
    choice=input("enter name of shape:")
    if choice==shapes[0]:
        x=int(input("enter length: "))
        y=int(input("enter width: "))
        print(rarea(x,y))
    elif choice==shapes[1]:
        x=int(input("enter side: "))
        print(sarea(x))
    elif choice==shapes[2]:
        x=int(input("enter height: "))
        y=int(input("enter base: "))
        print(tarea(x,y))
    elif choice==shapes[3]:
        x=int(input("enter radius: "))
        print(carea(x))
    else:
        print("invalid shape")

setShape()