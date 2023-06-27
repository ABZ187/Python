def computepay(p,h):
    if h<= 40:
        print('Your weekly salary is ',p*h )
    else:
        print('Your weekly salary is  ', p*(1.5*h-20))

p=float(input('How much do you get paid per hour for 40 or below hours?'))
h=float(input('How many hours do you work weekly?'))
computepay(p,h)
