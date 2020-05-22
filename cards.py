from functools import total_ordering
import random


@total_ordering
class Card(object):
    """represents a standard playing card"""
    suit_names = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank



class Deck(object):
    """creates a deck of 52 cards"""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def shuffle(self):
        return random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())



class Hand(Deck):
    """represents a hand of cards"""
    def __init__(self, label = ''):
        self.cards = []
        self.label = label


