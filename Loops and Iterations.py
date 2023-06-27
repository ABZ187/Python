num=[]
for n in num:
    if n=='done':
        print('done')
        break
    try:
        a=int(input('enter a number'))
        num.append(a)
    except:
        print('Invalid value entered')
        continue
