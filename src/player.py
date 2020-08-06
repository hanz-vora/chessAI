# pylint: disable-all
from settings import *

class Player():
    def __init__(self, white, lis, human):
        self.isTurn = white
        self.pieces = lis
        self.isHuman = human
    
    def makeMove(self):
        self.isTurn = not(self.isTurn)
    
    def losePiece(self, piece):
        self.pieces.remove(piece)

