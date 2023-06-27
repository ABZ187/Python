from numpy import *
m1=array([[3,3,3],[4,5,6],[7,9,9]])
m2=array([[4,5,3],[5,7,9],[9,4,5]])
ma=m1.flatten()
mb=m2.transpose()
mb=mb.flatten()
np=m1.flatten()
n=0
o=0
for r in range(3):
    m = 0
    for p in range(3):
        np[o]=ma[n]*mb[m]+ma[n+1]*mb[m+1]+ma[n+2]*mb[m+2]
        m+=3
        o+=1
    n += 3
print(np.reshape(3,3))


