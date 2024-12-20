def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a//b
def modulo(a,b):
    return a%b
def operation(a,b,operator):
    if operator=='+':
        return add(a,b)
    elif operator=='-':
        return sub(a,b)
    elif operator=='*':
        return  multi(a,b)
    elif operator=='/':
        return div(a,b)
    else:
        return modulo(a,b)
a=int(input("Enter The A Value:"))
b=int(input("Enter The B Value:"))
operator=input("Enter the Operators(+,-,*,/,%):")
operation_operator=operation(a,b,operator)
print('value is:',operation_operator)
while True:
    yes_no=input("YES or NO to continue('y'/'n'):")
    if yes_no=='y':
        a = operation_operator
        b = int(input("enter a value:"))
        operator = input("Enter the Operators(+,-,*,/,%):")
        operation_operator = operation(a, b, operator)
        print('value is:',operation_operator)
    else:
        print('value is:', operation_operator)
        break


