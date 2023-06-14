import pytest
from dovydas_calculator.calculator import add, subtract, multiply, divide, nth_root, Calculator


def test_addition():
    result = add(2, 3)
    assertion = result == 5
    assert assertion


def test_subtraction():
    result = subtract(5, 3)
    assertion = result == 2
    assert assertion


def test_multiplication():
    result = multiply(2, 3)
    assertion = result == 6
    assert assertion


def test_division():
    result = divide(10, 2)
    assertion = result == 5
    assert assertion


def test_division_by_zero():
    result = divide(10, 0)
    assertion = result == "Error: Division by zero"
    assert assertion


def test_nth_root():
    result = nth_root(16, 2)
    assertion = result == 4
    assert assertion


def test_calculator_add_to_memory():
    calculator = Calculator()
    calculator.add_to_memory(5)
    assertion = calculator.recall_memory() == 5
    assert assertion


def test_calculator_recall_memory():
    calculator = Calculator()
    calculator.add_to_memory(10)
    result = calculator.recall_memory()
    assertion = result == 10
    assert assertion


def test_calculator_clear_memory():
    calculator = Calculator()
    calculator.add_to_memory(5)
    calculator.clear_memory()
    assertion = calculator.recall_memory() == 0
    assert assertion


def test_calculator_store_result():
    calculator = Calculator()
    calculator.store_result(10)
    assertion = calculator.recall_memory() == 10
    assert assertion


def test_calculator_add_operation():
    calculator = Calculator()
    calculator.store_result(5)
    calculator.add_to_memory(3)
    result = add(calculator.recall_memory(), 2)
    calculator.store_result(result)
    assertion = calculator.recall_memory() == 10
    assert assertion


def test_calculator_subtract_operation():
    calculator = Calculator()
    calculator.store_result(10)
    calculator.add_to_memory(5)
    result = subtract(calculator.recall_memory(), 3)
    calculator.store_result(result)
    assertion = calculator.recall_memory() == 2
    assert assertion


def test_calculator_multiply_operation():
    calculator = Calculator()
    calculator.store_result(2)
    calculator.add_to_memory(3)
    result = multiply(calculator.recall_memory(), 4)
    calculator.store_result(result)
    assertion = calculator.recall_memory() == 24
    assert assertion


def test_calculator_divide_operation():
    calculator = Calculator()
    calculator.store_result(20)
    calculator.add_to_memory(4)
    result = divide(calculator.recall_memory(), 2)
    calculator.store_result(result)
    assertion = calculator.recall_memory() == 10
    assert assertion


def test_calculator_nth_root_operation():
    calculator = Calculator()
    calculator.store_result(81)
    result = nth_root(calculator.recall_memory(), 2)
    calculator.store_result(result)
    assertion = calculator.recall_memory() == 9
    assert assertion