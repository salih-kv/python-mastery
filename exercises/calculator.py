def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"
    else:
        result = "Invalid operator"

    print("Result:", result)

calculator()
