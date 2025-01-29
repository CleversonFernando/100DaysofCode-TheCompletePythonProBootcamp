from sys import int_info
import art

print(art.logo)
bids = {}
add_new_bid = True

# TODO-4: Compare bids in dictionary
def check_the_bid(bids):
    grater_value = 0
    winner = ""
    for item in bids:
        new_bid = bids[item]
        if new_bid > grater_value:
            grater_value = new_bid
            winner = item
    print(f"the winner is {winner} with the value of ${grater_value}")

# TODO-1: Ask the user for input
while add_new_bid:
    name = input("What's your name?: \n")
    bid = int(input("What's your bid? $\n"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    confirmation = input("There is someone else to bid? Type 'yes' or 'no'").lower()
    if confirmation == "yes" or confirmation == "y":
        add_new_bid = True
        print("\n" * 20)
    else:
        add_new_bid = False
check_the_bid(bids)

