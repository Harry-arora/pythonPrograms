'''nested if program to check whether 
the number entered is
positive negative or zero'''

num = float(input("Enter a number: "))   # type casting the input number
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
