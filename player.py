from cards import Hand


class Player(object):
    def __init__(self, name, chips = 1000, hole = Hand()):
        self.name = name
        self.chips = chips
        self.hole = hole

    def __repr__(self):
        return f'{self.name}: {self.chips} chips. Cards in the hole: \n{self.hole}'

    def bet(self, amount, pot):
        self.chips - amount
        pot + amount

