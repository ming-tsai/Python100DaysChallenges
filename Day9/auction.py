import art

print(art.logo)
print("Welcome to the secret auction program.")

bids = {}

def find_highest_bidder(bids):
    highest_bid = 0
    winner_name = ""

    for bidder_name in bids:
        if bids[bidder_name] > highest_bid:
            winner_name = bidder_name
            highest_bid = bids[bidder_name]

    print(f"The auction winner is {winner_name} with a bid of ${highest_bid:.2f}")

while True:
    name = input("What is your name? ")
    bid_amount = float(input("What is your bid? $"))
    bids[name] = bid_amount

    more_bidders = input("Are there other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "yes":
        print("\n" * 20)
    else:
        find_highest_bidder(bids)
        break