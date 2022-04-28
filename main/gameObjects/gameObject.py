# from pygame import Vector2

from maths.vector2d import *


class GameObject():
    def __init__(self):
        
        self._pos = Vector2D(0,0)
        
        
    def getPosition(self):
        return self._pos

    def setPosition(self, posX, posY): 
        self._pos.setX(posX)
        self._pos.setX(posY)
