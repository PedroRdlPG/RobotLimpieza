import random
from config import ROOM_DIMENSIONS, DIRT_PERCENTAGE
import threading

class Room:
    def __init__(self):
        self.rows, self.cols = ROOM_DIMENSIONS  # Dimensiones de la habitación
        # Crear una matriz para representar la habitación (0: limpio, 1: sucio)
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.lock = threading.Lock()  # Lock para sincronización
        self.initialize_dirt()  # Inicializar las celdas sucias

    def initialize_dirt(self):
        total_cells = self.rows * self.cols
        dirt_cells = int((DIRT_PERCENTAGE / 100) * total_cells)
        cells = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        dirty_cells = random.sample(cells, dirt_cells)  # Seleccionar celdas sucias aleatoriamente
        for i, j in dirty_cells:
            self.grid[i][j] = 1  # Marcar la celda como sucia

    def is_dirty(self, position):
        i, j = position
        with self.lock:
            return self.grid[i][j] == 1  # Retorna True si la celda está sucia

    def clean_cell(self, position):
        i, j = position
        with self.lock:
            self.grid[i][j] = 0  # Limpia la celda

    def is_all_clean(self):
        with self.lock:
            for row in self.grid:
                if 1 in row:
                    return False  # Hay al menos una celda sucia
            return True  # Todas las celdas están limpias

    def get_dimensions(self):
        return self.rows, self.cols  # Retorna las dimensiones de la habitación

    def print_room(self):
        with self.lock:
            for row in self.grid:
                print(' '.join(['D' if cell == 1 else 'C' for cell in row]))
            print('\n')
