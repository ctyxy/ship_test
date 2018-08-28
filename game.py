import time
import pygame
import gamefunction
from setting import Setting
from ship import Ship
from pygame.sprite import Group
from gamestats import Gamestats
from button import Button,ScoreBoard,HighScore

def run_game():
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_heigth))
    screen.fill(setting.screen_bg_color)
    pygame.display.set_caption("Aliens fight with ship(%s)" % time.ctime())

    play_button=Button(screen,setting,"START")
    ship = Ship(screen,setting)
    bullets=Group()
    aliens=Group()
    stats=Gamestats(setting)
    scoreB=ScoreBoard(screen,setting,stats)
    high_score = HighScore(screen, setting, stats)
    gamefunction.alien_fleet_creat(screen,setting,ship,aliens)
    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gamefunction.check_key(setting, screen,stats, ship, bullets,play_button)
        pygame.display.set_caption("Aliens fight with ship(%s)" % time.ctime())
        if stats.game_active:

            ship.update()
            gamefunction.update_bullets(screen,setting,ship,bullets,aliens,stats,scoreB)
            gamefunction.update_aliens(screen, setting, stats,scoreB,ship, bullets, aliens)

        gamefunction.update_screen(screen,setting,stats,ship,bullets,aliens,play_button,scoreB,high_score)

run_game()
