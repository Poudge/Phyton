from ursina import *
import random

class Apple(Entity):
    def __init__(self, MAP_SIZE,**kwargs):
        super().__init__(**kwargs)
        self.MAP_SIZE = MAP_SIZE

    def new_position(self):
        self.position = \
            (random.randrange(self.MAP_SIZE) + 0.5, random.randrange(self.MAP_SIZE) + 0.5, -0.5)


class Snake:
    def __init__(self, MAP_SIZE):
        self.MAP_SIZE = MAP_SIZE
        self.segmant_size = 1
        self.position_leght = segmant_size +1
        self.segment_positon = [Vec3(random.randrange(MAP_SIZE))]
        self.segmant_obj = []

