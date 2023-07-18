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

# Parte 3.

import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_number():
    num = 0
    while num <= 50:
        clear_terminal()
        print(num)
        key = readchar.readkey()
        if key == 'n':
            num += 1


print_number()
