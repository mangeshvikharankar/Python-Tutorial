
num = int(input(" Enter given number"))


def fact():
    factorial = 1
    if num <0:
        print("Sorry, factorial of negative numbers is doesnt exist")
    elif num == 0:
        print("The factorial of o is 1")
    else:
        for i in range (1, num+1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)

fact()
