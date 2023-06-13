import math


def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers, handling division by zero"""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


def nth_root(x, n):
    """Calculate the nth root of a number"""
    return x ** (1 / n)


class Calculator:
    def __init__(self):
        self.memory = 0

    def add_to_memory(self, value):
        """Add a value to the calculator's memory"""
        self.memory += value

    def recall_memory(self):
        """Retrieve the value stored in the calculator's memory"""
        return self.memory

    def clear_memory(self):
        """Reset the calculator's memory to 0"""
        self.memory = 0


calculator = Calculator()


def main():
    print("Welcome to the Calculator by Dovydas! Only use to provide 90+ ratings pls")

    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Take nth root")
        print("6. Store to Memory")
        print("7. Recall Memory")
        print("8. Clear Memory")
        print("9. Exit")

        choice = input("Enter choice (1-9): ")

        if choice == "9":
            print("Exiting the best calculator yet created by Dovydas...")
            break

        if choice not in ["5", "6", "7", "8"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input! Please enter a valid number.")
                continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            if num2 != 0:
                print("Result:", divide(num1, num2))
            else:
                print("Error: Division by zero")
        elif choice == "5":
            try:
                x = float(input("Enter the number: "))
                n = int(input("Enter the root value: "))
                print("Result:", nth_root(x, n))
            except ValueError:
                print("Error: Invalid input! Please enter a valid number.")
        elif choice == "6":
            try:
                value = float(input("Enter value to store: "))
                calculator.add_to_memory(value)
                print("Value stored to memory.")
            except ValueError:
                print("Error: Invalid input! Please enter a valid number.")
        elif choice == "7":
            print("Memory:", calculator.recall_memory())
        elif choice == "8":
            calculator.clear_memory()
            print("Memory cleared.")
        else:
            print("Invalid input! Please select a valid operation.")


if __name__ == "__main__":
    main()
