# head or tail
# import random

# print(random.randint(0, 1) == 0 and "heads" or "tails")
# def head_or_tail():
#     choice = input("Chose heads or tails: ").lower()
#     random_coin = random.choice(["heads", "tails"])
#     if choice == random_coin:
#         print(f"You win! The coin landed on {random_coin}.")
#     else:
#         print(f"You lose! The coin landed on {random_coin}.")

# head_or_tail()

# list of data structures
# unite_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky"] 
# print(unite_states[-1])

# import random

# friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# print(random.choice(friends) + " is going to buy the meal today!")

# fruits = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "kiwi", "pineapple"]
# vegetable = ["cucumber", "tomato", "pepper", "carrot", "lettuce", "broccoli", "spinach", "zucchini"]

# dirty_dozen = fruits + vegetable
# print(dirty_dozen)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen)

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
