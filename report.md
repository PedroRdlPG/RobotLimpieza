# Informe de Simulación de Robots de Limpieza Multiagente

## Introducción

Se ha desarrollado una simulación de robots de limpieza reactivos que operan en un entorno compartido, siguiendo un enfoque multiagente. Los agentes trabajan de manera independiente, sin comunicación entre ellos, y tienen como objetivo limpiar una habitación representada por una matriz de celdas.

## Objetivos

- Evaluar cómo la cantidad de agentes afecta el tiempo necesario para limpiar la habitación y el número total de movimientos realizados.
- Analizar la eficiencia del sistema en términos de colaboración entre agentes (aunque no se comuniquen entre sí) y su efecto en el tiempo de limpieza.

## Configuración de la Simulación

- **Dimensiones de la habitación**: 10 x 10 celdas.
- **Número de agentes**: 5.
- **Porcentaje de celdas sucias inicialmente**: 30%.
- **Tiempo máximo de ejecución**: 60 segundos.

## Módulos del Proyecto

- **`config.py`**:
  - **Función**: Módulo propio que contiene los parámetros de configuración de la simulación.
  - **Uso en el código**: Proporciona valores como las dimensiones de la habitación, el número de agentes, el porcentaje de suciedad y el tiempo máximo de ejecución.

- **`room.py`**:
  - **Función**: Define la estructura de la habitación y las celdas sucias.
  - **Uso en el código**: Crea y maneja la matriz que representa la habitación y su estado (celdas limpias o sucias).

- **`agent.py`**:
  - **Función**: Define la clase `CleaningAgent`, que representa a un agente de limpieza con comportamiento reactivo.
  - **Uso en el código**: Implementa el comportamiento de los agentes, su movimiento y acciones de limpieza.

## Librerías Utilizadas

- **`threading`**:
  - **Función**: Permite la creación y gestión de hilos (threads) para ejecutar tareas concurrentemente.
  - **Uso en el código**:
    - **`threading.Thread`**: Cada agente de limpieza es un hilo independiente que hereda de esta clase.
    - **`threading.Lock`**: Se utiliza como un "candado global" que los agentes se turnan para acceder de forma segura a los datos compartidos de la habitación y sus posiciones. Este `lock` evita que dos agentes accedan a la misma casilla al mismo tiempo, evitando conflictos de acceso simultáneo.

- **`time`**:
  - **Función**: Proporciona funciones relacionadas con el manejo del tiempo.
  - **Uso en el código**:
    - **`time.time()`**: Para medir el tiempo transcurrido y controlar la duración de la simulación.
    - **`time.sleep()`**: Para simular el tiempo que tarda un agente en realizar una acción.

- **`random`**:
  - **Función**: Generación de números y selecciones aleatorias.
  - **Uso en el código**:
    - **Inicialización aleatoria**: Distribuir las celdas sucias al inicio de la simulación.
    - **Movimientos aleatorios**: Determinar la dirección en la que se moverá un agente cuando la celda actual esté limpia.

Todas estas librerías son parte de la **biblioteca estándar de Python**, por lo que no se requiere la instalación de paquetes externos.

## Resultados

### Ejecución con 5 Agentes

- **Tiempo total de simulación**: **20.16 segundos**.
- **Porcentaje de celdas limpias**: **100.00%**.
- **Número total de movimientos realizados**: **934**.

**Estado final de la habitación**:

```
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
C C C C C C C C C C
```

### Observaciones

- Los agentes lograron limpiar el 100% de las celdas sucias en un tiempo significativamente menor al tiempo máximo permitido.
- El número total de movimientos realizados indica que los agentes exploraron eficientemente el entorno.
- La impresión del estado final de la habitación muestra que todas las celdas están limpias (`C` representa una celda limpia y `D` una celda sucia).

## Análisis de Resultados

- **Efecto del Número de Agentes en el Tiempo de Limpieza**:
  - Con 5 agentes, el tiempo necesario para limpiar todas las celdas sucias fue de aproximadamente 20 segundos.
  - Al aumentar el número de agentes, el tiempo de limpieza puede reducirse, pero también aumenta la posibilidad de que los agentes interfieran entre sí si no se maneja adecuadamente la sincronización.

- **Eficiencia y Colaboración Implícita**:
  - Aunque los agentes no se comunican entre sí, la implementación de un `lock` global garantiza que los agentes trabajen de manera segura y eviten colisiones, como intentar limpiar la misma casilla al mismo tiempo.
  - Los agentes evitan moverse a celdas ocupadas por otros agentes, lo que reduce la redundancia en sus movimientos.

## Conclusiones

- **Sincronización Exitosa**: El uso de `threading.Lock` ha sido efectivo para evitar conflictos de acceso simultáneo y asegurar que los agentes interactúen con el entorno de manera segura.
- **Eficiencia del Sistema Multiagente**: El sistema demuestra que es posible lograr una limpieza completa de manera eficiente con múltiples agentes, siempre que se maneje adecuadamente la sincronización y el acceso a recursos compartidos.
- **Potencial de Mejora**:
  - **Estrategias de Movimiento**: Implementar estrategias más inteligentes podría reducir el número de movimientos necesarios y el tiempo total de limpieza.
  - **Comunicación Entre Agentes**: Aunque no era parte de los requisitos, permitir cierta comunicación podría mejorar aún más la eficiencia.

## Recomendaciones

- **Pruebas Adicionales**: Realizar simulaciones con diferentes números de agentes y porcentajes de suciedad para analizar el impacto en el rendimiento.
- **Optimización**: Explorar algoritmos de movimiento más sofisticados, como búsqueda sistemática o patrones predefinidos, para mejorar la cobertura del espacio.

## Integrantes

- **Pedro Ruiz de la Peña Gaytan** - [A01562734]
- **Gilberto Alejandro Cordero Nuñez** - [A01562929]