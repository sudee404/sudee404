def counter(text,char):
    count=0
    for t in text:
        if t==char:
            count+=1
    return(count)

#getting input
name1=input("enter file name1: ")
name2=("{d}.txt".format(d=name1))
with open(name2) as f:
    txt=f.read()

name3=input("enter file name2: ")
name4=("{d}.txt".format(d=name3))
with open(name4) as g:
    txt1=g.read()


h=(counter(txt,"r"))
j=(counter(txt1,"r"))

print(f"{name1} has {h-j} more r's than {name3} ")