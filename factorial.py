def fac(n):
    fac=1
    while n>=1:
        fac=fac*n
        n=n-1
    return fac
n=int(input('enter a number'))
print(fac(n))