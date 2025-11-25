"""
It sets the grid, chooses start/goal, runs BFS,
and prints the result.
"""

from pathfinding_bfs import bfs_path
from grid_visualisation import print_grid_with_path


def main():
    # Example grid:
    # 1 = walkable
    # 0 = blocked
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1]
    ]

    start = (0, 0)   # top-left corner
    goal = (3, 4)    # near bottom-right

    # Run BFS pathfinding
    path = bfs_path(grid, start, goal)

    # Print results
    print("Path found:", path, "\n")
    print_grid_with_path(grid, path, start, goal)


if __name__ == "__main__":
    main()
