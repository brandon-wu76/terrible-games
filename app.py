import pygame
import game_config as gc

from pygame import display, event

pygame.init()

window = display.set_mode((gc.DISPLAY_WIDTH, gc.DISPLAY_HEIGHT))
display.set_caption("Terrible Games")
pygame.font.init()

titlefont = pygame.font.SysFont(('Comic Sans MS'), 30)

running = True

while running:
    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
    titletext = titlefont.render("Terrible Games", False, (0,0,0))
    window.fill((255, 255, 255))
    window.blit(titletext, (0, 0))
    display.flip()
