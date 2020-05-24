from game import Game





def run():
    n_players = int(input("How many people will be playing?\n"))
    player_names = [input("What is your name?\n") for i in range(n_players)]
    game = Game(player_names, 10, 20)
    game.run()




if __name__ == '__main__':
    run()


