from game_parameters import *
from game_display import GameDisplay
from snake import Snake
from bomb import Bomb
from apple import Apple

GREEN = "green"
RED = "red"
BLACK = "Black"
ORANGE = "orange"


def initializer(gd ):
    playing_snake = Snake()
    for i in range(len(playing_snake.snake_body)-1, -1, -1):
        x, y = playing_snake.snake_body[i]
        gd.draw_cell(x, y, BLACK)
    occupied_coordinates = []
    occupied_coordinates += playing_snake.snake_body
    playing_bomb = create_new_bomb(occupied_coordinates)
    x, y = playing_bomb.location
    gd.draw_cell(x, y, RED)
    occupied_coordinates += playing_bomb.location
    playing_apple1 = create_new_apple(occupied_coordinates)
    occupied_coordinates += playing_apple1.location
    playing_apple2 = create_new_apple(occupied_coordinates)
    occupied_coordinates += playing_apple2.location
    playing_apple3 = create_new_apple(occupied_coordinates)
    apple_lst = [playing_apple1, playing_apple2, playing_apple3]
    apple_cells = list(map((lambda apple: apple.location), apple_lst))
    for i in apple_cells:
        x, y = i
        gd.draw_cell(x, y, GREEN)
    gd.end_round()
    return apple_lst, playing_bomb, playing_snake


def create_new_apple(occupied_coordinates):
    while True:
        apple = Apple()
        if not apple.location in occupied_coordinates:
            return apple


def create_new_bomb(occupied_coordinates):
    while True:
        bomb = Bomb()
        if not bomb.location in occupied_coordinates:
            return bomb


def eat_apple(apple_lst, snake, score, counter, occupied_coordinates):
    for i in range(len(apple_lst)):
        if snake.apple_eating(apple_lst[i].location):
            score += apple_lst[i].score
            counter += 3
            apple_lst[i] = create_new_apple(occupied_coordinates)
    return score, counter


def blast_on_apple(apple_lst, blast_cells_to_paint, occupied_coordinates):
    for i in range(len(apple_lst)):
        if apple_lst[i].location in blast_cells_to_paint:
            apple_lst[i] = create_new_apple(occupied_coordinates)


def blast_appearence(blast_cells_to_paint, blast_counter, occupied_coordinates, playing_bomb):
    # playing_bomb_loc_to_paint = playing_bomb.location
    if playing_bomb.time <= 0 and blast_counter <= playing_bomb.radius:
        if len(playing_bomb.blast_cells(blast_counter)) != len(playing_bomb.blast_cells_general(blast_counter)):
            blast_cells_to_paint = []
            playing_bomb = create_new_bomb(occupied_coordinates)
            blast_counter = 0
        else:
            # playing_bomb_loc_to_paint = ()
            playing_bomb.location = ()
            blast_cells_to_paint = playing_bomb.blast_cells(blast_counter)
            blast_counter += 1
    if blast_counter > playing_bomb.radius:
        blast_cells_to_paint = []
        playing_bomb = create_new_bomb(occupied_coordinates)
        blast_counter = 0
    return blast_cells_to_paint, blast_counter, playing_bomb


def paint(apple_lst, blast_cells, snake_cells, bomb_location, gd):
    apple_cells = list(map((lambda apple: apple.location), apple_lst))
    for i in apple_cells:
        x, y = i
        gd.draw_cell(x, y, GREEN)
    for i in range(len(snake_cells)-1, -1, -1):
        x, y = snake_cells[i]
        gd.draw_cell(x, y, BLACK)
    if bomb_location != ():
        x, y = bomb_location
        gd.draw_cell(x, y, RED)
    for i in blast_cells:
        x, y = i
        gd.draw_cell(x, y, ORANGE)
    # if bomb_location == ():
    #     return



def main_loop(gd: GameDisplay) -> None:
    score = 0
    count_when_eat = 0
    apple_lst, playing_bomb, playing_snake = initializer(gd)
    gd.show_score(score)
    blast_counter = 0
    blast_cells_to_paint = []
    blast_flag = True
    bomb_flag = True

    while True:


        gd.show_score(score)
        occupied_coordinates = playing_snake.snake_body + [playing_bomb.location] + playing_bomb.blast_cells(
            blast_counter) + \
                               list(map((lambda apple: apple.location), apple_lst))
        if count_when_eat > 0:
            playing_snake.move_without_pop(count_when_eat)
            count_when_eat -= 1
        else:
            playing_snake.move_snake()
        if len(occupied_coordinates) == HEIGHT * WIDTH:
            flag = False
        key_clicked = gd.get_key_clicked()

        playing_snake.change_direction(key_clicked)
        if not playing_snake.self_collition() or not playing_snake.screen_edge():
            gd.end_round()
            return
        score, count_when_eat = eat_apple(apple_lst, playing_snake, score, count_when_eat, occupied_coordinates)
        playing_bomb.time -= 1
        blast_cells_to_paint, blast_counter, playing_bomb = blast_appearence(blast_cells_to_paint, blast_counter,
                                                                             occupied_coordinates, playing_bomb)
        if not playing_snake.blast_collition(blast_cells_to_paint):
            gd.end_round()
            blast_flag= False
        if not playing_snake.bomb_colition(playing_bomb.location):
            gd.end_round()
            bomb_flag = False

        blast_on_apple(apple_lst, blast_cells_to_paint, occupied_coordinates)
        # paint(apple_lst, blast_cells_to_paint, playing_snake.snake_body, playing_bomb.location, gd)
        # gd.end_round()
        paint(apple_lst, blast_cells_to_paint, playing_snake.snake_body, playing_bomb.location, gd)
        if not bomb_flag:

            x, y = playing_bomb.location
            gd.draw_cell(x, y, "Red")
            gd.end_round()
            return

        if not blast_flag:
            for i in playing_snake.snake_body:
                if i in blast_cells_to_paint:
                    x, y = i
                    gd.draw_cell(x, y, "orange")
                    break
                # print("didnt?")
            #     print("blabla")
            #     x, y = playing_bomb.location
            #     gd.draw_cell(x, y, "red")
            gd.end_round()
            return
        gd.end_round()

