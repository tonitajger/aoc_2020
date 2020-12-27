from typing import List, Any, Tuple, Iterable
from collections import Counter
import copy
import numpy as np


def pad_grid(grid: np.array) -> np.array:
    new_grid = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2, grid.shape[2] + 2, grid.shape[3] + 2), dtype=int)
    new_grid[1:-1, 1:-1, 1:-1, 1:-1] = grid
    return new_grid


def needs_padding(grid: np.array) -> bool:

    if np.sum(
            [np.sum(grid[0, :, :, :]),
             np.sum(grid[-1, :, :, :]),
             np.sum(grid[:, 0, :, :]),
             np.sum(grid[:, -1, :, :]),
             np.sum(grid[:, :, 0, :]),
             np.sum(grid[:, :, -1, :]),
             np.sum(grid[:, :, :, 0]),
             np.sum(grid[:, :, :, -1])]):
        return True
    return False


def init_grid(input_file: str) -> np.array:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    for i in range(len(lines)):
        lines[i] = np.array(list(lines[i].replace('#', '1').replace('.', '0')), dtype=int)
    grid = np.array([[lines]])
    grid = pad_grid(grid)
    return grid


def cycle(grid: np.array) -> np.array:
    new_grid = np.zeros(grid.shape, dtype=int)
    for i, i_el in enumerate(grid):
        for j, j_el in enumerate(i_el):
            for k, k_el in enumerate(j_el):
                for l, l_el in enumerate(k_el):
                    i_min, i_max = max(i - 1, 0), min(i + 2, grid.shape[0])
                    j_min, j_max = max(j - 1, 0), min(j + 2, grid.shape[1])
                    k_min, k_max = max(k - 1, 0), min(k + 2, grid.shape[2])
                    l_min, l_max = max(l - 1, 0), min(l + 2, grid.shape[3])
                    cnt = Counter(list(np.ndarray.flatten(grid[i_min:i_max, j_min:j_max, k_min:k_max, l_min:l_max])))
                    if l_el:
                        active_cnt = cnt[1] - 1
                        if active_cnt in [2, 3]:
                            new_grid[i, j, k, l] = 1
                    else:
                        active_cnt = cnt[1]
                        if active_cnt == 3:
                            new_grid[i, j, k, l] = 1

    if needs_padding(new_grid):

        new_grid = pad_grid(new_grid)

    return new_grid


def main():
    grid = init_grid('input.txt')

    for i in range(6):
        grid = cycle(grid)
    print(np.sum(grid))




if __name__ == '__main__':
    main()
