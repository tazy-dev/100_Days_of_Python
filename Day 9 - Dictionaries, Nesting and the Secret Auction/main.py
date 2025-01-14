"""
    Blind Auction 
"""
def addNewBid (name,bid):
    return {
        'bidder_name': name,
        'bid':bid
    }
def getWinner (bids:list[object])->str:
    name = "",
    winningBid = -1000
    for bid in bids :
        if bid["bid"] > winningBid:
            name = bid["bidder_name"]
            winningBid = bid["bid"]
    return f"The winner is {name} with a bid of ${winningBid}"

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids = []
moreBidders = False
from os import system as sys
#os.system('cls')
print('Welcome to the secret auction program.')
print(logo)
while True :
    name = input ("What is your name?: ")
    bid = int (input ("What's your bid?: $"))
    bids.append(addNewBid(name,bid))
    nextBid = input ("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if nextBid  == "yes":
        sys('cls')
    else:
        break
sys('cls')
print(logo)
print(getWinner(bids))