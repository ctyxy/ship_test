class Gamestats():
    def __init__(self,setting):
        self.setting=setting
        self.reset_stats()
        self.game_active=False
        self.score=0
        self.highest_score=0
        self.ships_left=3
    
    def reset_stats(self):
        self.ships_left=self.setting.ship_limit
        self.score=0

