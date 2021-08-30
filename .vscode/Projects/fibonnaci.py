n=int(input("enter number: "))
def fibonnacci(x):
    if x<=1:
        return x
    else:
        return(fibonnacci(x-1) + fibonnacci(x-2))

for i in range(n):
    print(fibonnacci(i))