import math
from physics import Vector2d

class GameObject(object):
    """All game objects have a position and an image"""
    def __init__(self, position, image, speed=0):
        self.object_time = 0
        self.c = 5
        self.image = image
        self.position = Vector2d(position[0], position[1])
        self.velocity = Vector2d(0, 0)
        self.speed = self.velocity.magnitude()
        
    def get_gamma(self):
        return 1.0 / math.sqrt(1.0 - math.pow(self.speed, 2) / math.pow(self.c, 2))        

    def draw_on(self, screen):
        draw_centered(self.image, screen, self.position)

    def size(self):
        return max(self.image.get_height(), self.image.get_width())

    def radius(self):
        return self.image.get_width()/2