def harshad():    
    n=156
    sum=0
    temp=n
    while temp>0:
        r=temp%10
        sum=sum+r
        temp//=10
    if n%sum==0:
        print(n,'harshad no.')
    else:
        print(n,'not harshad no.')
harshad()