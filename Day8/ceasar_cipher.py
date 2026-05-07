import string

# Full alphabet (a-z)
alphabet_list = list(string.ascii_lowercase)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ''
    for text in original_text:
        if text in alphabet_list:
            shifted_position = alphabet_list.index(text) + shift_amount
            shifted_position %= len(alphabet_list)
            cipher_text += alphabet_list[shifted_position]
        else:
            cipher_text += text

    print(f"Here is the encode result: {cipher_text}")

encrypt(text, shift)
