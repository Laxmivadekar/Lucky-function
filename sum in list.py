def fun(l):
    sum=0
    i=0
    while i<len(l):
        sum=sum+l[i]
        i=i+1
    return sum
l=(8,2,3,0,7)
print(fun(l))