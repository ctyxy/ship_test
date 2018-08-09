import time

import pygame

import gamefunction


def run_game():
    pygame.init()
    screen=pygame.display.set_mode((800,600))

    pygame.display.set_caption("Aliens fihgt with ship(%s)" % time.ctime())
    bg_color=(240,240,212)

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gamefunction.check_key()
        screen.fill(bg_color)

        pygame.display.flip()


run_game()
