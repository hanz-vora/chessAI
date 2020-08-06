# pylint: disable-all
from settings import *

def fillPieces(win, piece):
    if piece.to_restore:
        piece.restore_piece()
    if piece.show:
        win.blit(piece.img, (piece.x, piece.y))
        piece.update_moves(win)


def firstSetup(win):
    fillPieces(win, black_rook_1)
    fillPieces(win, black_rook_2)
    fillPieces(win, black_knight_1)
    fillPieces(win, black_knight_2)
    fillPieces(win, black_bishop_1)
    fillPieces(win, black_bishop_2)
    fillPieces(win, black_queen)
    fillPieces(win, black_king)

    fillPieces(win, white_rook_1)
    fillPieces(win, white_rook_2)
    fillPieces(win, white_knight_1)
    fillPieces(win, white_knight_2)
    fillPieces(win, white_bishop_1)
    fillPieces(win, white_bishop_2)
    fillPieces(win, white_queen)
    fillPieces(win, white_king)

    for i in range(0,8):
        fillPieces(win, white_pawn[i])
        fillPieces(win, black_pawn[i])