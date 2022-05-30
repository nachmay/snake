from bomb import *
from apple import *


GREEN = "green"
RED = "red"
BLACK = "black"
ORANGE = "orange"


class Game:
    """ a class for the snake game which contains all the
    methods concerning interactions with one object to another """

    def __init__(self, snake):
        """initializing the game with the following objects:
         snake, bomb and three apples, along with some vars"""
        self.snake = snake
        self.occupied_coordinates = []
        self.bomb = self.new_bomb()
        self.apple_lst = [self.new_apple(), self.new_apple(), self.new_apple()]
        self.apple_cells = None
        self.score = 0
        self.eat_apple_counter = 0
        self.blast_counter = 0
        self.blast_cells = []

    def game_initializer(self, gd):
        """the function initiate the game and paint the
        board for the first time"""
        self.occupied_coordinates += self.snake.snake_body
        for i in range(len(self.snake.snake_body) - 1, -1, -1):
            x, y = self.snake.snake_body[i]
            gd.draw_cell(x, y, BLACK)
        x, y = self.bomb.location
        gd.draw_cell(x, y, RED)
        self.apple_cells = list(map((lambda apple: apple.location), self.apple_lst))
        for i in self.apple_cells:
            x, y = i
            gd.draw_cell(x, y, GREEN)

    def move(self):
        """the function move the snake"""
        # if the snake eat apple and need to grow
        if self.eat_apple_counter > 0:
            self.snake.move_snake()
            self.eat_apple_counter -= 1
        else: # if not
            self.snake.move_snake()
            self.snake.snake_body.pop(0)

    def new_apple(self):
        """ the function create new apple"""
        # making sure the apple gets an empty spot
        while True:
            apple_i = Apple()
            if apple_i.location not in self.occupied_coordinates:
                self.occupied_coordinates += [apple_i.location]
                return apple_i

    def new_bomb(self):
        """ the function create new bomb"""
        # making sure the bomb gets an empty spot
        while True:
            bomb = Bomb()
            if bomb.location not in self.occupied_coordinates:
                self.occupied_coordinates += [bomb.location]
                return bomb

    def eat_apple(self):
        """the function update what necessary after
        eating apple event"""
        for i in range(len(self.apple_lst)):
            if self.snake.snake_body[-1] == self.apple_lst[i].location:
                self.score += self.apple_lst[i].score
                self.eat_apple_counter += 3
                apple_to_remove = self.apple_lst[i].location
                self.apple_lst[i] = self.new_apple()
                self.occupied_coordinates.remove(apple_to_remove)

    def blast_on_apple(self):
        """the function checks if the blast hit an apple """
        for i in range(len(self.apple_lst)):
            if self.apple_lst[i].location in self.blast_cells:
                self.occupied_coordinates.remove(self.apple_lst[i].location)
                self.apple_lst[i] = self.new_apple()

    def blast_appearence(self):
        """the function updated the blast cells by the frames"""
        self.bomb.time -= 1
        # when the blast expends
        if self.bomb.time <= 0 and self.blast_counter <= self.bomb.radius:
            if self.bomb.time == 0:
                self.occupied_coordinates.remove(self.bomb.location)
                self.bomb.location = ()
                self.blast_cells = self.bomb.blast_cells(self.blast_counter)
                self.blast_counter += 1
            elif self.bomb.time < 0:
                self.blast_cells = self.bomb.blast_cells(self.blast_counter)
                self.blast_counter += 1
        # when we reached the bomb radius
        elif self.blast_counter > self.bomb.radius:
            self.blast_cells = []
            self.bomb = self.new_bomb()
            self.blast_counter = 0

    def paint(self, gd):
        """ a function that pain the board"""
        apple_cells = list(map((lambda apple: apple.location), self.apple_lst))
        for i in apple_cells:
            x, y = i
            gd.draw_cell(x, y, GREEN)
        for i in range(len(self.snake.snake_body)-1, -1, -1):
            x, y = self.snake.snake_body[i]
            if self.snake.snake_body[i] in self.blast_cells:
                gd.draw_cell(x, y, ORANGE)
            if self.snake.snake_body[i] == self.bomb.location:
                gd.draw_cell(x, y, RED)
            else:
                gd.draw_cell(x, y, BLACK)
        if self.bomb.location != ():
            x, y = self.bomb.location
            gd.draw_cell(x, y, RED)
        for i in self.blast_cells:
            x, y = i
            gd.draw_cell(x, y, ORANGE)

    def paint_and_show_screen(self, gd):
        """a small function to make the main loop
         look tidy and more orgenize"""
        self.paint(gd)
        gd.end_round()

    def bomb_collition(self):
        """the function checks if the snake hit a bomb"""
        for i in range(len(self.snake.snake_body)):
            if self.snake.snake_body[i] == self.bomb.location:
                return False
        return True

    def blast_on_snake_head(self):
        """a function that checks if the snake-head hit the blast"""
        if self.snake.snake_body[-1] in self.blast_cells:
            return False
        return True

    def blast_collition_on_snake_body(self):
        """a function that checks if the snake-body hit the blast"""
        for i in range(len(self.snake.snake_body)):
            if self.snake.snake_body[i] in self.blast_cells:
                return False
        return True









