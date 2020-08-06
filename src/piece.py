# pylint: disable-all
import pygame
from settings import *


class Piece(object):
    def __init__(self, path, x, y, show, white):
        self.img = pygame.transform.scale(pygame.image.load(path), (75, 75))
        self.x = x
        self.y = y
        self.rect = self.img.get_rect()
        self.rect.center = (x + 35, y + 35)
        self.rect.size = (75, 75)
        self.show = show
        self.moves = []
        self.check = []
        self.isWhite = white
        self.to_restore = False
        self.restore_x = x
        self.restore_y = y

    def set_rect(self, x, y):
        self.x = x
        self.y = y
        self.restore_x = x
        self.restore_y = y
        self.rect.center = (x + 35, y + 35)

    def take_piece(self):
        from settings import Player1, Player2

        self.show = False
        self.x = -1
        self.y = -1
        self.rect.size = (0, 0)
        self.moves = []
        self.check = []
        if self.isWhite:
            Player1.losePiece(self)
        else:
            Player2.losePiece(self)

    def take_piece_temp(self):
        self.show = False
        self.x = -1
        self.y = -1
        self.rect.size = (0, 0)
        self.moves = []
        self.check = []
        self.to_restore = True

    def restore_piece(self):
        self.show = True
        self.x = self.restore_x
        self.y = self.restore_y
        self.rect.size = (75, 75)
        self.to_restore = False


class King(Piece):
    def legal_move(self, mx, my, win):
        if (
            abs(mx - self.x) > 75
            or abs(my - self.y) > 75
            or (mx == self.x and my == self.y)
        ):
            return False
        return True

    def update_moves(self, win):
        from checkCollision import check_black, check_white
        from check import possibleKingMoves

        self.moves = []

        var = check_white if self.isWhite else check_black

        if not isCollision(self.x + 75, self.y, win, var) and possibleKingMoves(
            self.x + 75, self.y
        ):
            self.moves.append((self.x + 75, self.y))
        if not isCollision(self.x + 75, self.y + 75, win, var) and possibleKingMoves(
            self.x + 75, self.y + 75
        ):
            self.moves.append((self.x + 75, self.y + 75))
        if not isCollision(self.x + 75, self.y - 75, win, var) and possibleKingMoves(
            self.x + 75, self.y - 75
        ):
            self.moves.append((self.x + 75, self.y - 75))
        if not isCollision(self.x, self.y + 75, win, var) and possibleKingMoves(
            self.x, self.y + 75
        ):
            self.moves.append((self.x, self.y + 75))
        if not isCollision(self.x, self.y - 75, win, var) and possibleKingMoves(
            self.x, self.y - 75
        ):
            self.moves.append((self.x, self.y - 75))
        if not isCollision(self.x - 75, self.y - 75, win, var) and possibleKingMoves(
            self.x - 75, self.y - 75
        ):
            self.moves.append((self.x - 75, self.y - 75))
        if not isCollision(self.x - 75, self.y, win, var) and possibleKingMoves(
            self.x - 75, self.y
        ):
            self.moves.append((self.x - 75, self.y))
        if not isCollision(self.x - 75, self.y + 75, win, var) and possibleKingMoves(
            self.x - 75, self.y + 75
        ):
            self.moves.append((self.x - 75, self.y + 75))
        self.check = self.moves


class Bishop(Piece):
    def legal_move(self, mx, my, win):
        from checkCollision import check_black, check_white

        if abs(self.x - mx) != abs(self.y - my) or (self.x == mx and self.y == my):
            return False
        dl = sign(mx - self.x)
        dc = sign(my - self.y)

        x, y = self.x + dl, self.y + dc

        while x != mx and y != my:
            if check_black(x, y, win, nothing) or check_white(x, y, win, nothing):
                return False
            x += dl
            y += dc
        return True

    def update_moves(self, win):
        from checkCollision import check_black, check_white

        self.moves = []

        var = check_white if self.isWhite else check_black
        var2 = check_white if not self.isWhite else check_black

        i, j = self.x + 75, self.y + 75
        while i < 600 and j < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j += 75
            i += 75

        i, j = self.x - 75, self.y - 75
        while i >= 0 and j >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j -= 75
            i -= 75

        i, j = self.x - 75, self.y + 75
        while i >= 0 and j < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j += 75
            i -= 75

        i, j = self.x + 75, self.y - 75
        while i < 600 and j >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j -= 75
            i += 75

        self.check = self.moves


class Rook(Piece):
    def legal_move(self, mx, my, win):
        from checkCollision import check_black, check_white

        if (self.x == mx and self.y == my) or (self.x != mx and self.y != my):
            return False
        if self.x == mx:
            for i in range(min(self.y, my) + 75, max(self.y, my), 75):
                if check_white(mx, i, win, nothing) or check_black(mx, i, win, nothing):
                    return False
        elif self.y == my:
            for i in range(min(self.x, mx) + 75, max(self.x, mx), 75):
                if check_white(i, my, win, nothing) or check_black(i, my, win, nothing):
                    return False
        return True

    def update_moves(self, win):
        from checkCollision import check_black, check_white

        self.moves = []

        var = check_white if self.isWhite else check_black
        var2 = check_white if not self.isWhite else check_black

        i, j = self.x + 75, self.y
        while i < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            i += 75

        i, j = self.x - 75, self.y
        while i >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            i -= 75

        i, j = self.x, self.y + 75
        while j < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j += 75

        i, j = self.x, self.y - 75
        while j >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j -= 75

        self.check = self.moves


class Queen(Piece):
    def legal_move(self, mx, my, win):
        from checkCollision import check_black, check_white

        if (self.x == mx and self.y == my) or (
            abs(self.x - mx) != abs(self.y - my) and (self.x != mx and self.y != my)
        ):
            return False

        if self.x == mx:
            for i in range(min(self.y, my) + 75, max(self.y, my), 75):
                if check_white(mx, i, win, nothing) or check_black(mx, i, win, nothing):
                    return False
        elif self.y == my:
            for i in range(min(self.x, mx) + 75, max(self.x, mx), 75):
                if check_white(i, my, win, nothing) or check_black(i, my, win, nothing):
                    return False
        else:
            dl = sign(mx - self.x)
            dc = sign(my - self.y)

            x, y = self.x + dl, self.y + dc

            while x != mx and y != my:
                if check_black(x, y, win, nothing) or check_white(x, y, win, nothing):
                    return False
                x += dl
                y += dc

        return True

    def update_moves(self, win):
        from checkCollision import check_black, check_white

        self.moves = []

        var = check_white if self.isWhite else check_black
        var2 = check_white if not self.isWhite else check_black

        i, j = self.x + 75, self.y + 75
        while i < 600 and j < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j += 75
            i += 75

        i, j = self.x - 75, self.y - 75
        while i >= 0 and j >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j -= 75
            i -= 75

        i, j = self.x - 75, self.y + 75
        while i >= 0 and j < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j += 75
            i -= 75
            var = check_white if self.isWhite else check_black
        var2 = check_white if not self.isWhite else check_black

        i, j = self.x + 75, self.y
        while i < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            i += 75

        i, j = self.x - 75, self.y
        while i >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            i -= 75

        i, j = self.x, self.y + 75
        while j < 600:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j += 75

        i, j = self.x, self.y - 75
        while j >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j -= 75

        i, j = self.x + 75, self.y - 75
        while i < 600 and j >= 0:
            if not isCollision(i, j, win, var):
                self.moves.append((i, j))
            else:
                break
            if isCollision(i, j, win, var2):
                break
            j -= 75
            i += 75

        self.check = self.moves


class Knight(Piece):
    def legal_move(self, mx, my, win):
        if not (abs(self.x - mx) == 75 and abs(self.y - my) == 150) and not (
            abs(self.x - mx) == 150 and abs(self.y - my) == 75
        ):
            return False
        return True

    def update_moves(self, win):
        from checkCollision import check_black, check_white

        self.moves = []

        var = check_white if self.isWhite else check_black

        if not isCollision(self.x + 75, self.y + 150, win, var):
            self.moves.append((self.x + 75, self.y + 150))
        if not isCollision(self.x + 150, self.y + 75, win, var):
            self.moves.append((self.x + 150, self.y + 75))
        if not isCollision(self.x + 150, self.y - 75, win, var):
            self.moves.append((self.x + 150, self.y - 75))
        if not isCollision(self.x + 75, self.y - 150, win, var):
            self.moves.append((self.x + 75, self.y - 150))
        if not isCollision(self.x - 75, self.y + 150, win, var):
            self.moves.append((self.x - 75, self.y + 150))
        if not isCollision(self.x - 150, self.y + 75, win, var):
            self.moves.append((self.x - 150, self.y + 75))
        if not isCollision(self.x - 150, self.y - 75, win, var):
            self.moves.append((self.x - 150, self.y - 75))
        if not isCollision(self.x - 75, self.y - 150, win, var):
            self.moves.append((self.x - 75, self.y - 150))
        self.check = self.moves


class WhitePawn(Piece):
    def legal_move(self, mx, my, win):
        from checkCollision import check_black, check_white

        if check_black(mx, my, win, nothing) or check_white(mx, my, win, nothing):
            if self.y - my != 75 or abs(self.x - mx) != 75:
                return False
            else:
                return True
        if self.x != mx:
            return False
        elif self.y - my > 150 or self.y <= my:
            return False
        elif (self.y - my > 75 and self.y != 450) or (
            check_black(mx, (self.y + my) / 2, win, nothing)
            or check_white(mx, (self.y + my) / 2, win, nothing)
        ):
            return False
        return True

    def update_moves(self, win):
        from checkCollision import check_black, check_white

        self.moves = []
        self.check = []

        var = check_white if self.isWhite else check_black
        var2 = check_white if not self.isWhite else check_black

        if not isCollision(self.x, self.y - 75, win, var):
            self.moves.append((self.x, self.y - 75))
            if self.y == 450 and not isCollision(self.x, self.y - 150, win, var):
                self.moves.append((self.x, self.y - 150))
        if isCollision(self.x + 75, self.y - 75, win, var2):
            self.check.append((self.x + 75, self.y - 75))
            self.moves.append((self.x + 75, self.y - 75))
        if isCollision(self.x - 75, self.y - 75, win, var2):
            self.moves.append((self.x - 75, self.y - 75))
            self.check.append((self.x - 75, self.y - 75))


class BlackPawn(Piece):
    def legal_move(self, mx, my, win):
        from checkCollision import check_black, check_white

        if check_black(mx, my, win, nothing) or check_white(mx, my, win, nothing):
            if my - self.y != 75 or abs(self.x - mx) != 75:
                return False
            else:
                return True
        if self.x != mx:
            return False
        elif my - self.y > 150 or self.y >= my:
            return False
        elif (my - self.y > 75 and self.y != 75) or (
            check_black(mx, self.y + 75, win, nothing)
            or check_white(mx, self.y + 75, win, nothing)
        ):
            return False
        return True

    def update_moves(self, win):
        from checkCollision import check_black, check_white

        self.moves = []
        self.check = []

        var = check_white if self.isWhite else check_black
        var2 = check_white if not self.isWhite else check_black

        if not isCollision(self.x, self.y + 75, win, var):
            self.moves.append((self.x, self.y + 75))
            if self.y == 75 and not isCollision(self.x, self.y + 150, win, var):
                self.moves.append((self.x, self.y + 150))
        if isCollision(self.x + 75, self.y + 75, win, var2):
            self.moves.append((self.x + 75, self.y + 75))
            self.check.append((self.x + 75, self.y + 75))
        if isCollision(self.x - 75, self.y + 75, win, var2):
            self.moves.append((self.x - 75, self.y + 75))
            self.check.append((self.x - 75, self.y + 75))


def nothing(piece, win):
    pass


def sign(n):
    if n >= 0:
        return 75
    else:
        return -75


def isCollision(x, y, win, func):
    return func(x, y, win, nothing)
