def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        return num1, num2, operation

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None, None, None

def calculator():
    print("------------------")
    print("Simple Calculator")
    print("------------------")
    print(" ")

    while True:
        num1, num2, operation = get_user_input()

        if num1 is None or num2 is None or operation not in ('+', '-', '*', '/'):
            continue

        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print(" ")

            print("------------------")

            print(f"Result: {result}")
            print("------------------")

        except ValueError as e:
            print(f"Error: {e}")

        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the calculator.")
            break

if __name__ == "__main__":
    calculator()
