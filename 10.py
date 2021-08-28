def fun():
    n=1
    while n<=200:
        temp=n
        sum=0
        while temp>0:
            fact=1
            i=1
            r=temp%10
            while i<=r:
                fact=fact*i
                i=i+1
            sum=sum+fact
            temp//=10
        if sum==n:
            print(n)
        n=n+1
fun()