# pylint: disable-all
import time
from math import floor
from settings import *
from checkCollision import *
from check import *


def validClick(event, win):
    x, y = event
    if Player1.isTurn:
        check_white(x, y, win, move)
    else:
        check_black(x, y, win, move)


def validTake(event, win):
    x, y = event
    if Player1.isTurn:
        if not (check_black(x, y, win, take)):
            if check_white(x, y, win, error):
                return False
    else:
        if not (check_white(x, y, win, take)):
            if check_black(x, y, win, error):
                return False
    return True


def error(piece, win):
    s = pygame.Surface((75, 75))
    s.set_alpha(128)
    s.fill((255, 0, 0))
    pygame.draw.rect(win, (232, 235, 239), [piece.x, piece.y, 75, 75])
    win.blit(piece.img, (piece.x, piece.y))
    win.blit(s, (piece.x, piece.y))
    pygame.display.update()
    time.sleep(0.5)


def take(piece, win):
    piece.take_piece()


def move(piece, win):
    run = True
    s = pygame.Surface((75, 75))
    s.set_alpha(90)
    s.fill((255, 255, 0))
    for item in piece.moves:
        win.blit(s, item)
    pygame.display.update()
    while run:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                pygame.quit()
            elif event2.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx = floor(mx / 75) * 75
                my = floor(my / 75) * 75
                if (
                    piece.legal_move(mx, my, win)
                    and noCheck(piece, mx, my, win)
                    and validTake(event2.pos, win)
                ):
                    piece.set_rect(mx, my)
                    Player1.makeMove()
                run = False

        if not Player1.isTurn and not Player2.isHuman:
            mx,my = Player2.finishMove()
            if (
                piece.legal_move(mx, my, win)
                and noCheck(piece, mx, my, win)
                and validTake((mx,my), win)
            ):
                piece.set_rect(mx, my)
                Player1.makeMove()
            run = False



# def colorSquare(x, y, win):
#     color = (125, 135, 150)

#     if ((x / 75) % 2 == 0) and ((y / 75) % 2 == 1):
#         color = (125, 135, 150)
#     elif (x / 75) % 2 == 0:
#         color = (232, 235, 239)
#     elif ((x / 75) % 2 == 1) and ((y / 75) % 2 == 1):
#         color = (232, 235, 239)

#     pygame.draw.rect(win, color, [x, y, 75, 75])
