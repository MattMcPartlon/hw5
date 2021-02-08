import time
from typing import Iterable, Tuple, List

from data_structures import PositionStorage
from utils import RandomMaze as Maze


class MazeSearch:

    def __init__(self, storage: PositionStorage):
        # store the set of discovered positions that have not yet been explored
        # during the search
        self.storage = storage
        # stores any position that has been seen during the maze search
        self.discovered_positions = set()
        # parent list - stores the position where each entry was discovered from
        self.parents = {}
        # stores state information for tracking the duration of the search
        self.start_time, self.end_time = 0, 0
        # dimensions of the maze being searched (num rows, num columns)
        self.m, self.n = -1, -1
        # the terminal and starting positions of the maze
        self.goal_position = None
        self.start_position = None

    def num_explored(self) -> int:
        """The number of positions explored during the search

        The number of positions that have been explored, i.e. discovered
        and processed, during the search
        """
        return len(self.discovered_positions) - len(self.storage)

    def num_discovered(self) -> int:
        """The number of positions discovered during the search

        The number of positions that have been discovered during the search
        """
        return len(self.discovered_positions)

    def search_time(self) -> float:
        """Time accrued during the search procedure
        """
        return self.end_time - self.start_time

    def solution_path(self) -> List[Tuple[int, int]]:
        """The path from starting position to goal position in the maze
        :return:
        """
        path = [self.goal_position]
        while self.parents[path[-1]] is not None:
            path.append(self.parents[path[-1]])
        assert path[-1] == self.start_position
        return list(reversed(path))

    def finishedQ(self, current_position) -> bool:
        """Determines if we are finished with the search
        """
        is_goal = current_position == self.goal_position
        return is_goal or len(self.storage) == 0

    def search(self, maze: Maze) -> bool:
        """Searches a maze for the goal position,
        beginning from the mazes starting position
        """
        # clear any state information from previous searches
        # and update state for the maze being solved
        self.storage.clear()
        self.storage.update(maze)
        self.parents = {}
        self.m, self.n = maze.shape
        self.goal_position = maze.goal_position()
        self.start_position = maze.start_position()
        self.discovered_positions = set()
        self.start_time = time.time()
        # add starting position to storage container and discovered vertices
        # search the maze
        found = self._search(maze)
        self.end_time = time.time()
        return found

    def _search(self, maze: Maze) -> bool:
        """
        Searches the maze until the end position is found
        :param maze:
        :return: True if the end position is found, otherwise False.
        """
        current_position = maze.start_position()
        self.storage.add_position(current_position)
        self.discovered_positions.add(current_position)
        self.parents[current_position] = None
        while not self.finishedQ(current_position):
            # Get and search from the current position
            # TODO
            # Search the maze - get the (yet to be discovered) neighbors of
            # the current position
            # TODO
            # Update the parent pointers and discover the added vertices
            # TODO
            pass
        return current_position == self.goal_position

    def get_undiscovered_neighbors(self, maze: Maze, pos: Tuple[int, int]) -> Iterable[Tuple[int, int]]:
        """Returns a list of (undiscovered) open cells neighboring
        the current position, pos
        """
        i, j = pos
        # TODO

    def discover(self, *posns) -> None:
        """Discover the positions and updates search state
        """
        # TODO
        pass

    def set_parent(self, parent, *children) -> None:
        """Sets the parent pointer of each child in children to be
        the position of the parent
        :param parent: the parent position from which the children were discovered
        """
        #TODO
        pass

    def print_state(self, maze):
        print('discovered:', self.discovered_positions)
        print('goal_position', self.goal_position)
        print(maze)
        print(maze[self.goal_position])
