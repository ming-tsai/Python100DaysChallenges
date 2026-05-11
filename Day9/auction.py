import art

print(art.logo)
print("Welcome to the secret auction program.")

close_auction = False
bidded_dictionary = {}
    
while not close_auction:
    name = input("What is your name? ")
    bidded = float(input("What is your bid? $"))
    bidded_dictionary[name] = bidded

    has_more_bid = input("Are there other users who want to bid? Yes or ").lower()
    if has_more_bid == "yes":
        print("\n" * 20)
    else:
        maxed = 0
        maxed_name = ""
        for bidded_name in bidded_dictionary:
            if bidded_dictionary[bidded_name] > maxed:
                maxed_name = bidded_name
                maxed = bidded_dictionary[bidded_name]

        print(f"This auction winner is {maxed_name}, with amout {maxed}")
        close_auction = True