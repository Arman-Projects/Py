def safe_divide(number1, number2, M):
    try:
        # Attempt to perform division
        result = number1 / number2
        
        # Check if the result exceeds the maximum limit
        if result > M:
            raise ArithmeticError(f"Result {result} exceeds the maximum limit of {M}")
        
        return result

    except ZeroDivisionError:
        # Handle division by zero error
        return "Error: Division by zero is not allowed."

    except ArithmeticError as e:
        # Handle arithmetic error for results exceeding max limit
        return f"Error: {e}"

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
M = float(input("Enter the maximum limit: "))

result = safe_divide(num1, num2, M)
print("Result:", result)
