# Simulación de Robots de Limpieza Multiagente

Un programa en Python que simula un sistema de robots de limpieza reactivos operando en un entorno compartido. Los agentes trabajan de manera concurrente para limpiar una habitación representada por una matriz, siguiendo un enfoque multiagente con sincronización adecuada.

## Cómo Ejecutar

1. **Clonar el repositorio** o descargar los archivos del proyecto.

2. **Navegar al directorio** donde se encuentran los archivos:

   cd /ruta/al/directorio/RobotLimpieza

3. **Ejecutar `simulation.py`** usando Python:

   python simulation.py

   Asegúrate de tener Python 3 instalado en tu sistema.

## Estructura del Proyecto

- **`config.py`**: Contiene los parámetros de configuración de la simulación (dimensiones de la habitación, número de agentes, porcentaje de suciedad, tiempo máximo).

- **`room.py`**: Define la estructura de la habitación y maneja el estado de las celdas (limpias o sucias).

- **`agent.py`**: Implementa la clase `CleaningAgent`, que representa a cada robot de limpieza con su comportamiento.

- **`simulation.py`**: Inicializa la simulación, crea los agentes y gestiona la ejecución de los hilos.

- **`report.md`**: Documento que presenta el análisis del desempeño de la simulación.

## Requisitos

- **Python 3.x**: El programa utiliza características de Python 3, por lo que es necesario tenerlo instalado.

## Integrantes

- **Pedro Ruiz de la Peña Gaytan** - [A01562734]
- **Gilberto Alejandro Cordero Nuñez** - [A01562929]