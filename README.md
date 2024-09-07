# Simulación Multi-Agente con Q-Learning y A*

Este proyecto implementa una simulación de un **sistema multi-agente** sobre una cuadrícula, donde cada agente utiliza **Q-Learning** para aprender a moverse eficientemente hacia su objetivo mientras evita obstáculos generados aleatoriamente. También se incluye el algoritmo **A*** como alternativa para calcular rutas óptimas. La visualización de la simulación se realiza en tiempo real utilizando **Pygame**, mostrando la evolución de los agentes a medida que interactúan con el entorno.

## Tabla de contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)

## Características

- **Q-Learning**: Un algoritmo de aprendizaje por refuerzo que permite a los agentes aprender de su experiencia y optimizar su ruta hacia el objetivo basándose en recompensas obtenidas durante la exploración.
- **A\***: Un algoritmo heurístico de búsqueda de caminos, utilizado para encontrar la ruta más corta entre dos puntos.
- **Obstáculos aleatorios**: Los obstáculos se generan en posiciones aleatorias, lo que obliga a los agentes a encontrar rutas alternativas hacia sus objetivos.
- **Posiciones de agentes y objetivos aleatorias**: Cada agente tiene una posición de inicio y un objetivo asignados de manera aleatoria al inicio de la simulación.
- **Visualización en tiempo real**: Utilizando Pygame, la simulación se muestra en una cuadrícula, con agentes y objetivos representados con colores diferenciados.
- **Interfaz adaptable**: La interfaz gráfica se adapta dinámicamente según la cantidad de agentes y muestra el estado actual de cada uno (en movimiento, detenido o con el objetivo alcanzado).

## Requisitos

Este proyecto requiere **Python 3.7 o superior** y las siguientes bibliotecas:

- **Pygame**: Para la visualización de la simulación.
- **Numpy**: Para las operaciones numéricas y manejo de matrices.
- **Scipy**: Para el algoritmo de búsqueda A*.

  

## Instalación
Puedes instalar todas las dependencias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
