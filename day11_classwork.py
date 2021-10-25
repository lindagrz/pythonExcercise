import itertools
import random


# 1. The Shuffle
# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A",
# "spades ♠"), ("A", "clubs ♣")]
# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.
# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html


def get_new_deck():
    values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    suits = ["spades ♠", "clubs ♣", "hearts ♥", "diamonds ♦"]
    # cards = [(value, suit) for value in values for suit in suits]  # an another way to do it
    cards = list(itertools.product(values, suits))
    return cards


def get_shuffled_cards(cards=get_new_deck()):
    return random.sample(cards, k=len(cards))


# 2. Deck
# write a class Deck with the following attributes(variables)
# available - contains list of card tuples that can be used
# spent - contains list of card tuples that have been used
# there should be following methods:
# constructor (__init__) method
# initializes available with full 52 card list of tuples
# initializes spent with empty list
# shuffle(self):
# # shuffles available cards - works just like 1st function but works on available
# get_cards(self, count=1):
# # gets some number(default 1) of cards from available
# adds these cards to spent
# returns these cards
# # you can add other methods and/or attributes if you wish to Deck class

class Deck:
    def __init__(self, available=get_new_deck(), spent=None):
        if spent is None:
            spent = []
        self.available = available
        self.spent = spent

    def reset(self):
        self.__init__()

    def shuffle(self):
        self.available = get_shuffled_cards(self.available)
        return self

    def get_cards(self, count=1):
        draw = self.available[:count]
        for card in draw:
            self.available.remove(card)
            self.spent.append(card)
        return draw


# 3. create a new deck in a different .py file from where Deck() is located, that means use import !

import day11_u3_module as d11


def main():
    # print(get_shuffled_cards())
    new_deck = Deck()
    hand = new_deck.get_cards(4)
    print("Picked up: ", hand)
    print("Discard pile: ", new_deck.spent)  # that's cheating, the deck is not shuffled here
    print()

    new_deck.reset()
    new_deck.shuffle()
    hand = new_deck.get_cards(2)
    print("Picked up: ", hand)
    print("Discard pile: ", new_deck.spent)
    hand = new_deck.get_cards()
    print("Picked up: ", hand)
    print("Discard pile: ", new_deck.spent)
    print()

    u3_deck = d11.Deck()
    u3_deck.shuffle()
    u3 = u3_deck.get_cards(2)
    print("Picked up: ", u3)
    print("Discard pile: ", u3_deck.spent)
    u3 = u3_deck.get_cards(3)
    print("Picked up: ", u3)
    print("Discard pile: ", u3_deck.spent)


if __name__ == "__main__":
    main()
