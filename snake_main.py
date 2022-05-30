from game_parameters import *
from game_display import GameDisplay
from game import Game
from snake import Snake


def main_loop(gd: GameDisplay) -> None:
    """ a function that combine all the classes
    together and function as the main engine of the game"""
    snake_game = Game(Snake())
    snake_game.game_initializer(gd)
    gd.show_score(snake_game.score)
    gd.end_round()
    # the loop
    while True:
        gd.show_score(snake_game.score)
        # get inf from user and move the snake accordingly
        key_clicked = gd.get_key_clicked()
        snake_game.snake.change_direction(key_clicked)
        snake_game.move()
        # check if the snake hit a bomb or the
        # blast or the screen edge or himself
        if not snake_game.bomb_collition():
            snake_game.paint_and_show_screen(gd)
            return
        if not snake_game.blast_on_snake_head():
            snake_game.snake.snake_body.pop()
            snake_game.paint_and_show_screen(gd)
            return
        if not snake_game.snake.screen_edge() or not snake_game.snake.self_collition():
            snake_game.snake.snake_body = snake_game.snake.snake_body[:-1]
            snake_game.paint_and_show_screen(gd)
            return
        # check if the snake ate any apples
        snake_game.eat_apple()
        if len(snake_game.occupied_coordinates + snake_game.blast_cells) == HEIGHT * WIDTH:
            snake_game.paint_and_show_screen(gd)
            return
        # updating score, blast, and check if the blast hit any apple
        gd.show_score(snake_game.score)
        snake_game.blast_appearence()
        snake_game.blast_on_apple()
        # check if blast hit the snake
        if not snake_game.blast_collition_on_snake_body():
            snake_game.paint_and_show_screen(gd)
            return
        # painting the board
        snake_game.paint_and_show_screen(gd)

