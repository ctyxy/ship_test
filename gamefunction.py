import sys
from time import ctime

import pygame


def time_update():
    return ctime()


def check_key(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_RIGHT:
                ship.move_right=True
            elif event.key == pygame.K_LEFT:
                ship.move_left=True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right=False
            elif event.key == pygame.K_LEFT:
                ship.move_left=False


def update_screen(screen,setting,ship):
    screen.fill(setting.screen_bg_color)
    ship.biltme()
    pygame.display.flip()
