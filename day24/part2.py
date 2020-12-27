import copy
from collections import Counter
from math import sqrt
from typing import List, Tuple, Any
import numpy as np
from tqdm import tqdm

poss_dirs = ['e', 'w', 'ne', 'nw', 'se', 'sw']
e_vec = np.array([1, -1, 0])
ne_vec = np.array([1, 0, -1])
se_vec = np.array([0, -1, 1])
neighbour_vec = [e_vec, -e_vec, ne_vec, -ne_vec, se_vec, -se_vec]


def parse_instr(tile_str: str) -> List[str]:
    i = 0
    instr_list = []
    instr = None
    while i < len(tile_str):
        char = tile_str[i]
        if char == 's':
            instr = tile_str[i:i + 2]
            i += 2
        elif char == 'n':
            instr = tile_str[i:i + 2]
            i += 2
        elif char == 'e':
            instr = char
            i += 1
        elif char == 'w':
            instr = char
            i += 1
        instr_list.append(instr)
    return instr_list


def count_dirs(dir_str: str) -> Counter:
    instr_list = parse_instr(dir_str)
    cnt = Counter(instr_list)
    for direction in poss_dirs:
        if direction not in cnt:
            cnt[direction] = 0
    return cnt


def reduce_dirs(dir_cnt: Counter) -> Tuple[Any]:
    e = dir_cnt['e'] - dir_cnt['w']
    ne = dir_cnt['ne'] - dir_cnt['sw']
    se = dir_cnt['se'] - dir_cnt['nw']

    return e * e_vec + ne * ne_vec + se * se_vec


def pad_grid(grid: np.array) -> np.array:
    new_grid = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2, grid.shape[2] + 2), dtype=int)
    new_grid[1:-1, 1:-1, 1:-1] = grid
    return new_grid

def need_padding(grid: np.array) -> bool:
    if np.sum(grid[:, :, 0]) + np.sum(grid[:, :, -1]) + np.sum(grid[:, 0, :]) +np.sum(grid[:, -1, :]) +np.sum(grid[0, :, :])+np.sum(grid[-1, :, :]) == 0:
        return False
    return True





if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
    flipped = {}
    tiles = []
    for i, line in enumerate(lines):
        cnt = count_dirs(line)
        coor = reduce_dirs(cnt)
        coor_str = str(coor)

        if coor_str in flipped:
            val = flipped[coor_str]
            if val:
                flipped[coor_str] = False
            else:
                flipped[coor_str] = True
        else:
            flipped[coor_str] = True
            tiles.append(coor)

    cnt = Counter()
    max_tile = None
    max_len = 0
    for tile in flipped.values():
        cnt[tile] += 1

    max_el = 0
    for tile in tiles:
        if max(tile) > max_el:
            max_el = max(tile)

    r = 2 * max_el + 1
    grid = np.zeros((r + 2, r + 2, r + 2), dtype=int)

    for tile in tiles:
        if flipped[str(tile)]:
            coor_offset = tile + np.array([max_el + 1, max_el + 1, max_el + 1])

            grid[coor_offset[0], coor_offset[1], coor_offset[2]] = 1

    print(np.sum(grid))
    for t in tqdm(range(100)):
        grid_copy = copy.deepcopy(grid)
        dim = grid.shape[0]
        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    el = grid[i, j, k]
                    blk_count = 0
                    for vec in neighbour_vec:
                        new_coor = np.array([i, j, k]) + vec
                        try:
                            blk_count += grid[new_coor[0], new_coor[1], new_coor[2]]
                        except IndexError:
                            pass
                    if el == 1:
                        if blk_count == 0 or blk_count > 2:
                            grid_copy[i, j, k] = 0
                    else:
                        if blk_count == 2:
                            grid_copy[i, j, k] = 1
        grid = grid_copy
        if need_padding(grid):
            grid = pad_grid(grid)


    print(np.sum(grid))







