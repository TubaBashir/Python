def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def power(x, y): return x ** y
def remainder(x, y): return "Error! Division by zero." if y == 0 else x % y

def calculator():
    print("🔢 Python Mathematical Operations Calculator 🔢")
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Remainder (%)")
    print("7. Exit")

    while True:
        choice = input("\nEnter choice (1-7): ").strip()

        if choice == '7':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"Result: {num1} % {num2} = {remainder(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid option from 1 to 7.")

if __name__ == "__main__":
    calculator()
