import art
from os import system
print(art.logo)

auction = {}

finished_bidding = False


def highest_bid(biding_records):
    highest_bids = 0
    winner = ''
    for bids in biding_records:
        bids_amount = biding_records[bids]
        if bids_amount > highest_bids:
            highest_bids = bids_amount
            winner = bids
    print(f"The winner is {winner} with bid = ${highest_bids}")


while not finished_bidding:
    users_name = input("Enter your name: ")
    bid_price = int(input("Amount you will Bid: $"))
    auction[users_name] = bid_price

    another_user = input("is there any other user: ").lower()

    if another_user == "no":
        finished_bidding = True
        highest_bid(auction)
    elif another_user == "yes":
        system("clear")
    else:
        print("Wrong input")

