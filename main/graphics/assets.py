# import pygame
from graphics.loader import *

class Assets():
    def __init__(self):
        self.player = Loader().imageLoader('resources\ships\ship.png').convert()
        

