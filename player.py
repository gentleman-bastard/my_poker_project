from cards import Hand

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hole = Hand()

    def __repr__(self):
        return f'{self.name}: {self.chips} chips. Cards in the hole: \n{self.hole}'

    def move_chips(self, amount):
        self.chips -= amount



player = Player('Ross', 1000)


print(player)

player.move_chips(500)

print(player)