#MONGOLO EL QUE LO LEA
import arcade
arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.BABY_BLUE)
arcade.start_render()

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
def arbol(troncox, troncoy, hojasy):
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
arcade.draw_circle_filled(690, 100, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(650, 100, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(670, 100, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(670, 110, 18, arcade.color.AMAZON)

arcade.draw_circle_filled(390, 150, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(350, 150, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(370, 150, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(370, 160, 18, arcade.color.AMAZON)

arcade.draw_circle_filled(290, 80, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(250, 80, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(270, 80, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(270, 90, 18, arcade.color.AMAZON)

arcade.draw_circle_filled(90, 100, 19, arcade.color.AMAZON)
arcade.draw_circle_filled(50, 100, 15, arcade.color.AMAZON)
arcade.draw_circle_filled(70, 100, 17, arcade.color.AMAZON)
arcade.draw_circle_filled(70, 110, 18, arcade.color.AMAZON)

#LLAMADAS A FUNCIONES

#Sol
sol(690, 470, 80)

#Nubes
nubes(290, 400, 21)
nubes(500, 500, 27)
nubes(690, 300, 19)
nubes(100, 500, 22)

#arbol
arbol(80,285,300)
arbol(400,100,115)
arbol(300,80,95)
arbol(210,200,215)
arbol(130,100,115)
#-----FIN-----#
arcade.finish_render()
arcade.run()
