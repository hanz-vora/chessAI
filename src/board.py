# pylint: disable-all
import pygame

def buildBoard(win, sys_height):
    pygame.display.set_caption("Chess")
    size = sys_height / 8

    white = (232, 235, 239)
    black = (125, 135, 150)

    cnt = 0

    for i in range(0, 8):
        for j in range(0, 8):
            if cnt % 2 == 0:
                pygame.draw.rect(win, white, [size * j, size * i, size, size])
            else:
                pygame.draw.rect(win, black, [size * j, size * i, size, size])
            cnt += 1
        cnt -= 1


