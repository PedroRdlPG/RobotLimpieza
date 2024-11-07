import threading
import random
import time
from config import MAX_TIME

class CleaningAgent(threading.Thread): #Función para inicializar agentes y sus atributos
    def __init__(self, agent_id, room, start_time, agents_positions):
        threading.Thread.__init__(self)
        self.agent_id = agent_id  # Identificador único para cada agente
        self.room = room  # Referencia al objeto Room compartido
        self.position = (0, 0)  # Posición inicial del agente
        self.moves = 0  # Contador de movimientos realizados
        self.start_time = start_time  # Tiempo de inicio de la simulación
        self.agents_positions = agents_positions  # Diccionario compartido de posiciones de agentes
        self.running = True  # Bandera para controlar la ejecución del hilo

    def run(self):
        while self.running:
            current_time = time.time()
            # Verificar si se alcanzó el tiempo máximo de ejecución
            if current_time - self.start_time >= MAX_TIME:
                self.running = False
                break

            # Verificar si la celda actual está sucia
            if self.room.is_dirty(self.position):
                # Limpiar la celda
                self.room.clean_cell(self.position)
                print(f"Agente {self.agent_id} limpió la celda {self.position}")
            else:
                # Elegir una nueva posición para moverse
                next_position = self.choose_next_position()
                if next_position:
                    # Actualizar la posición del agente en el diccionario compartido
                    with self.room.lock:
                        self.agents_positions[self.agent_id] = next_position
                    self.position = next_position  # Actualizar la posición actual
                    self.moves += 1  # Incrementar el contador de movimientos
                # Si no hay movimiento posible, el agente se queda en su posición actual

            time.sleep(0.1)  # Simular el tiempo de acción

    def choose_next_position(self):
        # Lista de movimientos posibles (8 direcciones)
        possible_moves = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),         (0, 1),
                          (1, -1),  (1, 0),  (1, 1)]
        random.shuffle(possible_moves)  # Aleatorizar los movimientos
        rows, cols = self.room.get_dimensions()

        with self.room.lock:
            # Obtener las posiciones de otros agentes
            other_agents_positions = [pos for agent_id, pos in self.agents_positions.items() if agent_id != self.agent_id]

        for move in possible_moves:
            new_row = self.position[0] + move[0]
            new_col = self.position[1] + move[1]
            # Verificar que la nueva posición esté dentro de los límites
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_position = (new_row, new_col)
                # Verificar que la posición no esté ocupada por otro agente
                if new_position not in other_agents_positions:
                    return new_position  # Retornar la nueva posición válida
        return None  # Si no hay movimiento posible
