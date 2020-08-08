import os

class Button:
    def __init__(self, button_name, button_font):
        self.name = button_name
        self.surf = button_font.render(self.name, True, (0,0,0))
        self.xpos = 0
        self.ypos = 0

    def set_x_pos(self, x):
        self.xpos = x

    def set_y_pos(self, y):
        self.ypos = y

    def renderButton(self, window):
        window.blit(self.surf,(self.xpos,self.ypos))