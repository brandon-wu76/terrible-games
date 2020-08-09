import game_base
import pygame
import game_config as gc
import time
from pygame import event, transform, display
from random import randint

class Card:
    def __init__(self, image):
        self.img = transform.scale(image.convert_alpha(), (56, 76))
        self.xpos = 0
        self.ypos = 0
        self.angle = 0
        self.surf = None
        self.rect = None

    def set_pos_and_rotate(self, x, y, angle):
        '''
        Finds the center of the original image, rotates the image
        then sets the center of the rotated rectangle to the center
        of the old rectangle
        '''
        center = self.img.get_rect().center
        rotated = pygame.transform.rotozoom(self.img, angle, 1)
        new_rect = rotated.get_rect(center = center)
        self.surf = rotated
        self.rect = new_rect.move(x-self.img.get_rect().centerx,y-self.img.get_rect().centery)


    def renderCard(self, window):
        assert self.surf is not None
        assert self.rect is not None

        window.blit(self.surf, self.rect.topleft)

def disp_pickup(main_window: game_base.gameWindow, cardlist: list):

    for c in cardlist:
        c.renderCard(main_window.window)

    for e in event.get():
        if e.type == pygame.QUIT:
            main_window.running = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_BACKSPACE:
            main_window.screen = "Title"
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for c in reversed(cardlist):
                if c.rect.collidepoint(mouse_x, mouse_y):
                    cardlist.remove(c)
                    break
    if not cardlist:
        main_window.window.fill((209, 169, 132))
        finish_font = pygame.font.SysFont(('Comic Sans MS'), 30)
        finish_line1 = finish_font.render("You did it!", True, (0, 0, 0))
        finish_line2 = finish_font.render("Now where did I put those keys... oops", True, (0, 0, 0))
        x1 = gc.DISPLAY_WIDTH//2-finish_line1.get_rect().centerx
        x2 = gc.DISPLAY_WIDTH//2-finish_line2.get_rect().centerx
        y = gc.DISPLAY_HEIGHT//2-finish_line1.get_rect().centery
        main_window.window.blit(finish_line1, (x1, y - finish_line1.get_rect().centery))
        main_window.window.blit(finish_line2, (x2, y + finish_line2.get_rect().centery))
        display.flip()
        time.sleep(3)
        cardlist.extend(init_pickup())

def init_pickup():
    cardlist = []
    faceCardList = [x for x in range(26)]
    for i in range(52):
        if randint(0,1):
            c = Card(pygame.image.load("./resources/cardback.png"))
        elif faceCardList:
            i = randint(0,len(faceCardList)-1)
            c = Card(pygame.image.load("./resources/{}.png".format(faceCardList[i])))
        else:
            c = Card(pygame.image.load("./resources/cardback.png"))

        x = randint(int(gc.DISPLAY_WIDTH*1/30), int(gc.DISPLAY_WIDTH*29/30))
        y = randint(int(gc.DISPLAY_HEIGHT*1/30), int(gc.DISPLAY_HEIGHT*29/30))
        theta = randint(0,359)
        c.set_pos_and_rotate(x, y, theta)
        cardlist.append(c)
    return cardlist