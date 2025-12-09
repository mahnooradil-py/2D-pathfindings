"""
It:
- defines example grids,
- sets the start and goal positions,
- runs BFS on an unweighted grid,
- runs A* on a weighted grid,
- prints the paths and visualises them.
"""
from pathfinding_bfs import bfs_path
from pathfinding_astar import astar_path
from grid_visualisation import print_grid_with_path


def main():
    # BFS (unweighted grid)
    # 1 = walkable
    # 0 = obstacle
    bfs_grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1]
    ]

    start = (0, 0)   # top-left corner
    goal = (3, 4)    # near bottom-right

    print("=== BFS (unweighted grid) ===")
    bfs_result = bfs_path(bfs_grid, start, goal)
    print("BFS path:", bfs_result, "\n")
    print_grid_with_path(bfs_grid, bfs_result, start, goal)

    # A* (weighted grid)
    # 0 = obstacle
    # 1 = normal ground (cheap)
    # 3 = harder terrain (e.g. hill)
    # 5 = very hard terrain (e.g. water or mud)
    weighted_grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 3, 5, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 5, 1]
    ]

    print("=== A* (weighted grid) ===")
    astar_result = astar_path(weighted_grid, start, goal)
    print("A* path:", astar_result, "\n")
    print_grid_with_path(weighted_grid, astar_result, start, goal)


# This ensures main() only runs when
# this file is executed directly
if __name__ == "__main__":
    main()
