import time

import pygame

import gamefunction
from setting import Setting
from ship import Ship


def run_game():
    pygame.init()
    setting=Setting()
    screen=pygame.display.set_mode((setting.screen_heigth,setting.screen_width))
    screen.fill(setting.screen_bg_color)
    pygame.display.set_caption("Aliens fihgt with ship(%s)" % time.ctime())

    ship=Ship(screen)

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gamefunction.check_key(ship)
        ship.update()
        gamefunction.update_screen(screen,setting,ship)

run_game()
