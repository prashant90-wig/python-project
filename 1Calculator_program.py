sign = input("Enter a mathematical expression: (* + - /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if sign == '+' :
    result = a + b
    print(f"The result of {a} + {b} is: {result}")
elif sign == '-':
    result = a - b
    print(f"The result of {a} - {b} is: {result}")
elif sign == '*': 
    result = a * b
    print(f"The result of {a} * {b} is: {result}")
elif sign == '/' :
    if b != 0:
        result = a / b
        print(f"The result of {a} / {b} is: {result}")
    else:
        result = "Error: Division by zero is not allowed."
        print(result)
