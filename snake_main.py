import game_parameters
from game_display import GameDisplay
from snake import Snake
from bomb import Bomb
from apple import Apple


def main_loop(gd: GameDisplay) -> None:
    playing_snake = Snake()
    playing_bomb = Bomb()
    playing_apple1 = Apple()
    playing_apple2 = Apple()
    playing_apple3 = Apple()
    gd.end_round()
    gd.show_score(0)
    while True:
        key_clicked = gd.get_key_clicked()
        playing_snake.change_direction(key_clicked)
        if not playing_snake.self_collition() or not playing_snake.screen_edge() or not playing_snake.bomb_or_blast_collition(
                playing_bomb.location, playing_bomb.blast, gd):
            return

