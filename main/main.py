import pygame

from gameObjects.player import *

class Window:
  
    def __init__(self):
        
        self.__WIDTH = 800
        self.__HEIGHT = 600
        self.__BLACK = (0, 0, 0)
        pygame.init()
        pygame.mixer.init()
        self.__screen = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        pygame.display.set_caption("Space Ship Game")
        self.__clock = pygame.time.Clock()


    def run(self):
        self.__all_sprites = pygame.sprite.Group()
        # player set position
        self.__player = Player(self.__screen.get_width()/2, self.__screen.get_height()/2)
        # self.__player.setPosition(self.__screen.get_width()/2, self.__screen.get_height()/2) 
        self.__all_sprites.add(self.__player)
   

        self.__running = True
        while self.__running:
            
            self.__clock.tick(60) # 60FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
            
            # Update
            self.__all_sprites.update()
            
            # Draw / Render
            self.__screen.fill(self.__BLACK)
            self.__all_sprites.draw(self.__screen)
            
            # Flip display
            pygame.display.flip()

        pygame.quit()

myWindow = Window()
myWindow.run()
