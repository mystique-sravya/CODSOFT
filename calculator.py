def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def square_root(x):
    if x < 0:
        return "Invalid input. Cannot calculate square root of a negative number!"
    return x ** 0.5

def exponentiation(x, y):
    return x ** y

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Exit")

    while True:
        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '6'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '6':
                print("Result:", exponentiation(num1, num2))
        elif choice == '5':
            num = float(input("Enter the number: "))
            print("Square Root:", square_root(num))
        else:
            print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
    main()
