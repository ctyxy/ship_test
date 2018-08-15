import time
import pygame
import gamefunction
from setting import Setting
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_heigth,setting.screen_width))
    screen.fill(setting.screen_bg_color)
    pygame.display.set_caption("Aliens fight with ship(%s)" % time.ctime())

    ship = Ship(screen,setting)
    bullets=Group()

    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gamefunction.check_key(setting,screen,ship,bullets)
        ship.update()
        gamefunction.update_bullets(bullets)
        gamefunction.update_screen(screen,setting,ship,bullets)

run_game()
