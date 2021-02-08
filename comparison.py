from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

from algorithm import MazeSearch
from datastructures import BestFirstStorage, BreadthFirstStorage, DepthFirstStorage
from utils import RandomMaze as Maze

"""
Plots metrics of the search procedure for each storage type.

Test each datastructure on (the same) k nxn mazes
for n = 50,100,150,200,250
"""
#TODO
"""
For each storage datastructure and each plot,
compare and give rationale for the observed behavior.
(i.e.)
(1) The average length of a solution path
(2) The average time taken to solve the mazes
(3) The average number of visited vertices
(4) The average number of discovered vertices
"""
ns = [50, 100, 150, 200, 250]
k = 6
storages = [BestFirstStorage(), BreadthFirstStorage(), DepthFirstStorage()]
all_data = defaultdict(lambda: defaultdict(list))

for n in ns:
    solver_data = defaultdict(lambda: defaultdict(list))
    for _ in range(k):
        maze = Maze(n, n)
        # solve the maze with each method and record the statistics
        for storage in storages:
            solver = MazeSearch(storage)
            assert solver.search(maze)
            solver_data[str(storage)]['time'] = solver.search_time()
            solver_data[str(storage)]['num visited'] = solver.num_explored()
            solver_data[str(storage)]['num discovered'] = solver.num_discovered()
            solver_data[str(storage)]['solution path length'] = len(solver.solution_path())
    # aggregate and average the data
    for storage_type in solver_data:
        for key in solver_data[storage_type]:
            storage_data = solver_data[storage_type][key]
            all_data[key][storage_type].append(np.mean(storage_data))

#Save each of the plots in ./plots
for key in all_data:
    fig = plt.figure()
    plt.title(key)
    for storage_type, color in zip(all_data[key], ['r', 'g', 'b']):
        plot_data = all_data[key][storage_type]
        plt.plot(ns, plot_data, color, label=storage_type)
        plt.xlabel('n')
        plt.ylabel(key)
    plt.legend()
    fig.savefig(f"./plots/{key}.png")

