def fun(l):
    mul=1
    i=0
    while i<len(l):
        mul*=l[i]
        i=i+1
    return mul
l=(8,2,3,-1,7)
print(fun(l))