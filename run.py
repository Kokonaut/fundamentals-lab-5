from os import path
import pyglet
import random

from engine.game import Game


window_width = 1400
rows = 9
cols = 16
window_ratio = cols / rows
window_height = int(window_width / window_ratio)

# Set up a window
game_window = pyglet.window.Window(window_width, window_height)

game = Game(game_window, rows, cols, lives=5)

game.add_finish((0.97, 0.67))
game.add_finish((0.97, 0.47))

game.add_tower_spots([
    (0.376, 0.431),
    (0.537, 0.216),
    (0.715, 0.54),
    (0.765, 0.825)
])

path_1 = [
    (0.108, 0.235),
    (0.165, 0.4),
    (0.22, 0.54),
    (0.41, 0.54),
    (0.5, 0.34),
    (0.55, 0.35),
    (0.6, 0.42),
    (0.64, 0.61),
    (0.67, 0.64),
    (0.85, 0.64),
    (0.93, 0.57),
    (1.1, 0.57),
]

path_2 = [
    (0.435, 0.225),
    (0.5, 0.34),
    (0.55, 0.35),
    (0.6, 0.42),
    (0.64, 0.61),
    (0.67, 0.64),
    (0.85, 0.64),
    (0.93, 0.57),
    (1.1, 0.57),
]

monster_config_1 = list()

for _ in range(100):
    type_dice = random.randint(0, 4)
    monster_type = None
    if type_dice == 0:
        monster_type = 'heavy'
    else:
        monster_type = 'fast'

    cooldown = random.uniform(0.2, 5.0)
    monster_config_1.append(
        {
            'type': monster_type,
            'cooldown': cooldown
        }
    )

game.add_spawner(
    (0, 0.235),
    path_1,
    monster_config_1
)

monster_config_2 = list()

for _ in range(100):
    type_dice = random.randint(0, 4)
    monster_type = None
    if type_dice == 0:
        monster_type = 'heavy'
    else:
        monster_type = 'fast'

    cooldown = random.uniform(2.0, 6.0)
    monster_config_2.append(
        {
            'type': monster_type,
            'cooldown': cooldown
        }
    )

game.add_spawner(
    (0.435, 0),
    path_2,
    monster_config_2
)


if __name__ == '__main__':
    game.start_game()
    pyglet.app.run()
