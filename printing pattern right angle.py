#num=int(input('enter a number'))
#for i in range(1,num+1):
 #   print('  '*(num-i)+'* '*i)

# i=1
# while i<=5:
#     j=i
#     while j>0:
#         print('  '*(5-i)+'* '*i,end=' ')
#         j=j-1
#     print()
#     i=i+1

r=0
while r<5:
    i=1
    s=5-r-1#5-r-1
    while s>0:
        print(end=" ")
        s-=1
    st=r+1
    while st>0:
        print(st,end="")
        st-=1
    print()
    r+=1
