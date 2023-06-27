import numpy as np
n=5
ilist = np.arange(n)+5
jlist = np.arange(n)+2
ilist=list(ilist)
jlist = list(jlist)
a = min(ilist)
print(ilist,jlist)
print(a)
ilist.remove(a)
jlist.remove(a)
print(ilist,jlist)