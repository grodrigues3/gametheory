"""
Run simulations to calculate the expected revenue earned from auctions with
various constraints.
"""
import random
NUM_TRIALS = 1000

"""
2 bidder vickery auction uniform (0,1] bids, 1 item
What is the expected revenue from a vickery auction 
with the above parameters?
"""
total = 0
for _ in range(NUM_TRIALS):
    b1 = random.random()
    b2 = random.random()
    total += min(b1,b2)
print ("Simulation 1")
print("\tExpected Vickery = ", total/NUM_TRIALS)


"""
2 bidder vickery auction uniform (0,1] bids, 1 item, reserve = 1/2
The reserve value is a floor on the price we are willing to sell the item at.
If both bids are below the reserve value, we do NOT sell the item.  If both
bids are above the reserve value, the highest bidder wins and pays the second
bidders bid.  If one bid is above the reserve value, the highest bidder wins
and pays the reserve value
"""
total = 0
sold = 0
reserve = 1/2.0
for _ in range(NUM_TRIALS):
    b1 = random.random()
    b2 = random.random()
    high_bid = max(b1,b2)
    low_bid = min(b1,b2)
    if high_bid < reserve:
        # we don't sell if neither bid meets the reserve
        continue
    else:
        total += max(reserve, low_bid)
        sold += 1

print ("Simulation 2")
print("\tWith the reserve set to {}, out of {} attempts, we sold the item {} \
times".format(reserve, NUM_TRIALS, sold))
print("\tExpected Vickery with 1/2 reserve= ", total/NUM_TRIALS)
