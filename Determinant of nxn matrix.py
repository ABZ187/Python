import numpy as np
mat= [[1,2,4,3],[2,3,4,1],[4,5,8,9],[5,4,6,4]]
mat = np.array(mat)
print(mat)
ilist=np.arange(4)
ilist=list(ilist)
jlist=np.arange(4)
jlist=list(jlist)
def cofac():
    alist=ilist
    blist=jlist
    for i,j in ilist ,jlist:
        alist.remove(i)
        blist.remove(j)        
        c=mat[i,j]
        len_a=len(alist)
        if len_a==2:
          d=c*  [mat[min(alist),min(alist)]*        mat[max(alist),max(alist)]-mat[min(alist),max(alist)]*mat[max(alist),min(alist)]]

