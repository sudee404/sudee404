#strings
string="hello my dear sweet rosaline"
print(string.replace("my","world"))
print(string.upper())
print(string.lower())
print(len(string))
print(string)

#lists
names=["sudi","otieno","abdalla"]
print(names)
names.pop(0)
print(names)
names.insert(0, "masuud")
print(names)
names.append("abdull")
print(names)
d=names.count("sudi")
print(d)

#list functions
num=[1,2,3,4,5,6,7,8,9]
num.sort(reverse=True)
print(num)
num.reverse()
print(num)
print(max(num))
print(min(num))

#list comprehensions
squares=[i**2 for i in range(4,8)]
print(squares[::-1])

cubes=[i**3 for i in range(4) if i%3==0]
print(cubes)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))