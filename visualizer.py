import pygame
from grid import Grid
from multi_agent_system import MultiAgentSystem
import random

class Visualizer:
    def __init__(self, grid: Grid, system: MultiAgentSystem, fps: int = 30):
        self.grid = grid
        self.system = system
        self.fps = fps
        self.cell_size = 50  # Tamaño de cada celda
        self.info_line_height = 20  # Altura de cada línea de información
        self.info_height = 40 + len(system.agents) * self.info_line_height  # Altura del panel de información depende del número de agentes
        pygame.init()
        # Ajustar el tamaño de la pantalla incluyendo el panel de información dinámico
        self.screen = pygame.display.set_mode(
            (self.grid.width * self.cell_size, self.grid.height * self.cell_size + self.info_height)
        )
        pygame.display.set_caption("Simulación Multi-Agente Mejorada")
        self.font = pygame.font.SysFont("Arial", 18)
        self.agent_colors = self.generate_agent_colors(len(system.agents))  # Colores únicos para cada agente

    def generate_agent_colors(self, num_agents: int):
        """Generar colores únicos y vibrantes para cada agente."""
        return [(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for _ in range(num_agents)]

    def draw_grid(self):
        """Dibujar la cuadrícula con líneas grises."""
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size + self.info_height, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)  # Líneas más claras

    def draw_obstacles(self):
        """Dibujar los obstáculos con un color oscuro y con borde."""
        for obstacle in self.grid.obstacles:
            pygame.draw.rect(self.screen, (50, 50, 50), pygame.Rect(
                obstacle[0] * self.cell_size, obstacle[1] * self.cell_size + self.info_height, self.cell_size, self.cell_size))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                obstacle[0] * self.cell_size, obstacle[1] * self.cell_size + self.info_height, self.cell_size, self.cell_size), 2)

    def draw_agents(self):
        """Dibujar los agentes con colores únicos y añadir transparencia."""
        for i, agent in enumerate(self.system.agents):
            color = self.agent_colors[i]
            # Dibujar el agente con transparencia
            agent_surface = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)
            pygame.draw.circle(agent_surface, (*color, 180), (self.cell_size // 2, self.cell_size // 2), 20)  # Color con transparencia
            self.screen.blit(agent_surface, (agent.start[0] * self.cell_size, agent.start[1] * self.cell_size + self.info_height))

            # Dibujar el objetivo con un borde blanco y relleno transparente
            pygame.draw.circle(self.screen, (255, 255, 255), 
                               (agent.goal[0] * self.cell_size + self.cell_size // 2, agent.goal[1] * self.cell_size + self.cell_size // 2 + self.info_height), 14, 2)
            pygame.draw.circle(self.screen, (0, 255, 0, 180), 
                               (agent.goal[0] * self.cell_size + self.cell_size // 2, agent.goal[1] * self.cell_size + self.cell_size // 2 + self.info_height), 10)

    def draw_info_panel(self):
        """Dibujar el panel de información en la parte superior de la pantalla."""
        pygame.draw.rect(self.screen, (240, 240, 240), (0, 0, self.grid.width * self.cell_size, self.info_height))  # Fondo del panel de información

        total_steps = sum(agent.steps_taken for agent in self.system.agents)
        status_text = f"Pasos totales dados: {total_steps}"
        text_surface = self.font.render(status_text, True, (0, 0, 0))
        self.screen.blit(text_surface, (10, 10))

        for i, agent in enumerate(self.system.agents):
            status = f"Agente {i}: Pasos {agent.steps_taken}/{agent.max_steps} - "
            if agent.start == agent.goal:
                status += "Objetivo alcanzado"
            elif not agent.is_active:
                status += "Detenido (límite de pasos)"
            else:
                status += "En movimiento"
            text_surface = self.font.render(status, True, (0, 0, 0))
            self.screen.blit(text_surface, (10, 40 + i * self.info_line_height))

    def draw(self):
        """Dibujar la escena completa."""
        self.screen.fill((255, 255, 255))  # Fondo blanco
        self.draw_info_panel()  # Dibujar el panel de información
        self.draw_grid()  # Dibujar la cuadrícula
        self.draw_obstacles()  # Dibujar obstáculos
        self.draw_agents()  # Dibujar agentes y objetivos
        pygame.display.flip()

    def run(self):
        """Ejecutar el visualizador."""
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.system.step()  # Actualizar la lógica de los agentes
            self.draw()  # Dibujar la nueva escena
            clock.tick(self.fps)  # Ajustar FPS
        pygame.quit()
