class Setting():
    def __init__(self):
        #screen setting
        self.screen_width=1200
        self.screen_heigth=800
        self.screen_bg_color=(230,230,230)
        #ship setting
        self.ship_speed=1
        self.ship_limit=3

        #bullet setting
        self.bullet_width=3000
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_speed=8

        #alien setting
        self.alien_speed_X=1
        self.alien_move_director=1
        self.alien_speed_Y=10
        self.point=10
        #level setting
        self.game_speed_up=1.1
        self.init_game_setting()

    def init_game_setting(self):
        self.alien_speed_Y=10
        self.bullet_speed=8
        self.ship_speed=1
        self.point=10

    def increase_speed(self):
        self.alien_speed_Y*=self.game_speed_up
        self.bullet_speed*=self.game_speed_up
        self.ship_speed*=self.game_speed_up
        self.point=int(self.point*self.game_speed_up)