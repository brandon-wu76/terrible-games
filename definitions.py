import os
import random
import game_config as gc


class Tile:
    def __init__(self, number, index):
        self.index = index
        self.row = index // gc.NUM_SQUARE_PER_SIDE
        self.col = index %gc.NUM_SQUARE_PER_SIDE
        self.number = number