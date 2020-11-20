import arcade
import os


class Player(arcade.AnimatedTimeSprite):
    """
    Simple class to represent our little user controlled plane in the
    game.
    """
    MOVE_SPEED = 5
    MAX_LIVES = 3
    PLAYER_SCALE = 1.0

    def __init__(self):
        super().__init__()

        self.number_of_lives = Player.MAX_LIVES
        self.center_y = 100
        self.center_x = 100
        self.current_index = 0
        self.score = 0
        self.textures = []

        for i in range(3):
            self.textures.append(arcade.load_texture(os.path.join('assets/images/', 'planeRed' + str(i + 1) + '.png')))

        self.cur_texture_index = 0

