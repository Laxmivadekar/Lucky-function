list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
a=[]
while i<len(list1):
    if list1[i] in list2:
        a.append(list1[i])
    i=i+1
print(a)


#==========
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
a=list1+list2
b=a.sort()
print(a)
i=0
c=[]
while i<len(a):
    if a[i] not in c:
        c.append(a[i])
    i=i+1
print(c)

