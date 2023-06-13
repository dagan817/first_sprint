# dovydas_calculator

The `dovydas_calculator` package provides a simple calculator program with basic arithmetic operations, memory functionality, and the ability to take the nth root of a number.

## Installation

You can install the `dovydas_calculator` package using pip:

pip install dovydas_calculator


## Usage

After installing the package, you can run the `dovydas_calculator` program from the command line:

dovydas_calculator


The program will display a menu with the available operations. Enter the corresponding number to select an operation and follow the prompts to input the necessary values. The program will then perform the selected operation and display the result.

### Operations

The `dovydas_calculator` supports the following operations:

- **Addition:** Add two numbers.
- **Subtraction:** Subtract one number from another.
- **Multiplication:** Multiply two numbers.
- **Division:** Divide one number by another. Avoids division by zero.
- **nth Root:** Calculate the nth root of a number.
- **Store to Memory:** Store a value in the memory.
- **Recall Memory:** Retrieve the value stored in the memory.
- **Clear Memory:** Clear the stored value in the memory.

### Examples

Here are a few examples to demonstrate the usage of the `dovydas_calculator` program:

1. Addition:
Select operation:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Take nth root
6. Store to Memory
7. Recall Memory
8. Clear Memory
9. Exit
Enter choice (1-9): 1
Enter first number: 5
Enter second number: 3
Result: 8


2. Division:

Select operation:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Take nth root
6. Store to Memory
7. Recall Memory
8. Clear Memory
9. Exit
Enter choice (1-9): 4
Enter first number: 10
Enter second number: 2
Result: 5.0


3. Taking nth Root:

Select operation:

1. Add
2. Subtract
3. Multiply
4. Divide
5. Take nth root
6. Store to Memory
7. Recall Memory
8. Clear Memory
9. Exit
Enter choice (1-9): 5
Enter the number: 16
Enter the root value: 4
Result: 2.0


## Testing

The `dovydas_calculator` package includes Pytest test cases to ensure the correctness of the calculator functions. To run the tests, you can use the following command:

pytest

This will automatically discover and execute the test cases defined in the `tests` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


