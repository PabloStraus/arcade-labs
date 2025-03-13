"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.2
GRASS_SCALING = 0.5
GRASS2_SCALING = 0.333
STONE_SCALING = 0.25
SLIME_SCALING = 0.1

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.slime_list = None
        self.score = 0
        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.slime_list = arcade.SpriteList()
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\GUIA.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)
        def slime_placer(slime_centerx, slime_centery, nx, ny):
            slime = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\SLIME_VERDE.png", SLIME_SCALING)
            slime.center_x = slime_centerx + 126*nx
            slime.center_y = slime_centery + 126*ny
            self.slime_list.append(slime)
        def wall_maker(wall_centerx, wall_centery, nx, ny):
            x = random.randrange(5)
            if x == 1 or x == 3:
                wall = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\CESPED.png", GRASS_SCALING)
            elif x == 2 or x ==4:
                wall = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\CESPED2.jpg", GRASS2_SCALING)
            else:
                wall = arcade.Sprite(r"C:\Users\pablo\Desktop\PNGS\PRACTICA8\PIEDRA.jpg", STONE_SCALING)
            wall.center_x = wall_centerx + 126*nx
            wall.center_y = wall_centery + 126*ny
            self.wall_list.append(wall)
        def wall_placer(numero, eje, wall_centerx, wall_centery, posx, posy):
            if eje == "y":
                for i in range(numero):
                    wall_maker(wall_centerx, wall_centery, posx, i)
            elif eje == "x":
                for i in range(numero):
                    wall_maker(wall_centerx, wall_centery, i, posy)
        wall_placer(10,"x", 300, 200, 10, 0)
        wall_placer(2, "y", 300, 200, 3, 1)
        wall_placer(10, "x", 300, 200, 10, 3)
        wall_placer(3, "y", 300, 200, 9, 0)
        slime_placer(300, 176, 3, 2)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BABY_BLUE)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.slime_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 50, arcade.color.BLACK, 30)
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.slime_list.update()

        # Generate a list of all sprites that collided with the player.
        slimes_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.slime_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for slime in slimes_hit_list:
            slime.remove_from_sprite_lists()
            self.score += 1


        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()