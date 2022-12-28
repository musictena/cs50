# to simulate a coin toss using the random library

import random # radnom library

# coin = random.choice(["head", "tails"]) #sqwuare brackets indicate a list
# print(coin)

# number = random.randint(1, 10)
# print (number)

cards = ["jack", "king", "queen"]
random.shuffle(cards)
for card in cards:
    print(card)


