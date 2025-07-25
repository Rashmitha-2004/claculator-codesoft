import operator

def get_number(prompt):
    """Keeps asking the user until they enter a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation(operations):
    """Keeps asking the user until they enter a valid operator."""
    while True:
        op_symbol = input("Enter an operator (+, -, *, /): ").strip()
        if op_symbol in operations:
            return op_symbol
        else:
            print("Invalid operator. Please choose from +, -, *, /.")

def run_calculator():
    """Runs the main calculator logic."""
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    print("\n--- Simple Python Calculator ---\n")

    while True:
        num1 = get_number("Enter the first number: ")
        op_symbol = get_operation(operations)
        num2 = get_number("Enter the second number: ")

        if op_symbol == "/" and num2 == 0:
            print("\nError: Cannot divide by zero.\n")
        else:
            calculate_function = operations[op_symbol]
            result = calculate_function(num1, num2)
            print(f"\nResult: {num1} {op_symbol} {num2} = {result}\n")

        again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_calculator()
