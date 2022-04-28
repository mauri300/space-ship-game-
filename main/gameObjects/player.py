
import pygame
from graphics.assets import *
from graphics.loader import *
# from gameObjects.gameObject import *
from gameObjects.movingObject import *
import math


class Player(pygame.sprite.Sprite, MovingObject): 
    def __init__(self, posX, posY):
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)
        #GameObject.__init__(self)
        MovingObject.__init__(self)
        self.__assets = Assets()
        self.__BLACK = (0, 0, 0)
        # self.image = self.__assets.player




        self.original_image = self.__assets.player
        self.image = self.original_image




        self.image.set_colorkey((255,0,255))
        self.image = pygame.transform.scale(self.image, (100, 75))
        self.rect = self.image.get_rect()
        self.__heading = Vector2D(0, 0)
       
        self.__w, self.__h = self.image.get_size()
        self.rect.x = posX
        self.rect.y = posY
        
    
    def update(self):
        
        self.__keystate = pygame.key.get_pressed()
        if(self.__keystate[pygame.K_RIGHT]):
            self._angle -= 10 % 360
            print("der")
        if(self.__keystate[pygame.K_LEFT]):
            self._angle += 10 % 360
            print("izq")
        # self.__heading = self.__heading.setDirection(self._angle - math.pi / 2)
        self.__rotate()
        
    # rotate
    def __rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self._angle)
        # self._angle += 1 % 360
        x, y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
      
        
