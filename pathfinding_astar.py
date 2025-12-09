"""
Differences from BFS version:
- Works on a WEIGHTED grid.
- Each walkable cell has a COST (e.g. 1 = easy, 5 = difficult).
- 0 still means an obstacle (blocked).

A* tries to find the path with the LOWEST TOTAL COST,
not just the fewest steps.
"""

from heapq import heappush, heappop


def astar_path(grid, start, goal):
    """
    Find a path from start to goal using the A* algorithm.

    The grid is a list of lists of integers:
      0 = obstacle (blocked)
      >0 = cost to ENTER that cell

    Returns:
        A list of (row, col) positions from start to goal (inclusive),
        or None if no path exists.
    """

    rows = len(grid)
    cols = len(grid[0])

    # Helper: is a position inside the grid?
    def inside(row, col):
        return 0 <= row < rows and 0 <= col < cols

    # Helper: simple heuristic = Manhattan distance
    # This is just "how far in rows + columns" the cell is from the goal.
    def heuristic(row, col):
        return abs(row - goal[0]) + abs(col - goal[1])

    # Basic safety checks
    if not inside(start[0], start[1]):
        print("Start position is outside the grid.")
        return None

    if not inside(goal[0], goal[1]):
        print("Goal position is outside the grid.")
        return None

    if grid[start[0]][start[1]] == 0:
        print("Start position is blocked.")
        return None

    if grid[goal[0]][goal[1]] == 0:
        print("Goal position is blocked.")
        return None

    if start == goal:
        # Already at the goal
        return [start]

    # A* uses:
    # - open_set: cells we still need to explore
    # - g_cost: best cost we know so far to reach each cell
    # - parents: to rebuild the path

    # Priority queue for the "open set"
    # Each item is (priority, row, col)
    # priority = g_cost + heuristic (often written as f = g + h)
    open_set = []

    # Cost from start to this cell (g cost)
    g_cost = {start: 0}

    # Parent links for path reconstruction
    parents = {start: None}

    # Start with the start cell
    start_priority = heuristic(start[0], start[1])
    heappush(open_set, (start_priority, start[0], start[1]))

    # Directions we can move: up, down, left, right
    moves = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    while open_set:
        # Get the cell with the LOWEST priority (best guess)
        current_priority, row, col = heappop(open_set)
        current_pos = (row, col)

        # If we reached the goal, rebuild the path
        if current_pos == goal:
            return build_path(parents, goal)

        # Explore neighbours
        for row_change, col_change in moves:
            new_row = row + row_change
            new_col = col + col_change
            neighbour = (new_row, new_col)

            # Check bounds first
            if not inside(new_row, new_col):
                continue

            # Cannot go through obstacles (cost 0 means blocked)
            cell_cost = grid[new_row][new_col]
            if cell_cost == 0:
                continue

            # New cost to reach this neighbour
            # g_cost[current] + cost of ENTERING the neighbour cell
            new_g = g_cost[current_pos] + cell_cost

            # Only update if this is a better (cheaper) route
            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                parents[neighbour] = current_pos

                # Priority = cost so far + heuristic estimate
                priority = new_g + heuristic(new_row, new_col)
                heappush(open_set, (priority, new_row, new_col))

    # If we empty the open set without finding the goal, there is no path
    return None


def build_path(parents, goal):
    """
    Rebuild the path from the goal back to the start,
    using the 'parents' dictionary.
    """
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parents.get(current)

    path.reverse()
    return path
