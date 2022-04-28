import pygame

class KeyBoard:
    def __init__(self):
        self.UP = False
        self.LEFT = False
        self.RIGHT = False
        self.__keystate = pygame.key.get_pressed()

    def update(self):
        self.UP = self.__keystate[pygame.K_UP]
        self.LEFT = self.__keystate[pygame.K_LEFT]
        self.RIGHT = self.__keystate[pygame.K_RIGHT]
        
        