print("Welcome to Simple Calculator")
print("1. Add")
print("2. Substraction")
print("3 Multi")
print("4 Divide")
print("5 Module")

operation = input("enter your choice \n")
if operation == '1':
    num1 = input("enter first number :")
    num2 = input('enter 2nd number')
    print("sum of two number is:", int(num1)+int(num2))
elif operation == '2':
    num1 = input("enter first number :")
    num2 = input('enter 2nd number')
    print("sub of two number is:", int(num1)-int(num2))
elif operation == '3':
    num1 = input("enter first number :")
    num2 = input('enter 2nd number')
    print("mul of two number is:", int(num1)*int(num2))
elif operation == '4':
    num1 = input("enter first number :")
    num2 = input('enter 2nd number')
    print("divide of two number is:", int(num1)/int(num2))            
else:
    print("invalid choice")
