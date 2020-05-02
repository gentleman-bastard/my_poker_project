from cards import Card, Deck, Hand
from player import Player
import logging
from itertools import combinations



deck = Deck()


deck.shuffle()

number_of_players = int(input("How many people will be playing?\n"))

players = {f'Player {x+1}':Player() for x in range(number_of_players)}

print("the following people will be playing:")
print(players)


for player_name, player_object in players.items():
    deck.move_cards(player_object.hole, 2)
    print(f'{player_name} has:\n {player_object.hole}')

pot = 0

for player, player_object in players.items():
    amount = int(input(f"{player}:\nHow much would you like to bet?\n"))
    player_object.bet(amount, pot)

print(f'There is now ${pot} in the pot')


"""
dead = Hand()
table = Hand()

deck.move_cards(dead, 1)
deck.move_cards(table, 3)
print(f'the flop: \n{table}')

deck.move_cards(dead, 1)
deck.move_cards(table, 1)
print(f'after the turn: /n{table}')

deck.move_cards(dead, 1)
deck.move_cards(table, 1)
print(f'after the river: /n{table}')
"""






