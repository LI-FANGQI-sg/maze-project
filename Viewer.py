import Maze

def view(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == Maze.EMPTY:
                print("__", end = "")
            elif grid[i][j] == Maze.WALL:
                print("XX", end = "")
            elif grid[i][j] == Maze.START:
                print("ST", end = "")
            elif grid[i][j] == Maze.END:
                print("EN", end = "")
            elif grid[i][j] == Maze.VISITED:
                print("::", end = "")
            else:
                raise AssertionError
        print()
