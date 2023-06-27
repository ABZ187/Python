s=float(input('What is your score between 0 to 1 ?'))
if s<0:
  print("Invalid value entered. Grade must be between 0 and 1.")

elif s<= 0.6:
    print("You got a F grade")
elif s<=0.7:
    print("You got a D grade")
elif s<=0.8:
    print("You got a C grade")
elif s<=0.9:
    print("You got a B grade")
elif s<=1:
    print("You got a A grade")
else :
    print("Invalid value entered. Grade must be between 0 and 1.")
