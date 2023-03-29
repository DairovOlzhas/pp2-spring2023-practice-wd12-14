import random

# Define constants for the maze grid
CELL_SIZE = 20
WALL = 'W'
PATH = 'P'
ENTRANCE = 'E'
EXIT = 'X'

# Define the dimensions of the maze grid
GRID_WIDTH = # write your natural number
GRID_HEIGHT = # write your natural number

# Define colors
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (1, 255, 255)

# Define a function to generate a random maze using a recursive backtracking algorithm
def generate_maze():
    maze_grid = [[WALL for y in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)]
    
    x_entrance = random.randint(1, GRID_WIDTH - 2)

    maze_grid[x_entrance][0] = ENTRANCE

    to_visit = set([(x_entrance, 1)])
    visited = set()

    def get_neighbors(x, y):
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    def is_wall(x,y):
        return (0 <= x < GRID_WIDTH) and (0 <= y < GRID_HEIGHT) and maze_grid[x][y] == WALL
    
    def get_neighbors_walls(x, y):
        return [n for n in get_neighbors(x,y) if is_wall(n[0],n[1])]

    def can_be_next_path(x,y):
        neighbors_walls = get_neighbors_walls(x, y)
        return (
            (1 <= x < GRID_WIDTH-1) and (1 <= y < GRID_HEIGHT-1) 
            and len(neighbors_walls) == 3
            and maze_grid[x][y] == WALL
        )

    while len(to_visit) > 0:
        x, y = random.choice(list(to_visit))

        visited.add((x,y))

        maze_grid[x][y] = PATH
        next_paths = [
            n for n in get_neighbors(x,y) 
            if can_be_next_path(n[0],n[1])
        ]

        if len(next_paths) > 0:
            next_path = random.choice(next_paths)
            if next_path not in visited:
                to_visit.add(next_path)
            maze_grid[next_path[0]][next_path[1]] = PATH
        else:
            to_visit.remove((x,y))
        
    x_exit = random.choice([x for x in range(1,GRID_WIDTH-1) if maze_grid[x][GRID_HEIGHT-2] == PATH])
    maze_grid[x_exit][GRID_HEIGHT - 1] = EXIT

    return maze_grid
