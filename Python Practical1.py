# Arbaaz Shaikh
# Roll no. 4454
# TyBsc Mathematics

# Python Practical1

# #Question1
x = int(input("enter a integer"))
y = int(input("enter another integer"))
print("Addition is ", x + y)
print("Subtraction is ", x - y)
print("multiplication is ", x * y)
print("Division is ", x / y)

##########
# Question2
char = input("Enter a character")
if char.isupper():
    print("Already in uppercase: ", char)
else:
    print("Character in uppercase: ", char.upper())

    #########
# Question3
x = input("enter a value")
y = input("enter another value")
t = x
x = y
y = t
print("first no. is ", x)
print("Second no. is", y)

#########

# Q4
p = float(input("enter principle"))
i = float(input("enter interest rate pcpa"))
n = float(input("enter period"))
print("Simple interest is ", p * n * i / 100)
print("Compound interest is ", p * (1 + i / 100) ** n)

#########

# Q5
x = input("enter first name")
y = input("enter second name")

print("Greetings!!!", x, y)

######
# Q6
b = float(input("enter your basic pay"))
print("Your HRA is ", b * 0.1)
print("Your TA is ", b * 0.05)
print("Your salary is ", b + b * 0.15)

#######
# Q7
x = float(input("enter a value"))
print(int(x))
##########

# Q8
x = int(input("enter a value"))
print(x % 10)

# Arbaaz Shaikh
# Roll no. 4454
# TyBsc Mathematics

# Python Practical2

# Q1
x = float(input("Enter a number"))
y = float(input("Enter another number"))
if x == y:
    print(f"{x} equals to {y}")
else:
    print(f"{x} not equals to {y}")

# Q3
x = input("Enter")
if x.isnumeric():
    print("Digit Entered")
elif x.isalpha():
    print("Alphabet Entered")
elif x.isspace():
    print("Whitespace Entered")

# Q4
x = input("Enter")
print(x)
Digit, uppercase, lowercase = 0, 0, 0
for i in x:
    if i.isnumeric():
        Digit += 1
    elif i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
print(f"There are {lowercase} lowercases, {uppercase} uppercases and {Digit} Digits ")

# Q5
s = 0
for i in range(1, 2000):
    s += 1 / i
print(s)

# Q6
while (1):
    x = input("Enter")
    if x == 'Quit':
        break
    print(f'String Lenght is {len(x)}')

# Q7
x = float(input("Enter a number"))
print(f'Number {x}, Square {x ** 2}, Cube {x ** 3}')


# Arbaaz Shaikh
# Roll no. 4454
# TyBsc Mathematics

# Python Practical3

# Q1
def find_ch(x, y):
    return x[y]


x = input("Enter a string")
y = int(input('Enter the position'))
print(find_ch(x, y))

# Q2
x = input("Enter a string")
position = 0
for i in x:
    position += 1
print(position)

# Q3
x = input("Enter a string")
if len(x) <= 2:
    print('')
else:
    print(x[0] + x[1] + x[-2] + x[-1])

# Q4
x = input("Enter a string")
print(x[0] + (len(x) - 1) * "$")

# Q5
x = input("Enter a string")
y = input('Enter anather String')
z = y[0] + x[1:] + ' ' + x[0] + y[1:]
print(z)

# Q6
x = input("Enter a string")
n = int(input('Enter the index of the character to be removed'))
if n == len(x):
    print(x[:n])
else:
    print(x[:n] + x[n + 1:])

# Arbaaz Shaikh
# Roll no. 4454
# TyBsc Mathematics

# Python Practical4

# Q2
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(x[:4])
print(x[4:7])
print(x[7:])

# Q3
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(list(map(ord, x)))

# Q4
x = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
s = 0
for i in x:
    s = s + i
print(s)

# Q5
x = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
s = 0
for i in x:
    if i % 2 == 0:
        s = s + i
print(s)

# Q6
while (1):
    t = x.count(x[i])
    s = x[i]
    if t > 1:
        for a in range(1, t):
            x.remove(s)
    i = i + 1
    if i >= len(x):
        break
print(x)


# Q7

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


R = matrix()
print(R)
print(transpose(R))



# Arbaaz Shaikh
# Roll no. 4454
# TyBsc Mathematics

# Python Practical5

# Q1
def find_ch(x, y):
    return x[y]


x = input("Enter a string")
y = int(input('Enter the position'))
print(find_ch(x, y))


# Q2
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(x[:4])
print(x[4:7])
print(x[7:])

# Q3
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(list(map(ord, x)))

# Q4
p = float(input("enter principle"))
i = float(input("enter interest rate pcpa"))
n = float(input("enter period"))
print("Simple interest is ", p * n * i / 100)
print("Compound interest is ", p * (1 + i / 100) ** n)

#########


# Q5
s = 0
for i in range(1, 2000):
    s += 1 / i
print(s)

# Q6
while (1):
    x = input("Enter")
    if x == 'Quit':
        break
    print(f'String Lenght is {len(x)}')
