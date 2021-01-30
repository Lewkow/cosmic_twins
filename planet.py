from game_object import GameObject
from helpers import *

class Planet(GameObject):
    def __init__(self, position=[0,0]):
        image_name = 'planet.png'
        super(Planet, self).__init__(position, load_image_convert_alpha(image_name))
        self.image = load_image_convert_alpha(image_name)
        
    def draw_on(self, screen):
        draw_centered(self.image, screen, (self.position.x, self.position.y))
