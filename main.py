from game import Game
from logging import getLogger

def main():
    n_players = input("How many people will be playing?")
    player_names = [input("What is your name?") for n in n_players]

    game = Game(getLogger('game_log'), player_names, 10, 20)
