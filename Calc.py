def add(x, y, z):
    return x + y + z

def subtract(x, y , z):
    return x - y - z

def multiply(x, y, z):
    return x * y * z

def divide(x, y, ):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                num3 = float(input("Enter Third number: "))

                if choice == '1':
                    print("Result:", add(num1, num2, num3))
                elif choice == '2':
                    print("Result:", subtract(num1, num2, num3))
                elif choice == '3':
                    print("Result:", multiply(num1, num2, num3))
                elif choice == '4':
                    print("Result:", divide(num1, num2, num3))
            except ValueError:
                print("Invalid input! Please enter numbers.")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    calculator()

