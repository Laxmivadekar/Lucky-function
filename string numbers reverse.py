def fun(x):
    i=1
    y=''
    while i<len(x):
        y=y+x[-i]
        i=i+1
    return y
x='1234abcd'
print(fun(x))