import pygame
import game_config as gc
from button import Button

from pygame import display, event

pygame.init()

window = display.set_mode((gc.DISPLAY_WIDTH, gc.DISPLAY_HEIGHT))
display.set_caption("Terrible Games")
pygame.font.init()

title_font = pygame.font.SysFont(('Comic Sans MS'), 60)
button_font = pygame.font.SysFont(('Comic Sans MS'), 30)
tiles_button = Button("Tiles", button_font)
running = True

while running:
    for e in event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

    window.fill((255, 255, 255))

    title_text = title_font.render("Terrible Games", True, (0,0,0))
    title_height = title_text.get_height()
    title_width = title_text.get_width()
    window.blit(title_text, ((gc.DISPLAY_WIDTH-title_width)//2,
                             (gc.DISPLAY_HEIGHT-title_height)//3))

    tiles_button = Button("Tiles", button_font)
    tiles_button.renderButton(window)

    display.flip()