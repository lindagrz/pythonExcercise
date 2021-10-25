import itertools
import random


def get_new_deck():
    values = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    suits = ["spades ♠", "clubs ♣", "hearts ♥", "diamonds ♦"]
    # cards = [(value, suit) for value in values for suit in suits]  # an another way to do it
    cards = list(itertools.product(values, suits))
    return cards


def get_shuffled_cards(cards=get_new_deck()):
    return random.sample(cards, k=len(cards))


class Deck:
    def __init__(self, available=get_new_deck(), spent=[]):
        self.available = available
        self.spent = spent

    def shuffle(self):
        self.available = get_shuffled_cards(self.available)
        return self

    def get_cards(self, count=1):
        draw = self.available[:count]
        for card in draw:
            self.available.remove(card)
            self.spent.append(card)
        return draw
