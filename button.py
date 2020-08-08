import os
import pygame
import game_config as gc

class Button:
    def __init__(self, button_name, button_font):
        self.name = button_name
        self.surf = button_font.render(self.name, True, (0,0,0))
        self.xpos = 0
        self.ypos = 0
        self.bg_rect = None


    def set_pos(self, x, y):
        self.xpos = x
        self.ypos = y
        self.bg_rect = pygame.Rect(self.xpos-gc.BUTTON_WIDTH//2,
                              self.ypos,
                              gc.BUTTON_WIDTH,
                              self.surf.get_height()
                              )


    def renderButton(self, window):
        # Renders a button if set_pos has been called
        assert self.bg_rect is not None
        pygame.draw.rect(window, (0, 0, 0), self.bg_rect, 5)
        window.blit(self.surf,(self.xpos-self.surf.get_width()//2,self.ypos))