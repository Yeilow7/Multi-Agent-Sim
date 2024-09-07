import random
from grid import Grid
from multi_agent_system import MultiAgentSystem
from visualizer import Visualizer

def setup_grid(width: int, height: int, num_obstacles: int) -> Grid:
    """Generar una cuadrícula con obstáculos aleatorios."""
    obstacles = set()
    while len(obstacles) < num_obstacles:
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        obstacles.add((x, y))
    return Grid(width, height, list(obstacles))

def setup_agents(system: MultiAgentSystem, grid: Grid, num_agents: int) -> None:
    """Generar agentes con posiciones y objetivos aleatorios."""
    positions = set()
    for i in range(num_agents):
        while True:
            start = (random.randint(0, grid.width - 1), random.randint(0, grid.height - 1))
            goal = (random.randint(0, grid.width - 1), random.randint(0, grid.height - 1))
            if start != goal and start not in grid.obstacles and goal not in grid.obstacles:
                system.add_agent(f"agent_{i}", grid, start, goal)
                positions.add(start)
                positions.add(goal)
                break

def main():
    width, height = 10, 10  # Tamaño de la cuadrícula
    num_obstacles = 10  # Número de obstáculos
    num_agents = 6  # Número de agentes

    grid = setup_grid(width, height, num_obstacles)
    system = MultiAgentSystem()

    setup_agents(system, grid, num_agents)

    visualizer = Visualizer(grid, system)
    visualizer.run()

if __name__ == "__main__":
    main()
