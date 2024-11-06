import time
from room import Room
from agent import CleaningAgent
from config import NUM_AGENTS, MAX_TIME

def main():
    room = Room()
    agents = []
    start_time = time.time()
    agents_positions = {}  # Diccionario compartido de posiciones de agentes

    # Crear e iniciar agentes
    for agent_id in range(NUM_AGENTS):
        agent = CleaningAgent(agent_id, room, start_time, agents_positions)
        agents_positions[agent_id] = agent.position  # Inicializar posición
        agent.start()
        agents.append(agent)

    try:
        while True:
            current_time = time.time()
            if current_time - start_time >= MAX_TIME or room.is_all_clean():
                # Detener agentes
                for agent in agents:
                    agent.running = False
                break
            time.sleep(1)
    except KeyboardInterrupt:
        # Permitir detener la simulación con Ctrl+C
        for agent in agents:
            agent.running = False

    # Esperar a que todos los agentes terminen
    for agent in agents:
        agent.join()

    # Recopilar datos
    total_moves = sum(agent.moves for agent in agents)
    total_cells = room.rows * room.cols
    clean_cells = total_cells - sum(row.count(1) for row in room.grid)
    clean_percentage = (clean_cells / total_cells) * 100
    total_time = time.time() - start_time

    print(f"Tiempo total de simulación: {total_time:.2f} segundos")
    print(f"Porcentaje de celdas limpias: {clean_percentage:.2f}%")
    print(f"Número total de movimientos realizados: {total_moves}")

    # Opcional: Mostrar estado final de la habitación
    room.print_room()

if __name__ == "__main__":
    main()
