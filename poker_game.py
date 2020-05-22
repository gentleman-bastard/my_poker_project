from cards import Deck
from player import Player as Player
import logging
from typing import List, Set, Dict, Tuple
import datetime
from itertools import combinations

class Game(object):
    def __init__(self, logger: logging.getLogger(),player_names: List[str], small_blind: int, big_blind: int):
        self.logger = logger
        self.flop = []
        self.turn = []
        self.river = []
        self.dead = []
        self.deck = Deck()
        self.player_names = player_names
        self.pot = 0

    @property
    def players(self):
        return [Player(player_name) for player_name in self.player_names]

    @property
    def table_cards(self):
        flop_plus_turn = self.flop.extend(self.turn)
        return flop_plus_turn.extend(self.river)

    def deal_preflop(self, players):
        """deals 2 pre flop (hole) cards to each player"""
        for i in range(2):
            for player in players:
                self.deck.move_cards(player.hole, 1)

    def deal_table_cards(self, n, dead_n):
        self.deck.move_cards(self.dead, dead_n)
        self.deck.move_cards(self.flop,n)









logger = logging.getLogger('pokergame')
logger.setLevel(logging.DEBUG)

deck = Deck()


deck.shuffle()


names = ['Ross', 'Stew', 'Alex', 'Johnny']



players = [Player(name) for name in names]

print("the following people will be playing:")
for player in players:
    print(player.name)

#TODO: deal one card at a time and circle twice
logger.debug('dealing hole cards to each player')
for player in players:
    deck.move_cards(player.hole, 2)



for player in players:
    print(f'{player}')


logger.debug('dealing flop')










