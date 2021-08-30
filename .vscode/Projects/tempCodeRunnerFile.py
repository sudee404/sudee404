def balanced(expression):
    #your code goes here
    
    class Stack:
        def __init__(self):
            self.items=[]

        def empty(self):
            self.items==[]

        def push(self,expression):
            for i in expression:
                if i=="(" or i==")":
                    self.items.insert(0,i)

        def pop(self):
            for i in self.items:
                if i==")":
                    x=self.items.index(i)
                    self.items.pop(0)
                    self.items.pop(x)

        def printstack(self):
            print(self.items)

    sttmnt=Stack()
    sttmnt.push(expression)
    sttmnt.printstack()
    sttmnt.pop()
    if sttmnt.printstack()==sttmnt.empty():
        return True
    else:
        return False


print(balanced(input()))