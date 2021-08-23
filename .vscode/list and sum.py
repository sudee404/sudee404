#give program 4 numbers and a sum and it shows which values add  to the sum
nums=[]
i=1
while i<=4:
    x=int(input(f"enter number {i}: "))
    nums+=[x]
    i+=1
tots=int(input("enter sum:"))

for x in nums:
    for y in nums:
        sum=x+y
        if sum==tots:
            print(f"{x} + {y} = {tots}")
            
