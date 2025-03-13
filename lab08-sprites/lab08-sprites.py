import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.07
SPRITE_SCALING_SLIME = 0.03
SPRITE_SCALING_EYE = 0.02
SLIME_COUNT = 50
EYE_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.slime_list = None
        self.eye_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.slime_list = arcade.SpriteList()
        self.eye_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\GUIA.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(SLIME_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\SLIME_VERDE.png", SPRITE_SCALING_SLIME)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.slime_list.append(coin)
        for i in range(EYE_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            eye = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\OJO.png", SPRITE_SCALING_EYE)

            # Position the coin
            eye.center_x = random.randrange(SCREEN_WIDTH)
            eye.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.eye_list.append(eye)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.slime_list.draw()
        self.player_list.draw()
        self.eye_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.slime_list.update()
        self.eye_list.update()

        # Generate a list of all sprites that collided with the player.
        slimes_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.slime_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for slime in slimes_hit_list:
            slime.remove_from_sprite_lists()
            self.score += 1
        eyes_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.eye_list)
        for eye in eyes_hit_list:
            eye.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()