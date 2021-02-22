"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import player
from obstacle import Obstacle
from random import randint
from game_states import GameState
from explosion import PlaneExplosion
import game_constants


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.player = None
        self.entity_list = None
        self.background = None
        self.obstacle_list = None
        self.coin_list = None
        self.explosion_list = None

        self.game_state = None

        # Pre-load the explosion textures


        # To track player key pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """

        # Setup the background
        self.background = arcade.Sprite("assets/images/background.png", 1.75)
        self.background.center_x = game_constants.SCREEN_WIDTH / 2
        self.background.center_y = game_constants.SCREEN_HEIGHT / 2

        # Setup an arcade timer
        arcade.schedule(self.spawn_single_obstacle, 1.0)
        arcade.schedule(self.spawn_double_obstacle, 3.0)

        # Setup the explosion sprite
        self.explosion_list = arcade.SpriteList()

        self.player = player.Player()

        self.coin_list = arcade.SpriteList()
        self.entity_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()

        self.entity_list.append(self.player)

        self.game_state = GameState.RUNNING

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.background.draw()
        self.entity_list.draw()
        self.obstacle_list.draw()
        self.coin_list.draw()
        self.explosion_list.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.game_state == GameState.PAUSE:
            return

        if self.game_state == GameState.PLAYER_EXPLOSION:
            self.explosion_list.update()
            return

        # Handle user input for the player
        self.player.change_x, self.player.change_y = 0, 0
        if self.up_pressed and not self.down_pressed:
            self.player.change_y = game_constants.MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player.change_y = -game_constants.MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -game_constants.MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = game_constants.MOVEMENT_SPEED

        # Check for collision between the player and the obstacles.
        obstacle_hit_list = arcade.check_for_collision_with_list(self.player, self.obstacle_list)
        if len(obstacle_hit_list) > 0:
            #explosion = PlaneExplosion(self.explosion_texture_list)
            explosion = PlaneExplosion()
            # Move it to the location of the player
            explosion.center_x = self.player.center_x
            explosion.center_y = self.player.center_y
            # Call update() because it sets which image we start on
            explosion.update()
            self.explosion_list.append(explosion)
            self.game_state = GameState.PLAYER_EXPLOSION
            self.player.remove_from_sprite_lists()
            return

        self.entity_list.update()
        self.entity_list.update_animation()
        self.obstacle_list.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True

        # Hard quit the game (for the moment).
        if key == arcade.key.ESCAPE:
            exit()

        # User pause?
        if key == arcade.key.SPACE:
            if self.game_state == GameState.PAUSE:
                self.game_state = GameState.RUNNING
            elif self.game_state == GameState.RUNNING:
                self.game_state = GameState.PAUSE

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False

    def spawn_single_obstacle(self, delta_time):
        """
        Will be called once every to spawn obstacle in the game. Will consist of a stalagmite or a stalagtite.
        :param delta_time:
        :return:
        """
        if self.game_state == GameState.PAUSE or self.game_state == GameState.PLAYER_EXPLOSION:
            return

        obstacle_type = randint(1, 2)
        if obstacle_type == game_constants.OBSTACLE_DOWNWARD:
            self.obstacle_list.append(Obstacle(True))
        elif obstacle_type == game_constants.OBSTACLE_UPWARD:
            self.obstacle_list.append(Obstacle(False))

    def spawn_double_obstacle(self, delta_time):
        if self.game_state == GameState.PAUSE or self.game_state == GameState.PLAYER_EXPLOSION:
            return

        self.obstacle_list.append(Obstacle(True))
        self.obstacle_list.append(Obstacle(False))


def main():
    """ Main method """
    game = MyGame(game_constants.SCREEN_WIDTH, game_constants.SCREEN_HEIGHT, game_constants.SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
