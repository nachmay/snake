from game_parameters import *

class Bomb:
    def __init__(self):
        x, y, radius, time = get_random_bomb_data()
        self.radius = radius
        self.location = [(x, y)]
        self.x = x
        self.y = y
        self.time = time
        self.blast = []
        self.temp_radius = 0


    def blast_cells(self, radius):
        for col in range(WIDTH-1):
            for row in range(HEIGHT-1):
                if abs(self.x - col) + abs(self.y - row) == radius:
                    self.blast.append((col, row))
        # self.temp_radius += 1







# b = Bomb()
# print(b.location)
# print("x = ", b.x, "y = ", b.y, "radius = ", b.radius)
# b.blast_cells()
# print(b.blast)


