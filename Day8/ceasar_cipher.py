import string
import art

print(art.logo)

# Full alphabet (a-z)
alphabet_list = list(string.ascii_lowercase)

closed = False
while not closed:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceasar_cipher(value, shift_amount, encode_or_decode):
        result = ''
        if encode_or_decode == "decode":
            shift_amount *= -1
            
        for characters in value:
            if characters in alphabet_list:
                shifted_position = alphabet_list.index(characters) + shift_amount
                shifted_position %= len(alphabet_list)
                result += alphabet_list[shifted_position]
            else:
                result += characters
        print(f"Here is the {encode_or_decode}d result: {result}")

    ceasar_cipher(text, shift, direction)

    want_to_go = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if not want_to_go.lower() == 'yes':
        closed = True

print("Good Bye!")