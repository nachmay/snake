from game_parameters import *

class Apple:
    """a class for the object apple which contain
     methods concerning the snake alone """
    def __init__(self):
        """initializing location and score"""
        x, y, score = get_random_apple_data()
        self.score = score
        self.location = (x, y)
        self.x = x
        self.y = y










