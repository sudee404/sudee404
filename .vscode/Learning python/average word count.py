text = input()
text.remove(" ")
test=text.split()
x=len(text)
y=len(test)
z=x/y
print(x,y,z)
print("{:.1f}".format(z))