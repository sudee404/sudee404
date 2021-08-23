nums = [1,2,3,4]
msg = "Numbers : {0} {1} {2} {3}".format(nums[0],nums[1],nums[2],nums[3])
print(msg)

mng = "I am {0}{1}{0}".format("abra","cad")
print(mng)

a="{x} {y}".format(x="sudi",y="abdalla")
print(a)

#string functions
print(a.replace("abdalla","otieno"))
print("-->".join([a,"abdalla","otieno"]))
print(a.endswith("abdalla"))
print(a.startswith("sudi"))
print(a.upper())
print(a.lower())
print(a.split())
x="sudi"
print(x.split())