# Hangman game
import random;

words = ["banana"]

word_to_guess = random.choice(words).lower()

display = ''

for g in range(0, len(word_to_guess)):
    display += '_'

print(display)

game_end = False
life = 6

word_guessed = []

while not game_end:
    guess=input("What letter you want to guess?").lower()

    display = ''
    for letter in word_to_guess:
        if letter == guess:
            display += guess
            word_guessed.append(guess)
        elif letter in word_guessed:
            display += letter
        else:
            display +='_'

    print(display)
    if guess not in word_guessed:
        life -= 1
        print(f"You have {str(life)} life to try")

    if len(word_guessed) == len(word_to_guess):
        game_end = True
        print("You Win!")
    elif life == 0:
        game_end = True
        print("You Loss")

