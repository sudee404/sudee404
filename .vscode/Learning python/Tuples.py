tup=(1,2,3,4)
print(tup)

dict={
    ("sudi",21):"green",
    ("chief",20):"yellow"
}
print(dict)

#tuple unpacking
a, b, c, d =tup
print(a)

num=(1,2,3,4,5,6,7,8,9,0)
a,b,*c,d=num
print(len(c))
print(c)