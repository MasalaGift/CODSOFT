def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)\n")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation sign (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        print()

        if operator == '+':
            result = add(num1, num2)
            print("Result: " + str(result))
        elif operator == '-':
            result = subtract(num1, num2)
            print("Result: " + str(result))
        elif operator == '*':
            result = multiply(num1, num2)
            print("Result: " + str(result))
        elif operator == '/':
            result = divide(num1, num2)
            print("Result: " + str(result))
        else:
            print("Invalid operation sign. Please enter a valid sign.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
