""" BFS explores the grid level by level and finds the SHORTEST path
when all walkable cells have the same cost (1). """
from collections import deque


def bfs_path(grid, start, goal):
    """Return the shortest path from start to goal using BFS."""

    rows = len(grid)
    cols = len(grid[0])

    # Check if position is inside the grid
    def inside(row, col):
        return 0 <= row < rows and 0 <= col < cols

    # Basic checks
    if not inside(start[0], start[1]): return None
    if not inside(goal[0], goal[1]): return None
    if grid[start[0]][start[1]] == 0: return None
    if grid[goal[0]][goal[1]] == 0: return None

    # If start equals goal
    if start == goal:
        return [start]

    # BFS setup
    queue = deque([start])        # cells to explore
    visited = {start}             # cells already visited
    parents = {start: None}       # to rebuild the path later

    # Moves we can make (up, down, left, right)
    moves = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    # Main BFS loop
    while queue:
        row, col = queue.popleft()

        # If we reached the goal → rebuild the path
        if (row, col) == goal:
            return build_path(parents, goal)

        # Try all four directions
        for row_change, col_change in moves:
            new_row = row + row_change
            new_col = col + col_change

            if inside(new_row, new_col):
                if grid[new_row][new_col] == 1:
                    if (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        parents[(new_row, new_col)] = (row, col)
                        queue.append((new_row, new_col))

    # If BFS finishes with no goal found → no path
    return None


def build_path(parents, goal):
    """Rebuilds the path backwards from goal to start."""
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return path
