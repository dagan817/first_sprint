# Calculator by Dovydas

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

Dovydas Calculator is a simple calculator application that provides basic arithmetic operations and memory functionality. It allows users to perform addition, subtraction, multiplication, division, and nth root calculations. The calculator also includes a memory feature to store and recall values.

This calculator is developed using Python and follows the PEP 8 style guidelines.

## Installation

You can install Dovydas Calculator using pip. Run the following command:


pip install dovydas_calculator
Usage
To use the calculator in your Python code, import the necessary functions and classes from the dovydas_calculator module:


from dovydas_calculator.calculator import add, subtract, multiply, divide, nth_root, Calculator
Basic Arithmetic Operations
You can perform various arithmetic operations using the provided functions:

Addition: add(x, y)
Subtraction: subtract(x, y)
Multiplication: multiply(x, y)
Division: divide(x, y)
Nth Root: nth_root(x, n)
Here's an example of using the arithmetic operations:


# Perform addition
result = add(2, 3)
print("Addition Result:", result)

# Perform subtraction
result = subtract(5, 3)
print("Subtraction Result:", result)

# Perform multiplication
result = multiply(2, 3)
print("Multiplication Result:", result)

# Perform division
result = divide(10, 2)
print("Division Result:", result)

# Calculate nth root
result = nth_root(16, 2)
print("Nth Root Result:", result)
Memory Functionality
The calculator also includes memory functionality to store and recall values. You can use the Calculator class to access this functionality:

# Create a calculator instance
calculator = Calculator()

# Add a value to memory
calculator.add_to_memory(5)

# Retrieve the value stored in memory
memory_value = calculator.recall_memory()
print("Memory Value:", memory_value)

# Clear the memory
calculator.clear_memory()
Storing and Using Results
You can store a result in memory and use it in subsequent calculations:

# Create a calculator instance
calculator = Calculator()

# Store a result in memory and use it in the next calculation
calculator.store_result(10)
calculator.add_to_memory(3)
result = add(calculator.recall_memory(), 2)
calculator.store_result(result)
print("Memory Calculation Result:", calculator.recall_memory())

# Clear the memory
calculator.clear_memory()
Testing
The calculator package includes comprehensive tests to ensure the correctness of its functionality. To run the tests, you can use the pytest framework.

Make sure you have pytest installed. If not, install it using pip:


pip install pytest
Navigate to the root directory of the calculator package where the tests folder is located.

Run the following command to execute the tests:


pytest
This will run all the tests and display the results in the terminal.

License
This project is licensed under the MIT License - see the LICENSE file for details.