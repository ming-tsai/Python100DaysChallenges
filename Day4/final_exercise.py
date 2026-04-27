import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def rock_paper_scissors():
    options = [rock, paper, scissors]
    wins = {(0, 2), (1, 0), (2, 1)}

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

    if user_choice not in range(3):
        print("Invalid choice, you lose!")
        return

    computer_choice = random.randrange(len(options))

    print(f"Your choice:\n{options[user_choice]}")
    print(f"Computer's choice:\n{options[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice, computer_choice) in wins:
        print("You win! 🎉")
    else:
        print("You lose! 😢")

if __name__ == "__main__":
    rock_paper_scissors()