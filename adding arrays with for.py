from numpy import *
arr=array([1,347,3,4])
arr1=array([2,4,6,223])
n=0
m=0
p=0
for q in arr:
    arr[p]=arr[n]+arr1[m]
    p+=1
    m+=1
    n+=1
print(arr)