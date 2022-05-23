from game_parameters import *


class Apple:
    def __init__(self):
        x, y, score = get_random_apple_data()
        self.score = score
        self.location = (x, y)

    def get_apple_location(self):
        return self.location




