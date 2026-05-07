import string
import art

print(art.logo)

alphabet_list = list(string.ascii_lowercase)

def caesar_cipher(value, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount *= -1  # ✅ flip once, outside the loop

    result = ''
    for character in value:
        if character in alphabet_list:
            shifted_position = (alphabet_list.index(character) + shift_amount) % len(alphabet_list)
            result += alphabet_list[shifted_position]
        else:
            result += character  # keep spaces, punctuation as-is

    print(f"Here is the {encode_or_decode}d result: {result}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)

    if input("\nType 'yes' to go again: ").lower() != 'yes':
        break

print("Goodbye! 👋")