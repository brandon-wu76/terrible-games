import pygame
import random

from pygame import display, event, image
from time import sleep

SQUARE_SIZE = 128
NUM_SQUARE_PER_SIDE = 4
def find_index(x,y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    index = row * NUM_SQUARE_PER_SIDE + col
    return index



pygame.init()

display.set_caption('My Game')
screen = display.set_mode((512,512))

available_tiles = [x for x in range(0,16)]
#tile with number 0 will display as blank
#initialize tile placement
tileList = [] 
#indices in tileList will the the same as indicies of the game
#The value at each index is the displayed value
for i in range(16):
    randInd = random.randrange(0, len(available_tiles))
    randNumber = available_tiles.pop(randInd)
    if randNumber == 0:
        emptyIndex = i
    tileList.append(randNumber)

print(tileList)

running =  True
tileClicked = False
while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if e.type == pygame.MOUSEBUTTONDOWN and tileClicked:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            nextIndex = find_index(mouse_x, mouse_y)
            if (nextIndex == emptyIndex):
                #value at index switches with empty index
                validMove = True

            tileClicked = True
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            tileClicked = True

    screen.fill((255,255,255))

    total_skipped = 0

    