from game_parameters import *

class Bomb:
    """a class for the object bomb which contain
     methods concerning the snake alone """
    def __init__(self):
        """ initializing location, radius, time and temp_radius"""
        x, y, radius, time = get_random_bomb_data()
        self.radius = radius
        self.location = (x, y)
        self.x = x
        self.y = y
        self.time = time
        self.temp_radius = 0


    def blast_cells(self, radius):
        """return a list of the blast cells in a specific frame"""
        blast = []
        for col in range(WIDTH):
            for row in range(HEIGHT):
                if abs(self.x - col) + abs(self.y - row) == radius:
                    blast.append((col, row))
        return blast


