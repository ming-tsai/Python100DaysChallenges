CALCULATOR_ART = """
     _____________________
    |  _________________  |
    | |                 | |
    | |   CALCULATOR    | |
    | |_________________| |
    |  ___ ___ ___   ___  |
    | | 7 | 8 | 9 | | + | |
    | |___|___|___| |___| |
    | | 4 | 5 | 6 | | - | |
    | |___|___|___| |___| |
    | | 1 | 2 | 3 | | * | |
    | |___|___|___| |___| |
    | | . | 0 | = | | / | |
    | |___|___|___| |___| |
    |_____________________|
"""

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: can't divide by zero!" if b == 0 else a / b

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(CALCULATOR_ART)
    first = float(input("What's the first number?: "))

    while True:
        print(" ".join(operations))
        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation! Try +, -, *, or /")
            continue

        second = float(input("What's the next number?: "))
        answer = operations[operation_symbol](first, second)

        print(f"{first} {operation_symbol} {second} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or 'n' to start over: ").lower()
        first = answer if choice == 'y' else float(input("What's the first number?: "))

if __name__ == "__main__":
    calculator()