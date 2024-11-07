# Simulación de Robots de Limpieza Multiagente

Un programa en Python que simula un sistema de robots de limpieza reactivos operando en un entorno compartido. Los agentes trabajan de manera concurrente para limpiar una habitación representada por una matriz, siguiendo un enfoque multiagente con sincronización adecuada.

## Cómo Ejecutar

1. **Clonar el repositorio** o descargar los archivos del proyecto.

2 . **Ejecutar `simulation.py`** usando Python

## Estructura del Proyecto

- **`config.py`**: Contiene los parámetros de configuración de la simulación (dimensiones de la habitación, número de agentes, porcentaje de suciedad, tiempo máximo).

- **`room.py`**: Define la estructura de la habitación y maneja el estado de las celdas (limpias o sucias).

- **`agent.py`**: Implementa la clase `CleaningAgent`, que representa a cada robot de limpieza con su comportamiento.

- **`simulation.py`**: Inicializa la simulación, crea los agentes y gestiona la ejecución de los hilos.

- **`report.md`**: Documento que presenta el análisis del desempeño de la simulación.

## NOTA ADICIONAL:

Para más detalles sobre la simulación y sus resultados, consulta el archivo [`report.md`](./report.md).

## Integrantes

- **Pedro Ruiz de la Peña Gaytan** - [A01562734]
- **Gilberto Alejandro Cordero Nuñez** - [A01562929]