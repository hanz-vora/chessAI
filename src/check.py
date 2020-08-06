# pylint: disable-all
from settings import *
import board
from checkCollision import *
import firstSetup

def update_board_temp(win):
    lis  = Player1.pieces + Player2.pieces

    for piece in lis:
        piece.update_moves(win)

def noCheck(piece, x, y, win):
    temp_x, temp_y = piece.x, piece.y
    piece.set_rect(x, y)

    if Player1.isTurn:
        check_black(x, y, win, tempDel)
    else:
        check_white(x, y, win, tempDel)

    update_board_temp(win)

    lis = Player2.pieces if Player1.isTurn else Player1.pieces
    king = Player2.pieces[0] if not Player1.isTurn else Player1.pieces[0]

    for item in lis:
        for square in item.check:
            if king.x == square[0] and king.y == square[1]:
                piece.set_rect(temp_x, temp_y)
                firstSetup.firstSetup(win)
                return False
    piece.set_rect(temp_x, temp_y)
    firstSetup.firstSetup(win)
    return True

def possibleKingMoves(mx,my):
    lis = Player2.pieces if Player1.isTurn else Player1.pieces
    king = Player2.pieces[0] if not Player1.isTurn else Player1.pieces[0]

    for item in lis:
        for square in item.check:
            if mx == square[0] and my == square[1]:
                return False
    return True


def tempDel(piece, win):
    piece.check = []
    piece.take_piece_temp()
