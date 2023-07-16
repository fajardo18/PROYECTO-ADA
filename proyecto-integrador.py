# Parte 1.

nombre = input("Nombre del jugador: ")
print("Bienvenido,", str(nombre), "\n" "Ahora juguemos!")

# Parte 2.

import readchar
# Bucle infinito
while True:
    # Leer un carácter
    char = readchar.readkey()
    # Imprimir el carácter
    print("Carácter ingresado:", char)
    # Verificar si se presionó la tecla UP
    if char == readchar.key.UP:
        break
