class Person:
    def __init__(self,gender):
        self.gender=gender
        self.dict={}

    def getDetails(self,name,age):
        self.name=name
        self.age=age

    def wr(self):
        f=open("fname.txt","a+")
        f.write("Name: {n}\n".format(n=[self.name]))
        f.write("Age: {a}\n".format(a=[self.age]))
        f.write("Gender: {g}\n".format(g=[self.gender]))
        f.close()

g=input("enter gender: ")
if g=="male"or "female":
    p1=Person(g)
    n=input("enter name:")
    a=int(input("enter age:"))
    p1.getDetails(n,a)
    p1.wr()
