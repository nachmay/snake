from game_parameters import *

class Bomb:
    def __init__(self):
        x, y, radius, time = get_random_bomb_data()
        self.radius = radius
        self.location = (x, y)
        self.x = x
        self.y = y
        self.time = time
        self.temp_radius = 0


    def blast_cells(self, radius):
        blast = []
        for col in range(WIDTH):
            for row in range(HEIGHT):
                if abs(self.x - col) + abs(self.y - row) == radius:
                    blast.append((col, row))
        return blast


)