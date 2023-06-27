from array import *

x=array('i',[5,7,-8,99,0])
n=0
for a in x:
    m=0
    for b in range(4):
        if x[n]<x[m]:
            tem=x[n]
            x[n]=x[m]
            x[m]=tem
        m+=1
        if m>4:
            m=0
    n+=1
print(x)