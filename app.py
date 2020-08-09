import pygame
import game_base
import tiles
from pygame import display

###  Game Initialization  ###

main_window = game_base.initialize_game()

title_font = pygame.font.SysFont(('Comic Sans MS'), 60)
tile_font = pygame.font.SysFont(('Comic Sans MS'), 38)

title_text = title_font.render("Terrible Games", True, (0, 0, 0))

game_list = ["Tiles", "52 Pickup", "Third Game"]
button_coordinates = [(1/5,3/4), (1/2,3/4), (4/5,3/4)]
button_list = game_base.init_title_buttons(game_list, button_coordinates)

tile_game_state = tiles.init_tiles(tile_font)

###  Game Loop  ###

while main_window.running:

    main_window.window.fill((209, 169, 132))

    if main_window.screen == "Title":
        game_base.disp_title(main_window, button_list, title_text)
    elif main_window.screen == "Tiles":
        tiles.disp_tiles(main_window, tile_game_state)
    elif main_window.screen == "52 Pickup":
        pass
    elif main_window.screen == "Third Game":
        pass

    display.flip()