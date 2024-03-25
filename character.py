class Character:
    def __init__(self, pos_x, pos_y, health, main_hand, off_hand):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health
        self.main_hand = main_hand
        self.off_hand = off_hand

    def set_pos(self, x ,y):
        self.pos_x = x
        self.pos_y = y

    def change_pos(self, x, y):
        self.pos_x += x
        self.pos_y += y
    
    def get_pos(self):
        return(self.pos_x, self.pos_y)