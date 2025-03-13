# Simple Calculator

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation! Use +, -, *, or /.")
        return

    print(f"Result: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
