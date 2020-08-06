# pylint: disable-all
from piece import *
from player import Player
from bot import bot

white_pawn = []
black_pawn = []

black_king = King("images/black_king.png", 300, 0, True, False)
black_queen = Queen("images/black_queen.png", 225, 0, True, False)

black_rook_1 = Rook("images/black_rook.png", 0, 0, True, False)
black_rook_2 = Rook("images/black_rook.png", 525, 0, True, False)

black_bishop_1 = Bishop("images/black_bishop.png", 150, 0, True, False)
black_bishop_2 = Bishop("images/black_bishop.png", 375, 0, True, False)

black_knight_1 = Knight("images/black_knight.png", 75, 0, True, False)
black_knight_2 = Knight("images/black_knight.png", 450, 0, True, False)

for i in range(0, 8):
    black_pawn.append(BlackPawn("images/black_pawn.png", i * 75, 75, True, False))

white_king = King("images/white_king.png", 300, 525, True, True)
white_queen = Queen("images/white_queen.png", 225, 525, True, True)

white_rook_1 = Rook("images/white_rook.png", 0, 525, True, True)
white_rook_2 = Rook("images/white_rook.png", 525, 525, True, True)

white_bishop_1 = Bishop("images/white_bishop.png", 150, 525, True, True)
white_bishop_2 = Bishop("images/white_bishop.png", 375, 525, True, True)

white_knight_1 = Knight("images/white_knight.png", 75, 525, True, True)
white_knight_2 = Knight("images/white_knight.png", 450, 525, True, True)

for i in range(0, 8):
    white_pawn.append(WhitePawn("images/white_pawn.png", i * 75, 450, True, True))

Player1 = Player(
    True,
    [
        white_king,
        white_queen,
        white_rook_1,
        white_rook_2,
        white_bishop_1,
        white_bishop_2,
        white_knight_1,
        white_knight_2,
    ]
    + white_pawn,
    True,
)
Player2 = bot(
    False,
    [
        black_king,
        black_queen,
        black_rook_1,
        black_rook_2,
        black_bishop_1,
        black_bishop_2,
        black_knight_1,
        black_knight_2,
    ]
    + black_pawn,
    True,
)
