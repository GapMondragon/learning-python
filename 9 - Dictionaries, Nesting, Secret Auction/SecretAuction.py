
# Visualize your code here
# https://pythontutor.com/visualize.html#mode=display

from ArtSecretAuction import logo
print(logo)

def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)

bids = {}
more_bidders = True

while more_bidders == True:
   print("Welcome to the secret auction program.")
   name = input("What is your name? ")
   bid = input("What is your bid? $")

   bids[name] = int(bid) 

   other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
   if other_bidders == "no":
      more_bidders = False
   clear()


highestbidder = ""
highestbid = 0

for bidder in bids:
   # print(bidder)
   # print(bids[bidder])
   if bids[bidder] > highestbid:
      highestbidder = bidder
      highestbid = bids[bidder]



print("Secret Auction Over.")
print(f"The highest bidder is: {highestbidder} with a bid of ${highestbid}")
print("Congratulations!!!")
# print(bids)