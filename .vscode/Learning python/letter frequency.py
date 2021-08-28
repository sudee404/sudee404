text=input("enter text: ")
letter=input("enter letter: ")
count=0
for x in text:
    if x==letter:
        count+=1

n=count
d=len(text)
print(n/d*100)