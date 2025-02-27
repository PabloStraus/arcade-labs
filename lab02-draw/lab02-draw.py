#MONGOLO EL QUE LO LEA
import arcade
arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()
arcade.draw_circle_filled(690, 470, 400, arcade.color.BABY_BLUE)
arcade.draw_circle_filled(690, 470, 150, arcade.color.LIGHT_SKY_BLUE)
#-----SUELO-----#
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(390, 1, 220, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(190, 1, 250, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(690, 1, 150, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(590, 1, 150, arcade.color.BANGLADESH_GREEN)
arcade.draw_circle_filled(80, 1, 250, arcade.color.BANGLADESH_GREEN)


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

#-----LLAMADAS-----#

#Sol
sol(690, 470, 80)

#Nubes
nubes(290, 400, 21)
nubes(500, 500, 27)
nubes(690, 300, 19)
nubes(100, 500, 22)

#Arbustos
arbustos(690, 100, 19)
arbustos(290, 40, 19)
arbustos(80, 100, 19)
arbustos(490, 150, 19)
arbustos(490, 150, 19)

#arbol
arbol(80,275)
arbol(400,100)
arbol(300,120)
arbol(210,200,)
arbol(130,120)

#-----FIN-----#
arcade.finish_render()
arcade.run()
