def balanced(expression):
    #your code goes here
    
    class Stack:
        def __init__(self):
            self.items=[]

        def empty(self):
            self.items==[]

        def push(self,expression):
            self.expression = expression
            self.items=list(filter(lambda x:x==")",expression)

        def pop(self):
            for i in expression:
                if i==")":
                    self.items.pop(0)

        def printstack(self):
            print(self.items)

    sttmnt=Stack()
    sttmnt.push(expression)
    sttmnt.printstack()
    sttmnt.pop()
    sttmnt.printstack()
    if sttmnt.items==[]:
        return True
    else:
        return False

print(balanced(input()))