from abc import ABC, abstractmethod
from typing import Tuple

from utils import RandomMaze as Maze


class PositionStorage(ABC):
    """ Datastructure for storing maze positions

    Keeps track of positions that have been discovered
    (not yet visited) during the maze search.

    Concrete instantiations of this class must implement
    three methods:

    1) _add_position(position)
    2) _get_next_position()
    3) clear()
    4) update(maze : np.ndarray)
    5) __len__()


    For a description of each method, see the doc-string.
    """

    def __init__(self, name):
        self.name = name
        pass

    @abstractmethod
    def add_position(self, pos: Tuple[int, int]) -> None:
        """
        Adds the position pos to the datastructure
        :param pos: The position to add
        """
        pass

    @abstractmethod
    def get_next_position(self) -> Tuple[int, int]:
        """Gets the next position to explore

        Gets the next position to explore, and removes it from the
        datastructure

        :return: The next position to explore
        """
        pass

    @abstractmethod
    def clear(self):
        """clears the underlying datastructure by removing any elements and
        resetting any state information
        """
        pass

    @abstractmethod
    def update(self, maze: Maze) -> None:
        """
        update any state information that is maze-dependent
        :param maze:
        :return:
        """
        pass

    @abstractmethod
    def __len__(self):
        """The number of positions currently held by the datastructure
        """
        pass

    def __str__(self):
        return self.name


class DepthFirstStorage(PositionStorage):
    """ Datastructure for storing maze positions

    Last-In-First-Out storage. The last position added to the
    data structure (via add_position) is always the next
    proposed position to explore (i.e. in get_position())

    When used with the maze solver, this data structure
    should produce behavior which mimics DFS
    """

    def __init__(self):
        # TODO
        super().__init__("depth first")
        self.discovered = []
        pass

    def add_position(self, pos: Tuple[int, int]):
        """
        Adds the position pos to the datastructure
        :param pos: The position to add
        """
        self.discovered.append(pos)
        # TODO
        pass

    def get_next_position(self) -> Tuple[int, int]:
        """Gets the next position to explore

        Gets the most recently added position, and removes
        it from the datastructure

        :return: The next position to explore
        """
        return self.discovered.pop()
        # TODO
        pass

    def clear(self):
        """clears the underlying datastructure by removing any elements and
        resetting any state information
        """
        # TODO
        self.discovered = []
        pass

    def update(self, maze: Maze):
        """
        update any state information that is maze-dependent
        :param maze:
        :return:
        """
        # TODO
        pass

    def __len__(self):
        """The number of positions currently held by the datastructure
        """
        # TODO
        return len(self.discovered)
        pass


class BreadthFirstStorage(PositionStorage):
    """ Datastructure for storing maze positions

    First-In-First-Out storage. The (chronologically) oldest
    position added to the data structure (via add_position)
    is always the next proposed position to explore
    (i.e. in get_position())

    When used with the maze solver, this data structure
    should produce behavior which mimics BFS
    """

    def __init__(self):
        super().__init__("breadth first")
        # TODO
        pass

    def add_position(self, pos: Tuple[int, int]):
        """
        Adds the position pos to the datastructure
        :param pos: The position to add
        """
        # TODO
        pass

    def get_next_position(self) -> Tuple[int, int]:
        """Gets the next position to explore

        Gets the chronologically oldest position and removes
         it from the datastructure

        :return: The next position to explore
        """
        # TODO
        pass

    def clear(self):
        """clears the underlying datastructure by removing any
        elements and resetting any state information
        """
        # TODO
        pass

    def update(self, maze: Maze):
        """
        update any state information that is maze-dependent
        :param maze:
        :return:
        """
        # TODO
        pass

    def __len__(self):
        """The number of positions currently held by the datastructure
        """
        # TODO
        pass


class BestFirstStorage(PositionStorage):
    """ Datastructure for storing maze positions

    Best-First storage. The get_position() method is guaranteed
    to return a position that is closest to the end of the maze.
    """

    def __init__(self):
        super().__init__("best first")
        # TODO
        pass

    def add_position(self, pos: Tuple[int, int]):
        """
        Adds the position pos to the datastructure
        :param pos: The position to add
        """
        # TODO
        pass

    def get_next_position(self) -> Tuple[int, int]:
        """Gets the next position to explore

        Gets the position closest to the end of the maze
        and removes it from the datastructure

        :return: The next position to explore
        """
        # TODO
        pass

    def clear(self):
        """clears the underlying datastructure by removing any elements and
        resetting any state information
        """
        # TODO
        pass

    def update(self, maze: Maze):
        """
        update any state information that is maze-dependent
        :param maze:
        :return:
        """
        # TODO
        pass

    def __len__(self):
        """The number of positions currently held by the datastructure
        """
        # TODO
        pass
