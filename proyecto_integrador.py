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

# Parte 4.

import os
import readchar
from typing import List, Tuple


def string_to_matrix(laberinto: str):
    matrix = list(map(list, laberinto.split("\n")))
    return matrix


def screen(mapa):

    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    for row in mapa:
        print(''.join(row))


def main_loop(mapa: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
    px, py = posicion_inicial
    mapa[py][px] = 'P'

    screen(mapa)

    while (px, py) != posicion_final:
        key = readchar.readkey()

        x, y = 0, 0
        if key == readchar.key.UP:
            x, y = -1, 0
        elif key == readchar.key.DOWN:
            x, y = 1, 0
        elif key == readchar.key.LEFT:
            x, y = 0, -1
        elif key == readchar.key.RIGHT:
            x, y = 0, 1

        new_px, new_py = px + x, py + y

        if 0 <= new_px < len(mapa) and 0 <= new_py < len(mapa[0]) and mapa[new_px][new_py] != '#':
            mapa[px][py] = '.'
            px, py = new_px, new_py
            mapa[px][py] = 'P'

            screen(mapa)
            print(px, py)

        if new_px == 12 and new_py == 11:
            break

    print('fin de juego')
