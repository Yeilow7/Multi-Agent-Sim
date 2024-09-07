# multi_agent_system.py

from typing import List, Tuple
from agent import QLearningAgent
from grid import Grid

class MultiAgentSystem:
    def __init__(self):
        self.agents: List[QLearningAgent] = []
    
    def add_agent(self, id: str, grid: Grid, start: Tuple[int, int], goal: Tuple[int, int]) -> None:
        """Add a Q-Learning agent to the system."""
        agent = QLearningAgent(id, grid, start, goal)
        self.agents.append(agent)
    
    def step(self) -> None:
        """Update all agents in the system."""
        for agent in self.agents:
            agent.step()
