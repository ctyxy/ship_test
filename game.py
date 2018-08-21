import time
import pygame
import gamefunction
from setting import Setting
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_heigth))
    screen.fill(setting.screen_bg_color)
    pygame.display.set_caption("Aliens fight with ship(%s)" % time.ctime())

    ship = Ship(screen,setting)
    bullets=Group()
    aliens=Group()

    gamefunction.alien_fleet_creat(screen,setting,ship.rect.height,aliens)
    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gamefunction.check_key(setting,screen,ship,bullets)
        ship.update()
        gamefunction.update_bullets(screen,setting,ship.rect.height,bullets,aliens)
        gamefunction.update_aliens(setting,ship,aliens)
        gamefunction.update_screen(screen,setting,ship,bullets,aliens)

run_game()
