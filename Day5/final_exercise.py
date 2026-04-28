import random
import string

def generate_password(letter_length, symbol_length, number_length):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    
    password_list = (
        [random.choice(string.ascii_lowercase) for _ in range(letter_length)] +
        [random.choice(symbols) for _ in range(symbol_length)] +
        [random.choice(string.digits) for _ in range(number_length)]
    )
    
    random.shuffle(password_list)
    return ''.join(password_list)

print("Welcome to the PyPassword Generator!")
letter_length = int(input("How many letters would you like in your password? "))
symbol_length = int(input("How many symbols would you like? "))
number_length = int(input("How many numbers would you like? "))

print(f"Your generated password is: {generate_password(letter_length, symbol_length, number_length)}")