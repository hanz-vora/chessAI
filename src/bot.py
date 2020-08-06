# pylint: disable-all
from settings import *
from player import Player
import random
from math import floor


class bot(Player):
    def makeMove(self):
        piece = random.choice(self.pieces)
        return (piece.x,piece.y)
    def finishMove(self):
        x = floor(random.randint(0, 525 / 75)) * 75
        y = floor(random.randint(0, 525 / 75)) * 75
        return (x,y)