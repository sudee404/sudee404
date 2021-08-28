#maps-applies a function to an iterable
def double(x):
    return x*2
nums = []
for i in range(1,11):
    nums.append(i)

v=(lambda x: x*x)
res=list(map(v,nums))
print(res)

result=list(map(double,nums))
print(result)

#filters - remove an item not meeting a criteria
u=(lambda x: x%2==0)
ref=list(filter(u,nums))
print(ref)