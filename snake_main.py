from game_parameters import *
from game_display import GameDisplay
from snake import Snake
from bomb import Bomb
from apple import Apple


def create_new_apple(occupied_coordinates):
    while True:
        apple = Apple()
        if not apple.location in occupied_coordinates:
            # occupied_coordinates += apple.location
            return apple


def create_new_bomb(occupied_coordinates):
    while True:
        bomb = Bomb()
        if not bomb.location in occupied_coordinates:
            # occupied_coordinates += bomb.location
            return bomb


def eat_apple(apple_lst, snake, score, counter, occupied_coordinates):
    for apple in apple_lst:
        if snake.apple_eating(apple.location):
            score += apple.score
            counter += 3
            occupied_coordinates.remove(tuple(apple.location))
            # new_apple = create_new_apple(occupied_coordinates)
            # occupied_coordinates += new_apple.location
            #

def initializer():
    playing_snake = Snake()
    occupied_coordinates = []
    occupied_coordinates += playing_snake.snake_body
    playing_bomb = create_new_bomb(occupied_coordinates)
    occupied_coordinates += playing_bomb.location
    playing_apple1 = create_new_apple(occupied_coordinates)
    occupied_coordinates += playing_apple1.location
    playing_apple2 = create_new_apple(occupied_coordinates)
    occupied_coordinates += playing_apple2.location
    playing_apple3 = create_new_apple(occupied_coordinates)
    apple_lst = [playing_apple1, playing_apple2, playing_apple3]
    return apple_lst, playing_bomb, playing_snake


def bang(radius, temp_radius):



def main_loop(gd: GameDisplay) -> None:
    score = 0
    count_when_eat = 0
    apple_lst, playing_bomb, playing_snake = initializer()
    gd.end_round()
    gd.show_score(score)

    while True:
        occupied_coordinates = playing_snake.snake_body + playing_bomb.location + playing_bomb.blast + \
                               list(map((lambda apple: apple.location), apple_lst))
        playing_snake.move_without_pop(count_when_eat) if count_when_eat > 0 else playing_snake.move_snake()
        if len(occupied_coordinates) == HEIGHT * WIDTH:
            return
        key_clicked = gd.get_key_clicked()
        playing_snake.change_direction(key_clicked)
        if not playing_snake.self_collition() or not playing_snake.screen_edge() or not playing_snake.bomb_or_blast_collition(
                playing_bomb.location, playing_bomb.blast, gd):
            return
        eat_apple(apple_lst, playing_snake, score, count_when_eat, occupied_coordinates)
        if playing_bomb.time == 0:






        # for apple in apple_lst:
        #     if playing_snake.apple_eating(apple.location):
        #         score += apple.score
        #         apple = Apple()
        #         if apple.location in




# apple_lst = [, Apple(), Apple()]
# occupied_coordinates += list(map((lambda apple: apple.location), apple_lst))
#         if count_when_eat > 0:
#             playing_snake.move_without_pop(count_when_eat)
#         else:
#             playing_snake.move_snake()