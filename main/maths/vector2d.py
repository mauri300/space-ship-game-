import math


class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getMagnitude(self):
        return math.sqrt(self.__x*self.__x + self.__y*self.__y)

    def setDirection(self, angle):
        return Vector2D(math.cos(angle)*self.getMagnitude(), math.sin(angle)*self.getMagnitude())