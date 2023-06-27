def fac(n):
    p=1
    for x in range(1,n):
        p=n*p
        n-=1
    print(p)
fac(4)