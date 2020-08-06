# pylint: disable-all
import pygame
import board
import firstSetup
from settings import *
import movePiece
import time
from win32api import GetSystemMetrics


def reset():
    win.fill(pygame.Color("black"))
    board.buildBoard(win, sys_height)
    firstSetup.firstSetup(win)
    pygame.display.update()


sys_height = 600  # int(GetSystemMetrics(0) / 2)
sys_width = 600  # int(GetSystemMetrics(1) * 2 / 3)

win = pygame.display.set_mode((sys_height, sys_width))

board.buildBoard(win, sys_height)
firstSetup.firstSetup(win)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            movePiece.validClick(event.pos, win)
    reset()
    if not Player1.isTurn and not Player2.isHuman:
        movePiece.validClick(Player2.makeMove(), win)
    reset()
pygame.quit()


