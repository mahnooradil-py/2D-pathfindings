# Colour codes for terminal text
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def print_grid_with_path(grid, path, start, goal):
    """Print the grid showing S (start), G (goal), * (path), and # (obstacles)."""

    rows = len(grid)
    cols = len(grid[0])
    path_set = set(path) if path else set()

    print("Grid:")
    for row in range(rows):
        line = ""
        for col in range(cols):
            pos = (row, col)

            if pos == start:
                line += BLUE + "S" + RESET
            elif pos == goal:
                line += BLUE + "G" + RESET
            elif grid[row][col] == 0:
                line += RED + "#" + RESET
            elif pos in path_set:
                line += GREEN + "*" + RESET
            else:
                line += "."
        print(line)

    print("\nLegend:")
    print(BLUE + "S" + RESET + " = Start")
    print(BLUE + "G" + RESET + " = Goal")
    print(GREEN + "*" + RESET + " = Path")
    print(RED + "#" + RESET + " = Obstacle")
    print(". = Walkable cell\n")
