import arcade
import game_constants


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()

        self.texture.draw_sized(game_constants.SCREEN_WIDTH / 2,
                                game_constants.SCREEN_HEIGHT / 2,
                                game_constants.SCREEN_WIDTH,
                                game_constants.SCREEN_HEIGHT)
