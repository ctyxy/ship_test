import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


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

def check_key(setting,screen,stats,ship,bullets,play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_key_down(setting,screen,ship,bullets,event)
        elif event.type==pygame.KEYUP:
            check_key_up(ship,event)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(setting,stats,play_button,mouse_x,mouse_y)

def check_play_button(setting,stats,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active=True
        stats.reset_stats()
        setting.init_game_setting()
        



def update_screen(screen,setting,stats,ship,bullets,aliens,play_button,scoreB,high_score):

    screen.fill(setting.screen_bg_color)
    ship.biltme()
    aliens.draw(screen)
    scoreB.show()
    high_score.high_show()
    for bullet in bullets:
        bullet.darw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(screen,setting,ship_height,bullets,aliens,stats,scoreB):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullets_aliens_coll(screen,setting,ship_height,bullets,aliens,stats,scoreB)

def check_bullets_aliens_coll(screen,setting,ship_height,bullets,aliens,stats,scoreB):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=setting.point*len(aliens)
            scoreB.prep_score()
    if len(aliens)==0:
        bullets.empty()
        setting.increase_speed()
        alien_fleet_creat(screen,setting,ship_height,aliens)

def update_aliens(screen, setting, stats, sb,ship, bullets, aliens):
    check_fleet_edge(setting,aliens)
    aliens.update()
    check_ship_aliens(screen, setting, stats, sb,ship, bullets, aliens)
    check_aliens_screen_bottom(screen, setting, stats, sb,ship, bullets, aliens)

def check_ship_aliens(screen, setting, stats, sb,ship, bullets, aliens):
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(screen, setting, stats, sb,ship, bullets, aliens)

def check_aliens_screen_bottom(screen, setting, stats, sb,ship, bullets, aliens):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(screen, setting, stats, sb,ship, bullets, aliens)
            break

def ship_hit(screen,setting,stats,sb,ship,bullets,aliens):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        sb.prep_ship()
        alien_fleet_creat(screen, setting, ship, aliens)

        sleep(0.5)

    else:
        if stats.score>stats.highest_score:
            stats.highest_score=stats.score
        stats.game_active=False

def check_fleet_edge(setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_aliens_direction(setting,aliens)
            break

def change_aliens_direction(setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=setting.alien_speed_Y
    setting.alien_speed_X*=-1

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
    alien.rect.y=alien.rect.height+2*alien.rect.height*number_aliens_y+10
    aliens.add(alien)

def alien_fleet_creat(screen,setting,ship,aliens):
    alien=Alien(screen,setting)
    number_aliens_x=get_number_aliens_x(setting,alien.rect.width)
    alien__num_y=get_num_aliens_y(setting,ship.rect.height,alien.rect.height)
    for num_y in range(alien__num_y):
        for alien_n in range(number_aliens_x):
            alien_creat(screen,setting,aliens,alien_n,num_y)