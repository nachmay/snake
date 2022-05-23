from game_display import *
from game_parameters import *
from bomb import Bomb
from apple import Apple

U = "up"
D = "down"
R = "right"
L = "left"


class Snake:
    def __init__(self):
        self.snake_body = [((WIDTH // 2), (HEIGHT // 2) - 2), ((WIDTH // 2), (HEIGHT // 2) - 1),
                           ((WIDTH // 2), (HEIGHT // 2))]
        self.head = self.snake_body[-1]
        self.tail = self.snake_body[0]
        self.direction = U


    def move_snake(self):
        x, y = self.snake_body[-1]
        if self.direction == U:
            self.snake_body.append((x, y + 1))
        if self.direction == D:
            self.snake_body.append((x, y - 1))
        if self.direction == R:
            self.snake_body.append((x + 1, y))
        if self.direction == L:
            self.snake_body.append((x - 1, y))
        self.snake_body.pop(0)

    def change_direction(self, key_clicked):
        if (key_clicked == 'Left') and self.direction != R:
            self.direction = L
        elif (key_clicked == 'Right') and self.direction != L:
            self.direction = R
        elif (key_clicked == 'up') and self.direction != D:
            self.direction = U
        elif (key_clicked == 'down') and self.direction != U:
            self.direction = R

    def self_collition(self):
        if self.head in self.snake_body[:-1]:
            return False
        return True

    def screen_edge(self):
        x, y = self.head
        if x < 0 or x > WIDTH or y < 0 or y > HEIGHT:
            return False
        return True

    def bomb_or_blast_collition(self, bomb_location, blast_cells, drew_cell):
        x, y = self.head
        if self.head == bomb_location:
            drew_cell(x, y, "red")
            return False
        if self.head in blast_cells:
            drew_cell(x, y, "orange")
            return False
        return True

    def apple_eating(self, apple_location):
        if self.head == apple_location:
            return True


