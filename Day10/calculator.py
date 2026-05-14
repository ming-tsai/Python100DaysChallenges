
def calculator_art():
    art = """
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
    return art

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(calculator_art())
    first = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
        
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        second = float(input("What's the next number?: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(first, second)
        
        print(f"{first} {operation_symbol} {second} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        
        if choice == 'y':
            first = answer
        else:
            should_continue = False

calculator()