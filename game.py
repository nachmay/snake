from snake import *
from bomb import *
from apple import *


GREEN = "green"
RED = "red"
BLACK = "black"
ORANGE = "orange"


class Game:

    def __init__(self, snake):
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
        if self.eat_apple_counter > 0:
            self.snake.move_without_pop(self.eat_apple_counter)
            self.eat_apple_counter -= 1
        else:
            self.snake.move_snake()

    def new_apple(self):
        while True:
            apple_i = Apple()
            if apple_i.location not in self.occupied_coordinates:
                self.occupied_coordinates += [apple_i.location]
                return apple_i
    # todo to remove the prev apple fro oocupied coordinates

    def new_bomb(self):
        while True:
            bomb = Bomb()
            if bomb.location not in self.occupied_coordinates:
                self.occupied_coordinates += [bomb.location]
                return bomb


    def eat_apple(self):
        for i in range(len(self.apple_lst)):
            if self.snake.snake_body[-1] == self.apple_lst[i].location:
                self.score += self.apple_lst[i].score
                self.eat_apple_counter += 3
                apple_to_remove = self.apple_lst[i].location
                self.apple_lst[i] = self.new_apple()
                self.occupied_coordinates.remove(apple_to_remove)


    def blast_on_apple(self):
        for i in range(len(self.apple_lst)):
            if self.apple_lst[i].location in self.blast_cells:
                self.occupied_coordinates.remove(self.apple_lst[i].location)
                self.apple_lst[i] = self.new_apple()


    def blast_appearence(self):
        self.bomb.time -= 1
        if self.bomb.time <= 0 and self.blast_counter <= self.bomb.radius:
            if self.bomb.time == 0:
                self.occupied_coordinates.remove(self.bomb.location)
                self.bomb.location = ()
                self.blast_cells = self.bomb.blast_cells(self.blast_counter)
                self.blast_counter += 1
            elif self.bomb.time < 0:
                self.blast_cells = self.bomb.blast_cells(self.blast_counter)
                self.blast_counter += 1
        elif self.blast_counter > self.bomb.radius:
            self.blast_cells = []
            self.bomb = self.new_bomb()
            self.blast_counter = 0


    def paint(self, gd):
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
        self.paint(gd)
        gd.end_round()

    def bomb_collition(self):
        for i in range(len(self.snake.snake_body)):
            if self.snake.snake_body[i] == self.bomb.location:
                return False
        return True

    def blast_on_snake_head(self):
        if self.snake.snake_body[-1] in self.blast_cells:
            return False
        return True

    def blast_collition_on_snake_body(self):
        for i in range(len(self.snake.snake_body)):
            if self.snake.snake_body[i] in self.blast_cells:
                return False
        return True

    # def blast_collition_on_head(self, head, blast_cells):
    #     x, y = head
    #     print("(x, y+1) = ", (x, y+1))
    #     if self.snake.direction == UP and (x, y+1) in blast_cells:
    #         print("(x, y+1) = ", (x, y+1))
    #         return False
    #     if self.snake.direction == DOWN and (x, y-1) in blast_cells:
    #         return False
    #     if self.snake.direction == LEFT and (x-1, y) in blast_cells:
    #         return False
    #     if self.snake.direction == RED and (x+1, y) in blast_cells:
    #         return False
    #     return True
    #









