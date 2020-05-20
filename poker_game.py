from cards import Card, Deck, Hand
from player import Player
import logging
from itertools import combinations



deck = Deck()


deck.shuffle()


names = ['Ross', 'Stew', 'Alex', 'Johnny']

players = [Player(name) for name in names]

print("the following people will be playing:")
for player in players:
    print(player.name)


for player in players:
    deck.move_cards(player.hole, 2)

for player in players:
    print(f'{player.name} has:\n {player.hole}')




pot = 0

for player in players:
    amount = int(input(f"{player}:\nHow much would you like to bet?\n"))
    player.bet(amount, pot)

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






