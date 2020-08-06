# pylint: disable-all
from settings import *

def check_black(x, y, win, func):
    if black_king.rect.collidepoint(x, y):
        func(black_king, win)
        return True
    elif black_queen.rect.collidepoint(x, y):
        func(black_queen, win)
        return True
    elif black_rook_1.rect.collidepoint(x, y):
        func(black_rook_1, win)
        return True
    elif black_rook_2.rect.collidepoint(x, y):
        func(black_rook_2, win)
        return True
    elif black_knight_1.rect.collidepoint(x, y):
        func(black_knight_1, win)
        return True
    elif black_knight_2.rect.collidepoint(x, y):
        func(black_knight_2, win)
        return True
    elif black_bishop_1.rect.collidepoint(x, y):
        func(black_bishop_1, win)
        return True
    elif black_bishop_2.rect.collidepoint(x, y):
        func(black_bishop_2, win)
        return True
    else:
        for pawn in black_pawn:
            if pawn.rect.collidepoint(x, y):
                func(pawn, win)
                return True
    return False


def check_white(x, y, win, func):
    if white_king.rect.collidepoint(x, y):
        func(white_king, win)
        return True
    elif white_queen.rect.collidepoint(x, y):
        func(white_queen, win)
        return True
    elif white_rook_1.rect.collidepoint(x, y):
        func(white_rook_1, win)
        return True
    elif white_rook_2.rect.collidepoint(x, y):
        func(white_rook_2, win)
        return True
    elif white_knight_1.rect.collidepoint(x, y):
        func(white_knight_1, win)
        return True
    elif white_knight_2.rect.collidepoint(x, y):
        func(white_knight_2, win)
        return True
    elif white_bishop_1.rect.collidepoint(x, y):
        func(white_bishop_1, win)
        return True
    elif white_bishop_2.rect.collidepoint(x, y):
        func(white_bishop_2, win)
        return True
    else:
        for pawn in white_pawn:
            if pawn.rect.collidepoint(x, y):
                func(pawn, win)
                return True
    return False