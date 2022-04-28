

from gameObjects.gameObject import *
class MovingObject(GameObject):
    def __init__(self):
        super().__init__()
        self._velocity = Vector2D(0, 0)
        self._angle = 0


