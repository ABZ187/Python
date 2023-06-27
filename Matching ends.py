x=['hello','pop','mom','window','ho']
n=len(x)
num=0
for i in range(n):
    if len(x[i])>2:
       str=x[i]
       if str[0]==str[-1]:
           num+=1
           print(str)
print("number of strings with matching ends are ",num)