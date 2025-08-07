def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    while True:
        print("\n--- Command-Line Calculator ---")
        print("1. Addition (+)")
        print("2. subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an operation: ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numaric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        
        print("Result:", result)

calculator()