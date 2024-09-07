# test_system.py
import unittest
from grid import Grid
from astar import a_star_search
from agent import QLearningAgent

class TestGrid(unittest.TestCase):
    def setUp(self):
        # Modify obstacle placement to ensure (1, 1) is passable
        self.grid = Grid(5, 5, [(2, 2)])

    def test_get_neighbors(self):
        neighbors = self.grid.get_neighbors((2, 1))
        self.assertIn((1, 1), neighbors)  # Ensure this is passable in the grid
        self.assertNotIn((2, 2), neighbors)  # Ensure obstacle at (2, 2) blocks it

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(5, 5, [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (3, 1)])  # Adjusted to block paths

    def test_a_star_no_path(self):
        # Add a more robust block of obstacles to prevent any path
        self.grid.obstacles.update([(2, 2), (3, 3), (4, 2)])
        path = a_star_search(self.grid, (0, 0), (4, 4))
        self.assertIsNone(path)

class TestQLearningAgent(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(5, 5, [])
        self.agent = QLearningAgent(1, self.grid, (0, 0), (4, 4))

    def test_choose_action_explore(self):
        self.agent.exploration_rate = 1.0  # Force exploration
        action = self.agent.choose_action((0, 0))
        self.assertIn(action, range(4))  # Check it's a valid action

    def test_choose_action_exploit(self):
        self.agent.q_table[(0, 0)][1] = 10  # Make action 1 most favorable
        self.agent.exploration_rate = 0.0  # Force exploitation
        action = self.agent.choose_action((0, 0))
        self.assertEqual(action, 1)

if __name__ == '__main__':
    unittest.main()
