from game_parameters import *

UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"


K_LEFT = "Left"
K_RIGHT = 'Right'
K_UP = 'Up'
K_DOWN = 'Down'


class Snake:
    def __init__(self):
        self.snake_body = [((WIDTH // 2), (HEIGHT // 2) - 2), ((WIDTH // 2), (HEIGHT // 2) - 1),
                           ((WIDTH // 2), (HEIGHT // 2))]
        self.direction = UP

    def move_snake(self):
        x, y = self.snake_body[-1]
        if self.direction == UP:
            self.snake_body.append((x, y + 1))
        if self.direction == DOWN:
            self.snake_body.append((x, y - 1))
        if self.direction == RIGHT:
            self.snake_body.append((x + 1, y))
        if self.direction == LEFT:
            self.snake_body.append((x - 1, y))
        self.snake_body.pop(0)

    def move_without_pop(self, counter):
        x, y = self.snake_body[-1]
        if self.direction == UP:
            self.snake_body.append((x, y + 1))
        if self.direction == DOWN:
            self.snake_body.append((x, y - 1))
        if self.direction == RIGHT:
            self.snake_body.append((x + 1, y))
        if self.direction == LEFT:
            self.snake_body.append((x - 1, y))
        counter -= 1

    def change_direction(self, key_clicked):
        if (key_clicked == K_LEFT) and self.direction != RIGHT:
            self.direction = LEFT
        elif (key_clicked == K_RIGHT) and self.direction != LEFT:
            self.direction = RIGHT
        elif (key_clicked == K_UP) and self.direction != DOWN:
            self.direction = UP
        elif (key_clicked == K_DOWN) and self.direction != UP:
            self.direction = DOWN

    def self_collition(self):
        if self.snake_body[-1] in self.snake_body[:-1]:
            return False
        return True

    def screen_edge(self):
        x, y = self.snake_body[-1]
        if x < 0 or x > WIDTH-1 or y < 0 or y > HEIGHT-1:
            return False
        return True

    def blast_collition(self, blast_cells):
        for i in self.snake_body:
            if i in blast_cells:
            #     x, y = i
            #     gd.draw_cell(x, y, "orange")
                return False
        return True

    def bomb_colition(self, bomb_location):
        if self.snake_body[-1] == bomb_location:
            # x, y = bomb_location
            # gd.draw_cell(x, y, "red")
            return False
        return True

    def apple_eating(self, apple_location):
        if self.snake_body[-1] == apple_location:
            return True


