from cards import Deck
from player import Player as Player
from typing import List, Set, Dict, Tuple
import datetime
from itertools import combinations
import random

class Game(object):
    def __init__(self, player_names: List[str], small_blind: int, big_blind: int):
        self.flop = []
        self.turn = []
        self.river = []
        self.dead = []
        self.deck = Deck()
        self.player_names = player_names
        self.pot = 0
        self.small_blind = small_blind
        self.big_blind = big_blind
        self. turn_count = 0
        self.dealer_position = 0

    @property
    def players(self):
        return [Player(player_name) for player_name in self.player_names]

    @property
    def table_cards(self):
        flop_plus_turn = self.flop.extend(self.turn)
        return flop_plus_turn.extend(self.river)

    @property
    def small_blind_position(self) -> int:
        return self.dealer_position+1

    @property
    def big_blind_position(self) -> int:
        return self.small_blind_position+1

    def move_blinds(self):
        self.dealer_position += 1

    def deal_preflop(self, players):
        """deals 2 pre flop (hole) cards to each player"""
        for i in range(2):
            for player in players:
                self.deck.move_cards(player.hole, 1)

    def deal_table_cards(self, n, dead_n):
        self.deck.move_cards(self.dead, dead_n)
        self.deck.move_cards(self.flop,n)

    def _collect_blinds(self):
        """invokes the Player method move_chips to move the blinds from the the players chip value to the pot"""
        # TODO: review blind methodology. Perhaps assign a player to blinds rather than a position
        small_blind_player = self.players[self.small_blind_position]
        big_blind_player = self.players[self.big_blind_position]
        small_blind_player.move_chips(self.small_blind, small_blind_player.chips, self.pot)
        big_blind_player.move_chips(self.big_blind, big_blind_player.chips, self.pot)



