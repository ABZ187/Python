from numpy import *
arr=array([1,2,4,68,890,0])
a=arr[0]
p=0
for n in arr:
    if a<arr[p]:
        a=arr[p]
    p+=1
print(a)
