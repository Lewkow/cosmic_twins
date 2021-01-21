import math

class Vector2d(object):
    
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
        
    def magnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
