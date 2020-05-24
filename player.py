from cards import Hand


class Player:
    def __init__(self, name, position, chips=1000):
        self.name = name
        self.position = position
        self.chips = chips
        self.hole = Hand()

    def __repr__(self):
        return f'{self.name}: {self.chips} chips. Cards in the hole: \n{self.hole}'

    def __sub__(self, other):
        return self.chips - other.chips

    def __add__(self, other):
        return self.chips + other.chips

    def move_chips(self, amount):
        self.chips -= amount


