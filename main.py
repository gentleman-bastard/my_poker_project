from game import Game
from logging import getLogger

class GameRunner:
    def __init__(self, logger = getLogger('PokerGame')):
        self.logger = logger

    def run(self):
        n_players = input("How many people will be playing?")
        player_names = [input("What is your name?") for n in n_players]

        self.logger.debug('instantiating game instance')
        game = Game(getLogger('game_log'), player_names, 10, 20)




if __name__ == '__main__':
    GameRunner.run()


