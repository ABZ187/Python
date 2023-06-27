from datetime import datetime

t = 100


def num_check(a):
    global t
    if a == num:
        print("Good one. You guessed it right. The number is ", num, "Your score is ", t)
        quit()
    else:
        t -= 20


now = datetime.now()

ct = now.strftime("%H:%M:%S")
num = int(ct[0]) + int(ct[1]) + int(ct[4]) + int(ct[3]) + int(ct[7]) + int(ct[6])
print(num)
x = int(input("Guess the number. it is a non-negative integer less than 39"))
print("You entered ", x)
num_check(x)
if num % 2 == 0:
    p = "even number"
else:
    p = "odd number"
sum_of_digits = num % 10 + int(num / 10)
print("it is a ", p, " and sum of digits is ", sum_of_digits)
x = int(input("Try again. Guess the number"))
print("You entered ", x)
num_check(x)
digit_replace = (num % 10) * 10 + int(num / 10)
print("if place value of the digits are interchanged and added to the number then the sum is "
      , num + digit_replace)
x = int(input("Try again. Guess the number."))
print("You entered ", x)
num_check(x)
between = int(num / 10)
print("The number is between ", between * 10, " and ", (between + 1) * 10)
x = int(input("Try again. Guess the number."))
num_check(x)
print("Exhausted the number of guesses. Game over")
