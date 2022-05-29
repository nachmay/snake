from game_parameters import *
from game_display import GameDisplay
from game import Game
from snake import Snake


def main_loop(gd: GameDisplay) -> None:
    snake_game = Game(Snake())
    snake_game.game_initializer(gd)
    gd.show_score(snake_game.score)
    gd.end_round()
    while True:
        gd.show_score(snake_game.score)
        key_clicked = gd.get_key_clicked()
        snake_game.snake.change_direction(key_clicked)
        snake_game.move()
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
        snake_game.eat_apple()
        if len(snake_game.occupied_coordinates + snake_game.blast_cells) == HEIGHT * WIDTH:
            snake_game.paint_and_show_screen(gd)
            return
        gd.show_score(snake_game.score)
        snake_game.blast_appearence()
        snake_game.blast_on_apple()
        if not snake_game.blast_collition_on_snake_body():
            snake_game.paint_and_show_screen(gd)
            return
        snake_game.paint_and_show_screen(gd)

