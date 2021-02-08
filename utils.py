import numpy as np
from datastructures import DepthFirstStorage
import numpy as np

from datastructures import DepthFirstStorage


class RandomMaze:
    """
    represents an nxn maze
    """

    def __init__(self, m, n):
        self.m, self.n = m, n
        self.maze = self.generate_maze(m, n)
        self.end_pos = self.set_end_position()

    def start_position(self):
        return (0, 0)

    def goal_position(self):
        return self.end_pos

    def set_end_position(self):
        rng = np.arange(self.n)
        while True:
            i, j = np.random.choice(rng, 2)
            if self.maze[i, j] == 1:
                return (i, j)

    @property
    def shape(self):
        return (self.n, self.n)

    def __len__(self):
        return self.n

    def __str__(self):
        return str(self.maze)

    def __getitem__(self, item):
        return self.maze[item]

    def generate_maze(self, m, n):
        maze = np.zeros((m, n))
        curr_pos = (0, 0)
        self.storage = DepthFirstStorage()
        self.discovered_positions = set()
        self.storage.add_position(curr_pos)
        while len(self.storage) > 0:
            curr_pos = self.storage.get_next_position()
            neighbors = self.get_undiscovered_neighbors(maze, curr_pos)
            if len(neighbors) > 0:
                self.discover(curr_pos)
                nbr = neighbors[int(np.random.choice(np.arange(len(neighbors))))]
                maze[nbr] = 1
                self.discover(nbr)
        return maze

    def get_undiscovered_neighbors(self, maze, pos):
        """
        :param pos:
        :return:
        """
        i, j = pos
        l, r = (i, max(0, j - 1)), (i, min(self.n - 1, j + 1))
        u, d = (max(0, i - 1), j), (min(self.m - 1, i + 1), j)
        posns = []
        for p in [l, r, u, d]:
            if p not in self.discovered_positions:
                if maze[p] == 0:
                    posns.append(p)
        return posns

    def discover(self, *posns):
        """Discover the positions
        """
        for pos in posns:
            self.discovered_positions.add(pos)
            self.storage.add_position(pos)
