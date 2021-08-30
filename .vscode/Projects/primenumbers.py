pnums=[]
nums=[]
isprime=True
start=int(input("enter starting point: "))
stop=int(input("enter stopping point: "))
stop+=1
nums=[i*1 for i in range(1,stop)]
for i in range(start,stop):
    for x in nums:
        if i%x==0:
            isprime=False
        x+=1
    i+=1 
    if isprime:
        pnums+=[i]

print(pnums)