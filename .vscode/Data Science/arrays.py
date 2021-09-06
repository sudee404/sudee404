import numpy as np
import random
x = [i for i in range(1,20,5)]
xArr=np.array(x)
xAr=np.arange(1,20,5)
for i in range(20,23):
    xArr=np.append(xArr,i)

xArr=np.delete(xArr,0)
print(x)
print(xArr)
print(xAr)
xAr=np.append(xArr,6)
print(xArr)
print(xAr)
print(np.sort(xAr))
xA=xArr.reshape([2,3])
print(xA)
xa=xA.flatten()
print(xa)
#conditions can be added to index
print(xa[xa<20])
print(xa.sum())
print(xa.max())
print(xa.min())