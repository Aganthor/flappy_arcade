import arcade
import game_constants


class Obstacle(arcade.Sprite):
    MOVE_SPEED = 3

    def __init__(self, flipped):
        """

        :param flipped: If true, flip the texture in the Y axis so that it points downward.
        """
        super().__init__()
        if flipped:
            self.textures = [arcade.load_texture("assets/images/rockGrassDown.png")]
        else:
            self.textures = [arcade.load_texture("assets/images/rockGrass.png")]

        self.current_texture = 0
        self.set_texture(self.current_texture)
        self.center_x = game_constants.SCREEN_WIDTH
        if flipped:
            self.center_y = game_constants.SCREEN_HEIGHT
        else:
            self.center_y = 0

        self.scale = 2.5
        self.change_x = -Obstacle.MOVE_SPEED

    def update(self):
        super().update()
        # Despawn-self if out of bounds.
        if self.right < 0:
            self.remove_from_sprite_lists()


