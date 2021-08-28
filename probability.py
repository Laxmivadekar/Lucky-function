# def comb(L):
      
#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
                  
#                 # check if the indexes are not
#                 # same
#                 if (i!=j and j!=k and i!=k):
#                     print(L[i], L[j], L[k])
                      
# # Driver Code
# comb([1, 2, 3])

l=[0,9,5]
i=0
while i<=2:
    j=0
    while j<=2:
        k=0
        while k<=2:
            if (i!=j and j!=k and i!=k):
                print(l[i],l[j],l[k])
            k=k+1
        j=j+1
    i=i+1

