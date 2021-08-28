def fun(b):
    i=0
    b=[]
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i=i+1
    return b
a=[1,2,3,3,3,3,4,5]
print(fun(a))