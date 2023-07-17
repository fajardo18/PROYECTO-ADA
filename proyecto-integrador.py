# Parte 1.

nombre = input("Nombre del jugador: ")
print("Bienvenido,", str(nombre), "\n" "Ahora juguemos!")

# Parte 2.

import readchar
# Bucle infinito
while True:
    # Leer un carácter
    key = readchar.readkey()
    # Imprimir el carácter
    print("Carácter ingresado:", key)
    # Verificar si se presionó la tecla UP
    if key == readchar.key.UP:
        break
