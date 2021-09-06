players = [14, 18, 19, 24, 26, 33, 42, 55, 67] 

#mean
def meanCalc(lst):
    sum=0
    for i in lst:
        sum+=i
    mean="{0:.1f} ".format((sum/len(lst)))
    return float(mean)
#median
def medianCalc(lst):
    lst.sort()
    print(lst)
    if len(lst)%2==1:
        m=(len(lst)+1)/2
        return lst[m]
    else:
        d1=len(lst)/2
        d2=((len(lst)/2)+1)
        lt=lst[(int(d1)):(int(d2))]
        m=meanCalc(lt)
        return m
#variance
def varianCalc(lst):
    m=meanCalc(lst)
    mlst=[]
    for i in lst:
        v=(i-m)**2
        mlst.append(v)
    var=meanCalc(mlst)
    return var
#standard deviation=sqaure root of variance
def deviation(lst):
    from math import sqrt
    var=varianCalc(lst)
    std=float("{0:.1f} ".format(sqrt(var)))
    return std

def deviate(lst):
    dev=deviation(lst)
    mn=meanCalc(lst)
    dif1=mn-dev
    dif2=mn+dev
    num=0
    for i in lst:
        if i >= dif1 and i<=dif2:
            num+=1

    return num

print(deviate(players))