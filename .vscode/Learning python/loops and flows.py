nums=[1,3,4,5,6]
count=0
if not 2 in nums:
    nums+=[2,7,8]
    for i in nums:
        while i==2:
            print(i)
            break
        count+=1
print(count)