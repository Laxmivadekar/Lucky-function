def fun():
    n=1
    while n<=1000:
        sum=0
        i=1
        while i<n:
            if n%i==0:
                sum=sum+i
            i=i+1
        if sum==n:
            print(n)
        n=n+1
fun()