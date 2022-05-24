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


    def blast_cells_general(self, radius):
        blast_general = []
        for col in range(self.x - radius, self.x + radius+1):
            for row in range(self.y - radius, self.y + radius+1):
                if abs(self.x - col) + abs(self.y - row) == radius:
                    blast_general.append((col, row))
        return blast_general



# b = Bomb()
# print("blast(0) = ", b.blast_cells(0))
# print("blast(1) = ", b.blast_cells(1))
# print("blast(2) = ", b.blast_cells(2))
# print("blast_general(0) = ", b.blast_cells_general(0))
# print("blast_general(1) = ", b.blast_cells_general(1))
# print("blast_general(2) = ", b.blast_cells_general(2))