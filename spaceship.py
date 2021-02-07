import math
from game_object import GameObject
from helpers import *
from physics import Vector2d


class Spaceship(GameObject):
    def __init__(self, position):
        """initializing an Spaceship object given it's position"""
        super(Spaceship, self).__init__(position,\
            load_image_convert_alpha('spaceship.png'))
        
        self.image_on = load_image_convert_alpha('spaceship.png')
        self.direction = Vector2d(0, -1)
        self.is_throttle_on = False
        self.angle = 0

    def draw_on(self, screen):
        """Draw the spaceship on the screen"""

        # select the image, based on spaceship accelerating
        if self.is_throttle_on:
            new_image, rect = rotate_center(self.image_on, \
                self.image_on.get_rect(), self.angle)
        else:
            new_image, rect = rotate_center(self.image, \
                self.image.get_rect(), self.angle)
        if (self.position.x > screen.get_width()) or (self.position.y > screen.get_height()) or (self.position.x < 0) or (self.position.y < 0):
            multiplier = 2
        else:
            multiplier = 1
            
        draw_position_x = -screen.get_width() + 2.0 * self.position.x / screen.get_width() 
        draw_position_y = -screen.get_height() + 2.0 * self.position.y / screen.get_height()
        draw_centered(new_image, screen, (self.position.x, self.position.y))


    def move(self):
        """Do one frame's worth of updating for the object"""
        
        # calculate the direction from the angle variable
        self.direction.x = math.sin(-math.radians(self.angle))
        self.direction.y = -math.cos(math.radians(self.angle))
        
        # calculate the position from the direction and speed
        self.position.x += self.velocity.x*self.speed / 100.0
        self.position.y += self.velocity.y*self.speed / 100.0
        
        
    def rel_factor(self):
        return 1.0 - math.pow(self.velocity.magnitude(), 2) / math.pow(self.c, 2)    