def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            return 1 / a
        return a + b
    except ZeroDivisionError:
        return float('inf')  # Handle division by zero appropriately
        # Or you might raise a more specific exception or handle it differently based on your application's needs.