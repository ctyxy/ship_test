import pygame.ftfont
from ship import Ship
from pygame.sprite import  Group
class Button():

    def __init__(self,screen,setting,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.setting=setting

        self.width,self.height=200,50
        self.button_color=(0,230,0)
        self.text_color=(250,250,250)
        self.font=pygame.ftfont.SysFont(None,48)

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

class ScoreBoard():
    def __init__(self,screen,setting,stats):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.setting=setting
        self.stats=stats

        self.text_color=(20,30,30)
        self.font=pygame.ftfont.SysFont(None,48)

        self.prep_score()
        self.prep_ship()

    def prep_score(self):
        score_str=str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.setting.screen_bg_color)

        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20
    
    def prep_ship(self):
        self.ships=Group()
        for ship_number in range(self.stats.ships_left):
            ship=Ship(self.screen,self.setting)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)
            
    
    def show(self):
        self.prep_score()
        self.prep_ship()
        self.screen.blit(self.score_image,self.score_rect)
        self.ships.draw(self.screen)
    
    
    
class HighScore():
    def __init__(self,screen,setting,stats):
        self.screen=screen
        self.setting=setting
        self.screen_rect=screen.get_rect()
        self.stats=stats

        self.text_color = (20, 30, 30)
        self.font = pygame.ftfont.SysFont(None, 48)

        self.prep_h_score()

    def prep_h_score(self):
        score_str = str(self.stats.highest_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.screen_bg_color)
    
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center= self.screen_rect.center
        self.score_rect.top = 20

    def high_show(self):
        self.prep_h_score()
        self.screen.blit(self.score_image, self.score_rect)