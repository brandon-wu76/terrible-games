import os
import random
import game_config as gc
import pygame


class Tile:
    def __init__(self, number, index, tile_font):
        self.index = index
        self.number = number
        print(number)
        self.surf = tile_font.render(self.number, True, (0,0,0))
        self.xpos = 0
        self.ypos = 0
        self.bg_rect = None

    def set_pos(self, x, y):
        self.xpos = x
        self.ypos = y
        self.bg_rect = pygame.Rect(self.xpos, self.ypos,
                                                gc.TILE_WIDTH, 
                                                gc.TILE_WIDTH)
    
    def renderTile(self, window):
        #renders a tile if set_pos has been called
        assert self.bg_rect is not None
        pygame.draw.rect(window, (0,0,0), self.bg_rect, 3)
        window.blit(self.surf, (self.xpos, self.ypos))