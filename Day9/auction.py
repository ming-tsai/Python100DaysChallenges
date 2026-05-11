import art

print(art.logo)
print("Welcome to the secret auction program.")

close_auction = False
bider_dictionary = {}
    
def find_higest_bider(bider_dictionary):
    maxed = 0
    maxed_name = ""
    for bidded_name in bider_dictionary:
        if bider_dictionary[bidded_name] > maxed:
            maxed_name = bidded_name
            maxed = bider_dictionary[bidded_name]

    print(f"This auction winner is {maxed_name}, with amout {maxed}")

while not close_auction:
    name = input("What is your name? ")
    bider = float(input("What is your bid? $"))
    bider_dictionary[name] = bider

    has_more_bider = input("Are there other users who want to bid? Type 'Yes' or ").lower()
    if has_more_bider == "yes":
        print("\n" * 20)
    else:
        find_higest_bider(bider_dictionary)
        close_auction = True