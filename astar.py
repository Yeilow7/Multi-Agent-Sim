# astar.py

from typing import List, Tuple, Dict, Optional
import heapq

def manhattan_distance(start: Tuple[int, int], goal: Tuple[int, int]) -> int:
    """Calculate the Manhattan distance heuristic for A*."""
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def reconstruct_path(came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]], 
                     current: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Reconstructs the path from start to goal."""
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        if current is not None:
            total_path.append(current)
    return total_path[::-1]  # Reverse the path

def a_star_search(grid, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """Perform A* search to find the shortest path from start to goal."""
    if not grid.passable(start) or not grid.passable(goal):
        return None  # No path if start or goal are not passable
    
    open_set = []
    heapq.heappush(open_set, (0, start))  # Priority queue based on f_score
    came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
    
    g_score: Dict[Tuple[int, int], float] = {start: 0}  # Cost from start to each node
    f_score: Dict[Tuple[int, int], float] = {start: manhattan_distance(start, goal)}
    
    while open_set:
        current = heapq.heappop(open_set)[1]  # Node with lowest f_score
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in grid.get_neighbors(current):
            tentative_g_score = g_score[current] + grid.get_cost(current, neighbor)
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

