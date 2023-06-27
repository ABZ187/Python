file= input('enter file: ')
if len(file)<1:
    file='temp.txt'
    fhand=open(file)
else:
    fhand=open(file)
di={}
for lin in fhand:
    if lin.startswith('From'):
        #print(lin)
        wds=lin.split()
        #print(wds)
        a=wds[1]
        
        di[a]=di.get(a,0)+1
for c,d in di.items():
    name=None
    num=None
    if num==None or d > num:
        name=c
        num=d

print('The highest number of mails were send by ',name,'.',name,' sent ',num,' mails.')
#print(di)
