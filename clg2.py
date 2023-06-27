hihellont(input('Enter a number'))
# # y=int(input('Enter a number'))
# # print("Addition is",x+y)
# # monthly_payment=int(input('enter your payment'))
# # print("your monthly payment is", 9*monthly_payment/10)
# # x=int(input("Enter a number"))
# # y=int(input("Enter another number"))
# # print(x%y)
# # age=int(input("Enter your age: "))
# # if (age>=18):
# #   print("You are eligible to vote")
# # if (age < 18):
# #   print("You can vote after ", 18-age ," years" )
#
# x = int(input("enter first number x= "))
# y = int(input("Enter second number y= "))
# if (x > y):
#     print("Greatest number is x")
# if (y > x):
#     print("Greatest number is y")
# if (x == y):
#     print("x=y")
#     #####
#
#     week = {1: 'Monday', 2: 'Tuesday', 3: 'Thurday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday', 7: 'Sunday'}
#     x = int(input("Enter a value"))
#     print(week.get(x))
# ########
#
# i = 0
# s = 0
# while i < 11:
#     s = i + s
#     i += 1
# print("sum is, ", s)
# print("average is ,", s / 10)
#
# ########
#
# i = 0
# while i < 20:
#     print('*', end='')
#     i += 1
#
# #######
#
# m = int(input("enter the value of m"))
# n = int(input("enter the value of n"))
# sum = 0
# while m <= n:
#     sum = sum + m
#     m += 1
# print("sum is", sum)
#
# ########
# x = int(input("enter a value"))
# i = 1
# for i in range(1, 11):
#     print(x * i)
#
# ############
# m = (int(input("Enter m")))
# n = (int(input("Enter n")))
# for i in range(m, n + 1):
#     if i % 2 == 1:
#         print(i, "is odd")
#     else:
#         print(i, "is even")
#
# ##############
# m = int(input("enter a number"))
# c = 0
# for i in range(2, m):
#     if m % i == 0:
#         c = +1
#         break
# if c > 0:
#     print(m, " is composite")
# else:
#     print(m, " is prime")
#     ##############
#
# for i in range(5):
#     print()
#
#     for j in range(5):
#         print("*", end=' ')
# #########
#
# for i in range(5):
#     print()
#     for j in range(i + 1):
#         print("*", end=' ')
#
# ##############
# for i in range(5):
#     print()
#     for j in range(i + 1):
#         print(j + 1, end=' ')
#
# ############
#
# x = [input("Enter a Alphabet from ( O, A, B, C, F)")]
# y = ["O", "A", "B", "C", "F"]
# if x[0] == y[0]:
#     print("Outstanding")
# elif x[0] == y[1]:
#     print("Apple")
# elif x[0] == y[2]:
#     print("Ball")
# elif x[0] == y[3]:
#     print("Cat")
# elif x[0] == y[4]:
#     print("Fail")
# #########
#
# str = input("enter the value")
# if str == 'Quit':
#     print("Program Quit ")
# else:
#     print("the lenght of string is ", len(str))
#
#
# ###############
#
# def lenck(m):
#     if len(m) < 6:
#         global x
#         print('Enter ', i + 1, 'th word again')
#         x = [input()]
#         m = x[0]
#         lenck(m)
#
#
# x = []
# list1 = []
# for i in range(6):
#     x = [input("Enter characters")]
#     y = x[0]
#     lenck(y)
#     list1.extend(x)
# print(list1)
#
# ###########
#
# ch = input("Enter character")
# n = len(ch)
# u = 0
# l = 0
# d = 0
# for i in range(n):
#     if ch[i].isupper():
#         u += 1
#     elif ch[i].islower():
#         l += 1
#     else:
#         try:
#             x = int(ch[i])
#             d = d + 1
#         except ValueError:
#             pass
# print("There are ", u, "uppercases.")
# print("There are ", l, "lowercases.")
# print("There are ", d, "digits.")
#
# ############
#
# import math
#
# while 1:
#     num = int(input("enter a no"))
#     if num == 999:
#         print("enter valid no.")
#         break
#     elif num < 0:
#         print("sqrt of -ve no. cannot be calculated")
#         continue
#     else:
#         print("sqrt is ", math.sqrt(num))
# ##########
#
# n=6
# for i in range(1,n):
#     if i % 4 == 1:
#
#         print("* * * * *",end="")
#     else:
#         print("*       *",end="")
#
#     print()
#
# ##############
#
# n = 7
# m = 1
# for i in range(n, 1, -1):
#     for j in range(1, i ):
#         print(' ', end='')
#     for k in range(1, m):
#         print(k, end='')
#     m += 1
#     print()
# ##############
#
# n = 6
# for i in range(n, 1, -1):
#     for j in range(i, 1, -1):
#         print(' ', end="")
#     for k in range(1, n - i + 2):
#         print(k, end="")
#     for m in range(1, n - i + 1):
#         print(k-m, end="")
#     print()
#
#     #############
#
#     n = 5
#     for i in range(1, n + 1):
#         for j in range(n - i + 1, 0, -2):
#             print(' ', end='')
#         for k in range(1, i + 1):
#             print(i, end="")
#         print()

# x=float(input("Enter a number"))
# y=float(input("Enter another number"))
# if x==y:
#     print(f"{x} equals to {y}")
# else:
#     print(f"{x} not equals to {y}")

# x=input("Enter")
# if x.isnumeric():
#     print("Digit Entered")
# elif x.isalpha():
#     print("Alphabet Entered")
# elif x.isspace():
#     print("Whitespace Entered")

# x = input("Enter")
# print(x)
# Digit, uppercase, lowercase = 0,0,0
# for i in x:
#     if i.isnumeric():
#         Digit += 1
#     elif i.isupper():
#         uppercase += 1
#     elif i.islower():
#         lowercase += 1
# print(f"There are {lowercase} lowercases, {uppercase} uppercases and {Digit} Digits ")


# s=0
# for i in range(1,200000000):
#     s+=1/i
# print(s)

# while(1):
#     x=input("Enter")
#     if x=='Quit':
#         break
#     print(f'String Lenght is {len(x)}')

# x=float(input("Enter a number"))
# print(f'Number {x}, Square {x**2}, Cube {x**3}')

# def find_ch(x,y):
#     return x[y]
# x=input("Enter a string")
# y=int(input('Enter the position'))
# print(find_ch(x,y))

# x=input("Enter a string")
# position=0
# for i in x:
#     position+=1
# print(position)

# x=input("Enter a string")
# if len(x)<=2:
#     print('')
# else:
#     print(x[0]+x[1]+x[-2]+x[-1])

# x=input("Enter a string")
# print(x[0]+(len(x)-1)*"$")

# x=input("Enter a string")
# y=input('Enter anather String')
# z=y[0]+x[1:]+' '+x[0]+y[1:]
# print(z)

# x=input("Enter a string")
# n=int(input('Enter the index of the character to be removed'))
# if n==len(x):
#     print(x[:n])
# else:
#     print(x[:n] + x[n + 1:])

# x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# print(x[:4])
# print(x[4:7])
# print(x[7:])

# x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# print(list(map(ord,x)))
#
# x=[65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
# s=0
# for i in x:
#     s=s+i
# print(s)
#
# x=[65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
# s=0
# for i in x:
#     if i%2==0:
#         s=s+i
# print(s)

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A', 'G', 'H', 'I', 'J', 'A']
i = 0


# while(1):
#     t = x.count(x[i])
#     s = x[i]
#     if t > 1:
#         for a in range(1, t):
#             x.remove(s)
#     i=i+1
#     if i>=len(x):
#         break
# print(x)

def matrix():
    R = []
    print('All rows must have same number of elements')
    m = int(input("Enter the number of rows"))
    n = int(input("Enter the number of colmns"))
    for j in range(1, m + 1):
        a = []
        for i in range(1, n + 1):
            a.append(input(f"Enter the values of {j}th row"))
        R.append(a)
    return R


def transpose(R):
    rt = []
    Rt = []
    r = R[1]
    for d in range(len(r)):
        rt = []
        for b in range(len(R)):
            r = R[b]
            v = r[d]
            rt.append(v)
        Rt.append(rt)
    return Rt

R=matrix()
print(R)
print(transpose(R))
