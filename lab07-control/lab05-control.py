
""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 18

# -----PERSONA-----#
def persona(centerx:int, centery:int, radius:int):
    arcade.draw_circle_filled(centerx,centery, radius, arcade.color.YELLOW)
    arcade.draw_circle_filled(centerx,centery, radius-10, arcade.color.BANANA_YELLOW)

# -----SOL-----#
def sol(centerx:int, centery:int, radius:int):
    arcade.draw_circle_filled(centerx,centery, radius, arcade.color.YELLOW)
    arcade.draw_circle_filled(centerx,centery, radius-10, arcade.color.BANANA_YELLOW)

#-----ÁRBOL-----#
def arbol(troncox, troncoy):
    hojasy = troncoy + troncoy/19
    arcade.draw_rectangle_filled(troncox, troncoy, troncoy/14.25, troncoy/3.17, arcade.color.DARK_BROWN)
    arcade.draw_rectangle_filled(troncox, hojasy, hojasy/2.5, hojasy/10, arcade.color.CAL_POLY_GREEN)
    arcade.draw_rectangle_filled(troncox, hojasy+hojasy/10, hojasy/3, hojasy/10, arcade.color.CAL_POLY_GREEN)
    arcade.draw_rectangle_filled(troncox, hojasy+hojasy/5, hojasy/3.75, hojasy/10, arcade.color.CAL_POLY_GREEN)
    arcade.draw_rectangle_filled(troncox, hojasy+hojasy/3.33, hojasy/5, hojasy/10, arcade.color.CAL_POLY_GREEN)
    arcade.draw_rectangle_filled(troncox, hojasy+hojasy/2.73, hojasy/7.5, hojasy/10, arcade.color.CAL_POLY_GREEN)
    arcade.draw_rectangle_filled(troncox, hojasy+hojasy/2.14, hojasy/15, hojasy/10, arcade.color.CAL_POLY_GREEN)

#-----NUBES-----#
def nubes(centerx:int, centery:int, radius):
    arcade.draw_circle_filled(centerx, centery, radius, arcade.color.WHITE)
    arcade.draw_circle_filled(centerx-40, centery, radius-3, arcade.color.WHITE)
    arcade.draw_circle_filled(centerx-20, centery+15, radius-1, arcade.color.WHITE)
    arcade.draw_circle_filled(centerx-20, centery, radius, arcade.color.WHITE)

#-----ARBUSTOS-----#

def arbustos(centerx:int, centery:int, radius):
    arcade.draw_circle_filled(centerx, centery, radius, arcade.color.AMAZON)
    arcade.draw_circle_filled(centerx-40, centery, radius-3, arcade.color.AMAZON)
    arcade.draw_circle_filled(centerx-20, centery+15, radius-1, arcade.color.AMAZON)
    arcade.draw_circle_filled(centerx-20, centery, radius, arcade.color.AMAZON)

class Persona:
    def __init__(self, position_x, position_y, radius, color1, color2):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color1 = color1
        self.color2 = color2

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color1)

        arcade.draw_rectangle_filled(self.position_x, self.position_y - self.radius, 10, 60, self.color1)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - self.radius - 10, 30, 10, self.color1)
        arcade.draw_rectangle_filled(self.position_x + 5, self.position_y - self.radius - 30, 10, 10, self.color1)
        arcade.draw_rectangle_filled(self.position_x - 5, self.position_y - self.radius - 30, 10, 10, self.color1)
        arcade.draw_rectangle_filled(self.position_x - 10, self.position_y - self.radius - 40, 10, 20, self.color1)
        arcade.draw_rectangle_filled(self.position_x + 10, self.position_y - self.radius - 40, 10, 20, self.color1)

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius - 5,
                                  self.color2)

class Villano:
    def __init__(self, position_x, position_y, radius, color1, color2, change_x, change_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color1 = color1
        self.color2 = color2
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color1)

        arcade.draw_rectangle_filled(self.position_x, self.position_y - self.radius, 10, 60, self.color1)
        arcade.draw_rectangle_filled(self.position_x, self.position_y - self.radius - 10, 30, 10, self.color1)
        arcade.draw_rectangle_filled(self.position_x + 5, self.position_y - self.radius - 30, 10, 10, self.color1)
        arcade.draw_rectangle_filled(self.position_x - 5, self.position_y - self.radius - 30, 10, 10, self.color1)
        arcade.draw_rectangle_filled(self.position_x - 10, self.position_y - self.radius - 40, 10, 20, self.color1)
        arcade.draw_rectangle_filled(self.position_x + 10, self.position_y - self.radius - 40, 10, 20, self.color1)

        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius - 5,
                                  self.color2)

    def on_update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "GOD DESTROYER",)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.persona = Persona(50, 50, 20, arcade.color.BLACK, arcade.color.WHITE)
        self.villano = Villano(100, 100, 20, arcade.color.RED, arcade.color.WHITE, 0, 0)
        self.set_mouse_visible(False)

    def on_draw(self):
        self.clear()

        arcade.start_render()
        #-----SOL-----#
        sol(690, 470, 80)
        # -----SUELO-----#
        arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BANGLADESH_GREEN)
        arcade.draw_circle_filled(390, 1, 220, arcade.color.BANGLADESH_GREEN)
        arcade.draw_circle_filled(190, 1, 250, arcade.color.BANGLADESH_GREEN)
        arcade.draw_circle_filled(690, 1, 150, arcade.color.BANGLADESH_GREEN)
        arcade.draw_circle_filled(590, 1, 150, arcade.color.BANGLADESH_GREEN)
        arcade.draw_circle_filled(80, 1, 250, arcade.color.BANGLADESH_GREEN)
        # Nubes
        nubes(290, 400, 21)
        nubes(500, 500, 27)
        nubes(690, 300, 19)
        nubes(100, 500, 22)

        # Arbustos
        arbustos(690, 100, 19)
        arbustos(290, 40, 19)
        arbustos(80, 100, 19)
        arbustos(490, 150, 19)
        arbustos(490, 150, 19)

        # arbol
        arbol(80, 275)
        arbol(400, 100)
        arbol(300, 120)
        arbol(210, 200, )
        arbol(130, 120)


        self.persona.draw()
        self.villano.draw()
        arcade.finish_render()

        #MONGOLO EL QUE LO LEA

    def on_update(self, delta_time):
        self.villano.on_update()

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Fiuuuuuum")
            arcade.set_background_color(arcade.color.RED_DEVIL)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)
            arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.persona.position_x = x
        self.persona.position_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            print("The 'w' key was hit")
            self.villano.change_y = MOVEMENT_SPEED
        elif key == arcade.key.A:
            print("The 'a' key was hit")
            self.villano.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.S:
            print("The 's' key was hit")
            self.villano.change_y = -MOVEMENT_SPEED

        elif key == arcade.key.D:
            print("The 'd' key was hit")
            self.villano.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.villano.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.villano.change_y = 0

def main():
    window = MyGame()
    arcade.run()


main()
