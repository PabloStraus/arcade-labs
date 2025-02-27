class Sala:
    """
    Clase de sala
    """
    def __init__(self, description, north, west, south, east):
        self.description = description
        self.north = north
        self.west = west
        self.south = south
        self.east = east
def main():
    Habitaciones = []
    keyB = False
    keyBa = False
    keyT = False
    Inicio = Sala("Estas en una sala inicial en la cual solo se encuentra una puerta, en el este, en ella, hay una nota, esta dice 'Si el tesoro quieres buscar, por la mazmorra deberás avanzar'",None,None,None,1)
    Habitaciones.append(Inicio)



    Pasillo = Sala(
            "Llegas a un largo pasillo, esta iluminado por antorchas y hay huesos en el suelo, en el norte hay una puerta cerrada donde dice 'almacen', en el este hay una puerta abierta donde dice 'baños'",
            2, 0, None, 3)
    Habitaciones.append(Pasillo)


    Almacen = Sala(
        "Un gran almacen lleno de huesos, cadenas y armas. Encuentras una llave que dice 'barracones', hay una gran puerta dorada, esta está cerrada.",
        None, None, 1, 5)
    Habitaciones.append(Almacen)


    Baños = Sala(
            "Hay una gran piscina en el centro, con agua caliente, puedes ver cientas de burbujas flotando por el baño, en el suelo se encuentra la llave del almacen, en el este se encuentra una puerta  cerrada con candado",
            None, 1, None, 4)
    Habitaciones.append(Baños)


    Barracones = Sala(
            "Te encuentras en una sala usada para que los guerreros descansen, esta llena de huesos y esqueletos, encuentras una llave dorada que dice 'tesoreria'",
            None, 3, None, None)
    Habitaciones.append(Barracones)


    Tesoreria = Sala(
            "Encuentras una gran pila de monedas de oro, ¡Enhorabuena, has encontrado el tesoro!",
            None, 2, None, None)
    Habitaciones.append(Tesoreria)
    current_room = 0
    done = False
    while done != True:
        print(" ")
        next_room = 0
        print(Habitaciones[current_room].description)
        if keyB == False and current_room == 2:
            print("Esta puerta esta cerrada con llave")
            current_room == Habitaciones[1]


        if current_room == 3 and keyB == False:
            respuesta = input("¿Quieres coger la llave? (y/n) ")
            if respuesta == "y":
                keyB = True
            else:
                keyB = False

        if keyBa == False and current_room == 4:
            print("Esta puerta esta cerrada con llave")
            current_room == Habitaciones[3]

        if current_room == 2 and keyB == True and keyBa == False:
            respuesta = input("¿Quieres coger la llave? (y/n) ")
            if respuesta == "y":
                keyBa = True
            else:
                keyBa = False

        if keyT == False and current_room == 5:
            print("Esta puerta esta cerrada con llave")
            current_room == Habitaciones[2]

        if current_room == 4 and keyBa == True and keyT == False:
            respuesta = input("¿Quieres coger la llave? (y/n) ")
            if respuesta == "y":
                keyT = True
            else:
                keyT = False

        accion = input("¿Qué quieres hacer? ")
        if accion.lower() == "n" or accion == "north" or accion == "norte":
            next_room = Habitaciones[current_room].north #No se si tiene que estar en orden
            if next_room == None:
                print("No puedes ir por ahi")
            else:
                current_room = next_room


        elif accion.lower() == "e" or accion == "east" or accion == "este":
            next_room = Habitaciones[current_room].east #No se si tiene que estar en orden
            if next_room == None:
                print("No puedes ir por ahi")
            else:
                current_room = next_room


        elif accion.lower() == "s" or accion == "south" or accion == "sur":
            next_room = Habitaciones[current_room].south  # No se si tiene que estar en orden
            if next_room == None:
                print("No puedes ir por ahi")
            else:
                current_room = next_room


        elif accion.lower() == "w" or accion == "west" or accion == "oeste":
            next_room = Habitaciones[current_room].west  # No se si tiene que estar en orden
            if next_room == None:
                print("No puedes ir por ahi")
            else:
                current_room = next_room
        elif accion == "exit":
            print("Fin del juego ")
            done = True
        else:
            print("No te he entendido ")

        if current_room == 5:
            print(Habitaciones[5].description)
            done = True



main()
