h=float(input('How many hours a week do you work?'))
p=float(input('How much do you get paid for working 40 hours or below?'))


if h<=40:
    print('Your weekly salary is',h*p)
if h>40:
    print('Your weekly salary is',(h-40)*1.5*p+40*p)
    
