marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
i=0
a=[]
while i<len(marks):
    j=0
    while j<len(marks[i]):
        a.append(marks[j])
        j=j+1
    i=i+1
print(a)

#=====use split function=======
a=['NavGurukul', 'is', 'an', 'alternative', 'to', 'higher', 'education', 'reducing', 'the', 'barriers', 'of', 'current', 'formal', 'education', 'system'] 
b=[]
i=0
while i<len(a):
    b.append(a[i])
    i=i+1
print(b)