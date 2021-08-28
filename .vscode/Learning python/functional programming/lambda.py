#creation of anonymous function

def my_func(f, arg):
  return f(arg)

def func(x):
    return (2*x*x)

print(my_func(func,5))
print((lambda x: 2*x*x)(5))

#assigning lambda to variables
v=(lambda x: x*x*x)
print(v(3))

triple=(lambda x:x*3)
double=(lambda x:x*2)

print(triple(double(2)))