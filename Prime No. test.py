x=int(input('enter a no.'))
n=2
while n<x:
    if x%n==0:
        print('Not a prime no')
        break
    n+=1
    if n>=x:
        print('Prime No.')
if x==2:
    print('prime no')


