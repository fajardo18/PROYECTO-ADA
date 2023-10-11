from proyecto_integrador import main_loop, string_to_matrix
from class_juego import Juego
from class_juegoArchivo import JuegoArchivo

laberinto = """..###########
....#.......#
###.#.###.###
#...#...#...#
#.#####.#.#.#
#...#.#.#.#.#
#.#.#.#####.#
#.#.....#.#.#
#.###.###.#.#
#.#.........#
###.#####.###
#.......#...#
###########.#"""

mapa = string_to_matrix(laberinto)


def main():
    main_loop(mapa, (0, 0), (11, 12))

    path_a_mapas = 'mapas'  # Reemplaza esto con la ubicación de tus mapas
    juego = JuegoArchivo(path_a_mapas)
    juego.main_loop()


if __name__ == "__main__":
    main()
