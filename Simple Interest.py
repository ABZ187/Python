try:
    i=float(input('Enter your annual interest rate\n'))
    p=float(input('Enter your priciple amount\n'))
    t=float(input('Enter the time period in years\n'))
    print('Your simple interest is ',t*i/100*p,'  and your total amount is ',t*i/100*p+p)
except:
    print('Invalid input')
