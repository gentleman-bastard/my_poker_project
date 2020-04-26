from cards import Card, Deck, Hand
from player import Player
import logging
from itertools import combinations



deck = Deck()


deck.shuffle()

number_of_players = int(input("How many people will be playing?"))

players = {f'player_{x}':Player() for x in range(number_of_players)}

print("the following people will be playing:")
print(players)


player1 = Hand()
player2 = Hand()


players = [player1,player2]


for num,player in enumerate(players):
    deck.move_cards(player, 2)
    print(f'player {num+1} has {player} in their hand')




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







