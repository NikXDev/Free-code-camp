try:
    value = 10/0
    num1 = int(input("Enter Number : "))
    print(num1)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError as err:
    print(err)
# we give error a name "err", so when we print the error it says
# pre defined error name