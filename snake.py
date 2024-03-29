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
    """a class for the  object snake which contain methods concerning the snake alone """
    def __init__(self):
        """initializing the snake location and direction"""
        self.snake_body = [((WIDTH // 2), (HEIGHT // 2) - 2), ((WIDTH // 2), (HEIGHT // 2) - 1),
                           ((WIDTH // 2), (HEIGHT // 2))]
        self.direction = UP

    def move_snake(self):
        """a function that move the snake"""
        x, y = self.snake_body[-1]
        if self.direction == UP:
            self.snake_body.append((x, y + 1))
        if self.direction == DOWN:
            self.snake_body.append((x, y - 1))
        if self.direction == RIGHT:
            self.snake_body.append((x + 1, y))
        if self.direction == LEFT:
            self.snake_body.append((x - 1, y))

    def change_direction(self, key_clicked):
        """a function that changes the direction of the snake
         according to the user choice"""
        if (key_clicked == K_LEFT) and self.direction != RIGHT:
            self.direction = LEFT
        elif (key_clicked == K_RIGHT) and self.direction != LEFT:
            self.direction = RIGHT
        elif (key_clicked == K_UP) and self.direction != DOWN:
            self.direction = UP
        elif (key_clicked == K_DOWN) and self.direction != UP:
            self.direction = DOWN

    def self_collition(self):
        """return false if the snake hit himself"""
        if self.snake_body[-1] in self.snake_body[:-1]:
            return False
        return True

    def screen_edge(self):
        """return false if the snake hit the screen edge"""
        x, y = self.snake_body[-1]
        if x < 0 or x > WIDTH-1 or y < 0 or y > HEIGHT-1:
            return False
        return True






