di={'a':1, 'b':4, 'c':2}
n=len(di)
if di.get('a')>di.get('b'):
    if di.get('a') > di.get('c'):
        print("greatest value is ",di.get('a'))
    else:
        print("greatest value is ", di.get('c'))
elif di.get('b')>di.get('c'):
    print("greatest value is ", di.get('b'))
else:
    print("greatest value is ", di.get('c'))

