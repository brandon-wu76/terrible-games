import pygame
import game_config as gc
from pygame import display, event


class gameWindow:
    def __init__(self, window: pygame.Surface, running: bool, curr_screen: str, img: pygame.Surface):
        self.window = window
        self.running = running
        self.screen = curr_screen
        self.background = img

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

    load_font = pygame.font.SysFont(('Comic Sans MS'), 45)
    load_text = load_font.render("Loading...", True, (0, 0, 0))
    x = (gc.DISPLAY_WIDTH*1.03-load_text.get_rect().right)//2
    y = (gc.DISPLAY_HEIGHT-load_text.get_rect().bottom)//2
    window.fill((210,127,73))
    window.blit(load_text, (x,y))
    display.flip()

    image = pygame.image.load("./resources/wood_texture.jpg").convert()
    image = pygame.transform.scale(image, (gc.DISPLAY_WIDTH,gc.DISPLAY_HEIGHT))

    main_window = gameWindow(window=window, running=True, curr_screen="Title", img=image)
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

    ## Help button initialization ##
    helpbutton = Button("?", button_font)
    x_pos = int(gc.DISPLAY_WIDTH * 15 / 16)
    y_pos = int(gc.DISPLAY_HEIGHT * 1 / 32)
    helpbutton.set_pos(x_pos, y_pos)
    helpbutton.bg_rect = pygame.Rect(helpbutton.xpos - helpbutton.surf.get_height()//2,
                                     helpbutton.ypos,
                                     helpbutton.surf.get_height(),
                                     helpbutton.surf.get_height()
                                     )
    buttons_list.append(helpbutton)

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

def disp_help(main_window: gameWindow, help_text: pygame.Surface):

    x_pos = (gc.DISPLAY_WIDTH*1.02 - help_text.get_rect().right) // 2
    y_pos = (gc.DISPLAY_HEIGHT - help_text.get_rect().bottom) // 4
    main_window.window.blit(help_text, (x_pos, y_pos))

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