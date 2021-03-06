import pygame
import game_base
import tiles
import pickup
import game_config as gc
from pygame import display

###  Game Initialization  ###

main_window = game_base.initialize_game()

title_font = pygame.font.SysFont(('Comic Sans MS'), 60)
tile_font = pygame.font.SysFont(('Comic Sans MS'), 38)

title_text = title_font.render("Terrible Games", True, (0, 0, 0))
help_font = pygame.font.SysFont(('Comic Sans MS'), 50)
help_text = title_font.render("How to play", True, (0,0,0))

game_list = ["Tiles", "52 Pickup", "Snake"]
button_coordinates = [(1/5,3/4), (1/2,3/4), (4/5,3/4)]
button_list = game_base.init_title_buttons(game_list, button_coordinates)

tile_game_state = tiles.init_tiles(tile_font)

card_list = pickup.init_pickup()

###  Game Loop  ###

while main_window.running:

    main_window.window.blit(main_window.background, (0,0))

    if main_window.screen == "Title":
        game_base.disp_title(main_window, button_list, title_text)
    elif main_window.screen == "?":
        game_base.disp_help(main_window, help_text)
    elif main_window.screen == "Tiles":
        tiles.disp_tiles(main_window, tile_game_state)
    elif main_window.screen == "52 Pickup":
        pickup.disp_pickup(main_window, card_list)
    elif main_window.screen == "Snake":
        pass

    display.flip()