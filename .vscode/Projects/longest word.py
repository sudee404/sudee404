txt=input("enter sentence: ")
text=txt.split()

list=[]
for i in text:
    list+=[len(i)]

lonlet=max(list)
for j in text:
    if lonlet == len(j):
        print(j)
