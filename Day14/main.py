from game_data import data
import random

def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account["name"]
    description = account["description"]
    return f"{name}: {description}"

def main():
    chosen_a = random.choice(data)
    chosen_b = random.choice(data)
    print(f"Compare A: {format_data(chosen_a)}")
    print("VS")
    print(f"Compare B: {format_data(chosen_b)}")
    value = input(f"Which account has more flowers? Type 'A' or 'B': ").upper()
    if (value == 'A' and chosen_a['flower_count'] > chosen_b['flower_count']) or (value == 'B' and chosen_b['flower_count'] > chosen_a['flower_count']):
        print("Correct!")
        main()
    else:
        print("Incorrect!")

if __name__ == "__main__":
    main()