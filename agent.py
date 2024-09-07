import numpy as np
from collections import defaultdict
from typing import List, Tuple, Dict

class Agent:
    def __init__(self, id: int, grid, start: Tuple[int, int], goal: Tuple[int, int]):
        self.id = id
        self.grid = grid
        self.start = start
        self.goal = goal
        self.path: List[Tuple[int, int]] = []
        self.is_active = True
        
        # Cálculo de la distancia inicial para determinar el límite dinámico de pasos
        self.initial_distance = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
        self.max_steps = self.initial_distance * 30  # Pasos permitidos
        self.steps_taken = 0  # Contador de pasos

    def set_path(self, path: List[Tuple[int, int]]) -> None:
        self.path = path

class QLearningAgent(Agent):
    def __init__(self, id: int, grid, start: Tuple[int, int], goal: Tuple[int, int], 
                 learning_rate: float = 0.1, discount_factor: float = 0.9, 
                 exploration_rate: float = 0.2, num_actions: int = 4):
        super().__init__(id, grid, start, goal)
        self.q_table: Dict[Tuple[int, int], np.ndarray] = defaultdict(lambda: np.zeros(num_actions))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.num_actions = num_actions

    def choose_action(self, state: Tuple[int, int]) -> int:
        """
        Elegir la mejor acción basada en los valores Q actuales o explorar de manera aleatoria.
        """
        if np.random.rand() < self.exploration_rate:
            # Explorar: elige una acción aleatoria
            return np.random.choice(self.num_actions)
        # Explotar: elige la acción con el mayor valor Q
        return np.argmax(self.q_table[state])

    def update_q_value(self, state: Tuple[int, int], action: int, reward: float, next_state: Tuple[int, int]) -> None:
        """
        Actualizar el valor Q para el estado y la acción dados.
        """
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        td_delta = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.learning_rate * td_delta

    def calculate_reward(self, current_state: Tuple[int, int], next_state: Tuple[int, int]) -> float:
        """
        Calcular la recompensa basada en la distancia al objetivo.
        Recompensa positiva si se acerca al objetivo, negativa si se aleja.
        """
        current_distance = abs(current_state[0] - self.goal[0]) + abs(current_state[1] - self.goal[1])
        next_distance = abs(next_state[0] - self.goal[0]) + abs(next_state[1] - self.goal[1])
        
        # Recompensa mayor si se acerca al objetivo
        if next_distance < current_distance:
            return 1  # Se está acercando al objetivo
        else:
            return -1  # Se está alejando o no progresa

    def step(self) -> None:
        """
        Actualiza el estado del agente en cada paso.
        """
        # Si el agente ya no está activo (ha llegado o excedido el límite de pasos), no hace nada
        if not self.is_active:
            return

        # Si el agente ha alcanzado su objetivo
        if self.start == self.goal:
            print(f"Agente {self.id} ha alcanzado su objetivo en {self.goal}.")
            self.is_active = False
            return

        # Si el agente ha excedido el límite de pasos
        if self.steps_taken >= self.max_steps:
            print(f"Agente {self.id} ha excedido el límite de pasos. Deteniendo.")
            self.is_active = False
            return

        # Obtener el estado actual y los vecinos
        current_state = self.start
        neighbors = self.grid.get_neighbors(current_state)

        if len(neighbors) > 0:
            action = self.choose_action(current_state)
            next_state = neighbors[action % len(neighbors)]  # Mapea la acción a un vecino válido

            # Calcular la recompensa
            reward = self.calculate_reward(current_state, next_state)
            
            # Actualizar la posición del agente
            self.start = next_state
            
            # Actualizar el valor Q
            self.update_q_value(current_state, action, reward, next_state)

            # Incrementar el contador de pasos
            self.steps_taken += 1
        else:
            print(f"Agente {self.id} no tiene vecinos válidos para moverse desde {current_state}")
