import arcade
import os
import game_constants


class Player(arcade.AnimatedTimeBasedSprite):
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


    def update(self):
        # Apply mouvement...
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > game_constants.SCREEN_WIDTH - 1:
            self.right = game_constants.SCREEN_WIDTH - 1
        if self.top < 0:
            self.top = 0
        elif self.bottom > game_constants.SCREEN_HEIGHT - 1:
            self.bottom = game_constants.SCREEN_HEIGHT - 1

