import arcade
import os
import game_constants


class Player(arcade.Sprite):
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
        self.score = 0

        self.textures = [
            arcade.load_texture("assets/images/planeRed1.png"),
            arcade.load_texture("assets/images/planeRed2.png"),
            arcade.load_texture("assets/images/planeRed3.png")
        ]
        self.current_texture = 0
        self.set_texture(self.current_texture)

    def update(self):
        # Update the animation.
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.current_texture = 0
            self.set_texture(self.current_texture)

        # Apply mouvement...
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > game_constants.SCREEN_WIDTH - 1:
            self.right = game_constants.SCREEN_WIDTH - 1
        if self.top > game_constants.SCREEN_HEIGHT:
            self.top = game_constants.SCREEN_HEIGHT
        elif self.bottom < 0:
            self.bottom = 0

