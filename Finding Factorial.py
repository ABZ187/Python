try:
    y=int(input('Enter a number\n'))
    f=1
    x=y
except:
    print('Input should be a positive integer')
    quit()
if x>0:
    while x>0:
        f=f*x
        x=x-1
elif x==0:
   f=1
else:
    print('Input should be a positive integer')
    quit()
print('The factorial of ',y,' is ',f,)
