from math import pi,pow

shape=["circle","rectangle","square","triangle"]
ushape=input("enter shape: ")

while ushape in shape:
    if ushape==shape[0]:
        r=int(input("enter radius: "))
        a=(lambda x: pi*pow(x,2))(r)
        print(round(a,2))
        break

    elif ushape==shape[1]:
        a=(lambda x,y: x*y)
        l=int(input("enter length: "))
        w=int(input("enter width: "))
        print(round((a(l,w)),2))
        break

    elif ushape==shape[2]:
        a=(lambda x: x*x)
        s=int(input("enter side: "))
        print(round((a(s)),2))        
        break
    elif ushape==shape[3]:
        a=(lambda x,y:x/2*y)
        h=int(input("enter height: "))
        b=int(input("enter base: "))
        print(round((a(h,b)),2))
        break
while not ushape in shape:
    print("wrong shape")
    break