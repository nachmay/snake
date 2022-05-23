from game_parameters import *

class Bomb:
    def __init__(self):
        x, y, radius, time = get_random_bomb_data()
        self.radius = radius
        self.location = (x, y)
        self.time = time

    def blast_cells(self):

