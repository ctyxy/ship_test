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

def update_aliens(alien):
    alien.update()


def get_number_aliens_x(setting,alien_width):
    avail_space_x=setting.screen_width - 2 * alien_width
    aliens_num_x=int(avail_space_x / (2 * alien_width))
    return aliens_num_x

def get_num_aliens_y(setting,ship_height,aliens_height):
    available_space_y=(setting.screen_heigth-(3*aliens_height)-ship_height)
    number_aliens_y=int(available_space_y/(2*aliens_height))
    return number_aliens_y


def alien_creat(screen,setting,aliens,aliens_num,number_aliens_y):
    alien=Alien(screen,setting)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*aliens_num
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*number_aliens_y
    aliens.add(alien)

def alien_fleet_creat(screen,setting,ship_height,aliens):
    alien=Alien(screen,setting)
    number_aliens_x=get_number_aliens_x(setting,alien.rect.width)
    alien__num_y=get_num_aliens_y(setting, ship_height, alien.rect.height)
    for num_y in range(alien__num_y):
        for alien_n in range(number_aliens_x):
            alien_creat(screen,setting,aliens,alien_n,num_y)