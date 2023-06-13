import math


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
        return "Error: Division by zero"


def nth_root(x, n):
    return x ** (1 / n)


class Calculator:
    def __init__(self):
        self.memory = 0

    def add_to_memory(self, value):
        self.memory += value

    def recall_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0


calculator = Calculator()


def main():
    print("Welcome to the dovydas_calculator!")

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
            print("Exiting dovydas_calculator...")
            break

        if choice not in ["5", "6", "7", "8"]:
            num1 = float(input("Enter first number: "))

            if choice != "5":
                num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            x = float(input("Enter the number: "))
            n = int(input("Enter the root value: "))
            print("Result:", nth_root(x, n))
        elif choice == "6":
            value = float(input("Enter value to store: "))
            calculator.add_to_memory(value)
            print("Value stored to memory.")
        elif choice == "7":
            print("Memory:", calculator.recall_memory())
        elif choice == "8":
            calculator.clear_memory()
            print("Memory cleared.")
        else:
            print("Invalid input! Please select a valid operation.")


if __name__ == "__main__":
    main()
