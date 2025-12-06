"""
Defines the safe_divide function for performing division with robust error handling.
"""

def safe_divide(numerator, denominator):
    """
    Performs division of two values, handling ZeroDivisionError and ValueError
    (for non-numeric inputs).

    Args:
        numerator (str): The numerator, typically a string from command line arguments.
        denominator (str): The denominator, typically a string from command line arguments.

    Returns:
        str: A message indicating the result or the specific error encountered.
    """
    try:
        # 1. Attempt to convert input arguments to floats
        num = float(numerator)
        den = float(denominator)

        # 2. Perform the division. If 'den' is 0.0, a ZeroDivisionError will be raised.
        result = num / den

        # 3. Return successful result message
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # 4. Handle division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # 5. Handle non-numeric input (if float() conversion fails)
        return "Error: Please enter numeric values only."

if __name__ == '__main__':
    # Simple tests for internal verification
    print(safe_divide("10", "5"))
    print(safe_divide("10", "0"))
    print(safe_divide("ten", "5"))
