from cards import Hand

class Player:
    def __init__(self, name, chips = 1000):
        self.name = name
        self.chips = chips
        self.hole = Hand()

    def __repr__(self):
        return f'{self.name}: {self.chips} chips. Cards in the hole: \n{self.hole}'

    def move_chips(self, amount, source, target):
        source -= amount
        target += amount


