
# errors:
# 1. Compile time error: e.g. Syntax error
# 2. Logical error: e.g. we got invalid output.
# 3. Run time error: by using try, except , finally block we can handle it.


num1 = int(input("Enter a first number"))
num2 = int(input("Enter a second number"))
try:
    print("resource open")
    num1 = 5
    num2 = 0
    print(num1/num2)
except ZeroDivisionError as e:
    print ("A number cannot divisible by zero")
except NameError as e:
    print("Invalid input")
except Exception as e:
    print("Something went wrong")
finally:
    print("resource closed")







