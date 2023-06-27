num=[0,1]
n=2

while n < 100:
    x=num[n - 1] + num[n - 2]
    num.extend([x])
    n+=1
print(num)
