import pygame
import game_config as gc
from pygame import display, event


class gameWindow:
    def __init__(self, window: pygame.Surface, running: bool, curr_screen: str):
        self.window = window
        self.running = running
        self.screen = curr_screen

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

def initialize_game():
    pygame.init()

    window = display.set_mode((gc.DISPLAY_WIDTH, gc.DISPLAY_HEIGHT))
    display.set_caption("Terrible Games")
    pygame.font.init()

    main_window = gameWindow(window=window, running=True, curr_screen="Title")
    return main_window

def init_title_buttons(button_names, button_coords):
    '''
    Initializes buttons on title screen
    Params: button_names contains a list of button names
    button_coords contains coordinate tuples for top left corner
    '''

    button_font = pygame.font.SysFont(('Comic Sans MS'), 30)

    assert len(button_names) == len(button_coords)

    buttons_list = []

    for name, coords in zip(button_names, button_coords):
        button = Button(name, button_font)
        x_pos = int(gc.DISPLAY_WIDTH * coords[0])
        y_pos = int(gc.DISPLAY_HEIGHT * coords[1] - button.surf.get_height() / 2)
        button.set_pos(x_pos, y_pos)
        buttons_list.append(button)

    return buttons_list

def disp_title(main_window: gameWindow, button_list: list, title_text: pygame.Surface):
    # Renders title text and buttons
    title_height = title_text.get_height()
    title_width = title_text.get_width()

    x_pos = (gc.DISPLAY_WIDTH - title_width) // 2
    y_pos = (gc.DISPLAY_HEIGHT - title_height) // 3
    main_window.window.blit(title_text, (x_pos, y_pos))
    for button in button_list:
        button.renderButton(main_window.window)

    for e in event.get():
        if e.type == pygame.QUIT:
            main_window.running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_BACKSPACE:
                main_window.screen = "Title"

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if main_window.screen == "Title":
                for button in button_list:
                    if button.bg_rect.collidepoint(mouse_x, mouse_y):
                        main_window.screen = button.name