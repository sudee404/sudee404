text=input("enter text: ")
dict={}
l=[]
for i in text:
    if i not in l:
        l.append(i)

for j in l:
    x=text.count(j)
    dict[j]=x

print(dict)