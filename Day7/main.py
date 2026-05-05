import random
from hangman_art import stages, logo      # Angela's ASCII art!
from hangman_words import word_list

def hangman():
    word_to_guess = random.choice(word_list).lower()
    guessed_letters = set()   # ✅ set = no duplicates ever
    lives = 6

    print(logo)

    while True:
        # Build display
        display = ' '.join(
            letter if letter in guessed_letters else '_'
            for letter in word_to_guess
        )
        print(f"\nWord: {display}")
        print(stages[lives])

        # Check win
        if all(letter in guessed_letters for letter in word_to_guess):
            print("🎉 You Win!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            lives -= 1
            print(f"'{guess}' is not in the word. {lives} lives remaining.")

        if lives == 0:
            print(f"💀 You Lose! The word was '{word_to_guess}'")
            break

if __name__ == "__main__":
    hangman()