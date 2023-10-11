import random
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Juego:
    mapa: List[List[str]]
    px: int
    py: int
    start: Tuple[int, int]
    end: Tuple[int, int]

    @staticmethod
    def string_to_matrix(laberinto: str) -> List[List[str]]:
        return [list(fila) for fila in laberinto.strip().split('\n')]

    def screen(self):
        os.system('clear')
        for fila in self.mapa:
            print(''.join(fila))

    def main_loop(self):
        while (self.px, self.py) != self.end:
            self.screen()
            key = readkey()
            self.move(key)

    def move(self, key: str):
        x, y = 0, 0

        if key == readkey.UP:
            x, y = -1, 0
        elif key == readkey.DOWN:
            x, y = 1, 0
        elif key == readkey.LEFT:
            x, y = 0, -1
        elif key == readkey.RIGHT:
            x, y = 0, 1

        new_px, new_py = self.px + x, self.py + y

        if (
                0 <= new_px < len(self.mapa) and
                0 <= new_py < len(self.mapa[0]) and
                self.mapa[new_px][new_py] != '#'
        ):
            self.mapa[self.px][self.py] = '.'
            self.px, self.py = new_px, new_py
            self.mapa[self.px][self.py] = 'P'


@dataclass
class JuegoArchivo(Juego):
    path_a_mapas: str

    def __post_init__(self):
        # Obtener la lista de archivos de mapas en la carpeta especificada
        archivos_mapa = os.listdir(self.mapas)
        print(archivos_mapa)

        # Elegir un archivo aleatorio de la lista
        nombre_archivo = random.choice(archivos_mapa)
        path_completo = os.path.join(self.mapas, nombre_archivo)

        # Leer el archivo de mapa y obtener el contenido
        mapa_str = self.leer_mapa_archivo(path_completo)

        # Llamar al constructor de la clase base (Juego) con el mapa leído
        super().__init__(
            mapa=self.string_to_matrix(mapa_str),
            px=0,
            py=0,
            start=(0, 0),
            end=(len(self.mapa) - 1, len(self.mapa[0]) - 1)
        )

    @staticmethod
    def leer_mapa_archivo(path_completo):
        with open(path_completo, 'r') as archivo_mapa:
            contenido = archivo_mapa.read()
        return contenido.strip()

path_a_mapas = 'mapas'
    juego = JuegoArchivo(path_a_mapas, px=0, py=0, start=(0, 0), end=(0, 0))