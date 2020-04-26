from cards import Hand


class Player(object):
    def __init__(self, chips = 1000, hole = Hand()):
        self.chips = chips
        self.hole = hole

    def __repr__(self):
        return f'Poker Player: {self.chips} chips. Cards in the hole: \n{self.hole}'