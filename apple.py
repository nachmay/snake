from game_parameters import *


class Apple:
    def __init__(self):
        x, y, score = get_random_apple_data()
        self.score = score
        self.location = [(x, y)]
        self.x = x
        self.y = y


    def get_apple_location(self):
        return self.location

    # def paint(self, gd):
    #     gd.draw_cells(self.x, self.y, "green")






