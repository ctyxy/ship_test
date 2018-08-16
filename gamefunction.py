import sys
from time import ctime
import pygame
from bullet import Bullet
from alien import Alien
def time_update():
    return ctime()


def check_key_down(setting,screen,ship,bullets,event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            ship.move_right=True
        elif event.key == pygame.K_LEFT:
            ship.move_left=True
        elif event.key==pygame.K_SPACE:
            new_bullet=Bullet(setting,screen,ship)
            bullets.add(new_bullet)

def check_key_up(ship,event):
        if event.key == pygame.K_RIGHT:
            ship.move_right=False
        elif event.key == pygame.K_LEFT:
            ship.move_left=False

def check_key(setting,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_key_down(setting,screen,ship,bullets,event)
        elif event.type==pygame.KEYUP:
            check_key_up(ship,event)


def update_screen(screen,setting,ship,bullets,aliens):
    screen.fill(setting.screen_bg_color)
    ship.biltme()
    aliens.draw(screen)
    for bullet in bullets:
        bullet.darw_bullet()
    pygame.display.flip()

def update_bullets(bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

def alien_fleet(screen,setting,aliens):
    alien=Alien(screen,setting)
    alien_width=alien.rect.width
    avail_space_x=setting.screen_width-3*alien_width
    alien_num_x=int(setting.screen_width/alien_width)
    for alien_n in range(alien_num_x):
        alien=Alien(screen,setting)
        alien.x=alien_width+2*alien_width*alien_n
        alien.rect.x=alien.x
        aliens.add(alien)
