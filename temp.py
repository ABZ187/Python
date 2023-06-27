d=dict()
c=['m','n','o','p','o','m']
for a in c:
    d[a]= d.get(a,0)+1
    print(d[a])
print(c)
print(d)
