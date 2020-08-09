import pygame
import random
import game_config as gc
from game_base import gameWindow

from pygame import display, event, image

### Tile initialization ###

SQUARE_SIZE = gc.TILE_WIDTH * gc.TILE_WIDTH
NUM_SQUARE_PER_SIDE = 4

class tileGame:
    def __init__(self, tile_font: pygame.font, tileList: list, emptyIndex: int):
        self.font = tile_font
        self.tileList = tileList
        self.emptyIndex = emptyIndex
        self.tileClicked = False
        self.validMove = False
        self.moves = 0


class Tile:
    def __init__(self, number, index, tile_font):
        self.index = index
        self.number = number
        if number != "0":
            self.surf = tile_font.render(self.number, True, (0, 0, 0))
        if number == "0":
            self.surf = tile_font.render(" ", True, (0, 0, 0))
        self.xpos = 0
        self.ypos = 0
        self.bg_rect = None

    def set_pos(self, x, y):
        self.xpos = x
        self.ypos = y
        self.bg_rect = pygame.Rect(self.xpos, self.ypos,
                                   gc.TILE_WIDTH,
                                   gc.TILE_WIDTH)

    def renderTile(self, window, tile_font):
        # renders a tile if set_pos has been called
        assert self.bg_rect is not None
        pygame.draw.rect(window, (0, 0, 0), self.bg_rect, 3)
        if self.number != "0":
            self.surf = tile_font.render(self.number, True, (0, 0, 0))
        if self.number == "0":
            self.surf = tile_font.render(" ", True, (0, 0, 0))
        window.blit(self.surf, (self.xpos + gc.TILE_WIDTH // 3, self.ypos + gc.TILE_WIDTH // 3.5))

def find_index(x, y):
    row = (y - gc.TILE_TOP_OFFSET) // gc.TILE_WIDTH
    col = (x - gc.TILE_MARGIN_WIDTH) // gc.TILE_WIDTH
    index = row * NUM_SQUARE_PER_SIDE + col
    return index


def find_tile_xpos_from_index(index):
    col = index % gc.NUM_SQUARE_PER_SIDE
    xpos = int(gc.TILE_MARGIN_WIDTH + col * gc.TILE_WIDTH)
    return xpos


def find_tile_ypos_from_index(index):
    row = index // gc.NUM_SQUARE_PER_SIDE
    ypos = int(gc.TILE_TOP_OFFSET + row * gc.TILE_WIDTH)
    return ypos


def moveTiles(main_window, game_state):
    temp = game_state.tileList[game_state.emptyIndex].number
    game_state.tileList[game_state.emptyIndex].number = game_state.tileList[game_state.currIndex].number
    game_state.tileList[game_state.currIndex].number = temp
    game_state.emptyIndex = game_state.currIndex
    for tile in game_state.tileList:
        tile.renderTile(main_window.window, game_state.font)

def disp_tiles(main_window: gameWindow, game_state: tileGame):

    moves_text = game_state.font.render("Moves: " + str(game_state.moves), True, (0, 0, 0))
    main_window.window.blit(moves_text, (200, 28))

    for tile in game_state.tileList:
        tile.renderTile(main_window.window, game_state.font)

    for e in event.get():
        if e.type == pygame.QUIT:
            main_window.running = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_BACKSPACE:
            main_window.screen = "Title"
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # When the player clicks the tile they want to move
            if not game_state.tileClicked:
                game_state.currIndex = find_index(mouse_x, mouse_y)
                game_state.tileClicked = True
                game_state.validMove = False

            # check if the next tile clicked is empty
            else:
                checkEmpty = find_index(mouse_x, mouse_y)
                if checkEmpty == game_state.emptyIndex:
                    game_state.validMove = True
                    game_state.moves += 1
                game_state.tileClicked = False

            if game_state.validMove:
                moveTiles(main_window, game_state)
                game_state.validMove = False

            print(game_state.currIndex,
                  game_state.tileList[game_state.currIndex].number,
                  game_state.tileList[game_state.currIndex].xpos)

def init_tiles(tile_font: pygame.font):

    available_tiles = [x for x in range(0, 16)]
    # tile with number 0 will display as blank
    # initialize tile placement
    initTileList = []
    # indices in tileList will the the same as indicies of the game
    # The value at each index is the displayed value
    for i in range(16):
        randInd = random.randrange(0, len(available_tiles))
        randNumber = available_tiles.pop(randInd)
        if randNumber == 0:
            emptyIndex = i
        initTileList.append(randNumber)
    # print(initTileList)
    tileList = []
    for index in range(16):
        tile = Tile(str(initTileList[index]), index, tile_font)
        xpos = find_tile_xpos_from_index(index)
        ypos = find_tile_ypos_from_index(index)
        tile.set_pos(xpos, ypos)
        tileList.append(tile)

    game = tileGame(tile_font, tileList, emptyIndex)
    return game
