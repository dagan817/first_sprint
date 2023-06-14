from dovydas_calculator.calculator import add, subtract, multiply, divide, nth_root, Calculator 

calculator = Calculator()
calculator.store_result(10)
calculator.add_to_memory(5)
result = subtract(calculator.recall_memory(), 3)
calculator.store_result(result)
assertion = calculator.recall_memory() == 12