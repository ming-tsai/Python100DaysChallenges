import random

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

def generate_password(letterLength, symbolLength, numberLength):
    password_list = []
    for letter in range(0, letterLength):
        password_list.append(random.choice(alphabet))
    for symbol in range(0, symbolLength):
        password_list.append(random.choice(symbols))
    for number in range(0, numberLength):   
        password_list.append(random.choice(numbers))  
    random.shuffle(password_list)
    return ''.join(password_list)

print("Welcome to the PyPassword Generator!")
letter_length = int(input("How many letters would you like in your password? "))
symbol_length = int(input("How many symbols would you like? "))
number_length = int(input("How many numbers would you like? "))
final_password = generate_password(letter_length, symbol_length, number_length)
print(f"Your generated password is: {final_password}")