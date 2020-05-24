from game import Game
import pytest


def test_game():
    game_test = Game(['Ross', 'Stew', 'Alex', 'Johnny'], 25, 50)

    assert len(game_test.players) == 4
    assert game_test.players[0].name == 'Ross'



