from algorithm import MazeSearch
from data_structures import BestFirstStorage, BreadthFirstStorage, DepthFirstStorage
from utils import RandomMaze as Maze

ns = [5,10, 20, 30, 40]

# test each storage/search method
storages = [BestFirstStorage(), BreadthFirstStorage(), DepthFirstStorage()]
for storage in storages:
    for n in ns:
        maze = Maze(n, n)
        # solve the maze with each method and record the statistics
        solver = MazeSearch(storage)
        assert solver.search(maze)
        assert solver.solution_path()[0] == maze.start_position()
        assert solver.solution_path()[-1] == maze.goal_position()
        assert solver.num_discovered() >= solver.num_explored()
        assert maze.goal_position() in solver.discovered_positions
        assert maze.start_position() in solver.discovered_positions
