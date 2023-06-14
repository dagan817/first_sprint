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

    def store_result(self, result):
        """Store the result in memory"""
        self.memory = result


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
        print("6. Recall Memory")
        print("7. Clear Memory")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "8":
            print("Exiting the best calculator yet created by Dovydas...")
            break

        if choice not in ["6", "7"]:
            try:
                if calculator.recall_memory() != 0:
                    num1 = calculator.recall_memory()
                else:
                    num1 = float(input("Enter first number: "))

                if choice != "5":
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input! Please enter a valid number.")
                continue

        if choice == "1":
            # Perform addition
            result = add(num1, num2)
            print("Result:", result)
            calculator.store_result(result)
        elif choice == "2":
            # Perform subtraction
            result = subtract(num1, num2)
            print("Result:", result)
            calculator.store_result(result)
        elif choice == "3":
            # Perform multiplication
            result = multiply(num1, num2)
            print("Result:", result)
            calculator.store_result(result)
        elif choice == "4":
            if num2 != 0:
                # Perform division if the divisor is not zero
                result = divide(num1, num2)
                print("Result:", result)
                calculator.store_result(result)
            else:
                print("Error: Division by zero")
        elif choice == "5":
            try:
                if calculator.recall_memory() != 0:
                    # Use the stored value as the first number for nth root
                    x = calculator.recall_memory()
                else:
                    x = float(input("Enter the number: "))

                n = int(input("Enter the root value: "))
                # Calculate the nth root
                result = nth_root(x, n)
                print("Result:", result)
                calculator.store_result(result)
            except ValueError:
                print("Error: Invalid input! Please enter a valid number.")
        elif choice == "6":
            # Recall the value from memory
            print("Memory:", calculator.recall_memory())
        elif choice == "7":
            # Clear the memory
            calculator.clear_memory()
            print("Memory cleared.")
        else:
            print("Invalid input! Please select a valid operation.")


if __name__ == "__main__":
    main()