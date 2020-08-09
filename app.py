import pygame
import random
import game_config as gc
from button import Button
from pygame import display, event
from definitions import Tile


def init_title_buttons(button_names, button_coords):
    '''
    Initializes buttons on title screen
    Params: button_names contains a list of button names
    button_coords contains coordinate tuples for top left corner
    '''

    assert len(button_names) == len(button_coords)

    buttons_list = []

    for name, coords in zip(button_names, button_coords):
        button = Button(name, button_font)
        x_pos = int(gc.DISPLAY_WIDTH * coords[0])
        y_pos = int(gc.DISPLAY_HEIGHT * coords[1] - button.surf.get_height() / 2)
        button.set_pos(x_pos, y_pos)
        buttons_list.append(button)

    return buttons_list

### Tile initialization ### 

SQUARE_SIZE = gc.TILE_WIDTH*gc.TILE_WIDTH
NUM_SQUARE_PER_SIDE = 4
def find_index(x,y):
    row = (y-gc.TILE_TOP_OFFSET) // gc.TILE_WIDTH
    col = (x-gc.TILE_MARGIN_WIDTH) // gc.TILE_WIDTH
    index = row * NUM_SQUARE_PER_SIDE + col
    return index

def find_tile_xpos_from_index(index):
    col = index %gc.NUM_SQUARE_PER_SIDE
    xpos = int(gc.TILE_MARGIN_WIDTH + col*gc.TILE_WIDTH)
    return xpos

def find_tile_ypos_from_index(index):
    row = index // gc.NUM_SQUARE_PER_SIDE
    ypos = int(gc.TILE_TOP_OFFSET + row*gc.TILE_WIDTH)
    return ypos

def init_tiles():
    available_tiles = [x for x in range(0,16)]
    #tile with number 0 will display as blank
    #initialize tile placement
    initTileList = [] 
    #indices in tileList will the the same as indicies of the game
    #The value at each index is the displayed value
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
    
    return tileList, emptyIndex
        
def moveTiles(emptyIndex, currIndex, tileList):
    temp = tileList[emptyIndex].number
    tileList[emptyIndex].number = tileList[currIndex].number
    tileList[currIndex].number = temp
    emptyIndex = currIndex
    for tile in tileList:
        tile.renderTile(window, tile_font)
    return tileList, emptyIndex

###  Game Rendering Functions  ###

def disp_title():
    # Renders title text and buttons
    x_pos = (gc.DISPLAY_WIDTH - title_width) // 2
    y_pos = (gc.DISPLAY_HEIGHT - title_height) // 3
    window.blit(title_text, (x_pos, y_pos))
    for button in button_list:
        button.renderButton(window)

def disp_tiles():
    # window.fill((209, 169, 132))
    test_text = title_font.render("Tiles", True, (0, 0, 0))
    window.blit(test_text, (0, 0))
    
    moves_text = tile_font.render("Moves: " + str(moves), True, (0, 0, 0))
    window.blit(moves_text, (200, 28))
    
    for tile in tileList:
        tile.renderTile(window, tile_font)

def disp_52pickup():
    return

def disp_thirdgame():
    return

###  Game Initialization  ###

pygame.init()

window = display.set_mode((gc.DISPLAY_WIDTH, gc.DISPLAY_HEIGHT))
display.set_caption("Terrible Games")
pygame.font.init()

title_font = pygame.font.SysFont(('Comic Sans MS'), 60)
button_font = pygame.font.SysFont(('Comic Sans MS'), 30)
tile_font = pygame.font.SysFont(('Comic Sans MS'), 38)

title_text = title_font.render("Terrible Games", True, (0, 0, 0))
title_height = title_text.get_height()
title_width = title_text.get_width()

game_list = ["Tiles", "52 Pickup", "Third Game"]
button_coordinates = [(1/5,3/4), (1/2,3/4), (4/5,3/4)]

button_list = init_title_buttons(game_list, button_coordinates)
tileList, emptyIndex = init_tiles()

running = True
moves = 0

disp_states = {"Title": disp_title,
               "Tiles": disp_tiles,
               "52 Pickup": disp_52pickup,
               "Third Game": disp_thirdgame
}

current_screen = "Title"
tileClicked = False
validMove = False

###  Game Loop  ###

while running:

    window.fill((209, 169, 132))

    assert current_screen in disp_states

    disp_states[current_screen]()

    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_BACKSPACE:
                current_screen = "Title"

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if current_screen == "Title":
                for button in button_list:
                    if button.bg_rect.collidepoint(mouse_x, mouse_y):
                        current_screen = button.name

            # for tiles display
            elif current_screen == "Tiles":
                 # check if the next tile clicked is empty 
                if tileClicked:
                    checkEmpty = find_index(mouse_x,mouse_y)
                    if checkEmpty == emptyIndex:
                        validMove = True
                        moves +=1
                    tileClicked = False
                
                # When the player clicks the tile they want to move
                else:
                    currIndex = find_index(mouse_x, mouse_y)
                    tileClicked = True
                    validMove = False

                if validMove:
                    tileList, emptyIndex = moveTiles(checkEmpty, currIndex, tileList)
                    validMove = False
                print(currIndex, tileList[currIndex].number, tileList[currIndex].xpos)

                        
                
    display.flip()