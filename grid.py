# grid.py

from typing import List, Tuple, Optional

class Grid:
    def __init__(self, width: int, height: int, obstacles: List[Tuple[int, int]]):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)
    
    def in_bounds(self, position: Tuple[int, int]) -> bool:
        """Check if a position is within the grid bounds."""
        (x, y) = position
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, position: Tuple[int, int]) -> bool:
        """Check if a position is not an obstacle."""
        return position not in self.obstacles
    
    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Return the valid neighbors of a given position."""
        (x, y) = position
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_neighbors = [n for n in neighbors if self.in_bounds(n) and self.passable(n)]
        return valid_neighbors

    def get_cost(self, current: Tuple[int, int], neighbor: Tuple[int, int]) -> int:
        """Returns the cost to move from the current position to a neighbor."""
        return 1  # Uniform cost for now, could be extended for different terrains
