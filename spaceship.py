import math
from game_object import GameObject
from helpers import *
from physics import Vector2d


class Spaceship(GameObject):
    def __init__(self, position):
        """initializing an Spaceship object given it's position"""
        super(Spaceship, self).__init__(position,\
            load_image_convert_alpha('spaceship-off.png'))
        
        self.image_on = load_image_convert_alpha('spaceship-on.png')
        self.direction = Vector2d(0, -1)
        self.is_throttle_on = False
        self.angle = 0

    def draw_on(self, screen):
        """Draw the spaceship on the screen"""

        new_image, rect = rotate_center(self.image, self.image.get_rect(), self.angle)
        
        draw_position_x = self.position.x
        draw_position_y = self.position.y
        
        if (abs(draw_position_x) > screen.get_width()) or (abs(draw_position_y) > screen.get_height()):
            draw_position_x = draw_position_x / 10.0
            draw_position_y = draw_position_y / 10.0
        
        draw_centered(new_image, screen, (draw_position_x, draw_position_y))


    def move(self):
        """Do one frame's worth of updating for the object"""
        
        # calculate the direction from the angle variable
        self.direction.x = math.sin(-math.radians(self.angle))
        self.direction.y = -math.cos(math.radians(self.angle))
        
        # calculate the position from the direction and speed
        self.position.x += self.velocity.x*self.speed
        self.position.y += self.velocity.y*self.speed
        
        
    def rel_factor(self):
        return 1.0 - math.pow(self.velocity.magnitude(), 2) / math.pow(self.c, 2)    