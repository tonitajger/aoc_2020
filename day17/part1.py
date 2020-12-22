from typing import List, Any, Tuple, Iterable
from collections import Counter
import copy

def pad_object(obj: List[Any], el: Any) -> None:
    obj.insert(0, el)
    obj.append(copy.deepcopy(el))


def pad_grid(grid: List[List[List]]) -> None:
    dim_x = len(grid[0][0])
    dim_y = len(grid[0])
    for layer in grid:
        for i in range(len(layer)):
            pad_object(layer[i], '.')
        pad_object(layer, ['.' for l in range(dim_x + 2)])

    dim_x += 2
    dim_y += 2

    zero_layer = [['.' for _l in range(dim_x)] for _j in range(dim_y)]
    pad_object(grid, zero_layer)


def get_neighbour_coor(coor: Tuple[int], grid: List[List[List]]) -> List[List[int]]:
    dim_k = len(grid[0][0])
    dim_j = len(grid[0])
    dim_i = len(grid)

    i = coor[0]
    ii = list(range(max(0, i-1), min(dim_i, i+2)))
    j = coor[1]
    jj = list(range(max(0, j-1), min(dim_j, j+2)))
    k = coor[2]
    kk = list(range(max(0, k-1), min(dim_k, k+2)))
    neighbour_coor = [ii, jj, kk]
    # for i in ii:
    #     for j in jj:
    #         for k in kk:
    #             if (i, j, k) != coor:
    #                 neighbour_coor.append((i, j, k))
    return neighbour_coor


def count_neighbours(coor: Tuple[int], grid: List[List[List]]) -> Counter:
    cnt = Counter()
    ranges = get_neighbour_coor(coor, grid)
    subgrid_z = grid[ranges[0][0]:ranges[0][-1] + 1]
    subgrid_y = [col[ranges[1][0]:ranges[1][-1] + 1] for col in subgrid_z]

    subgrid = [[row[ranges[2][0]:ranges[2][-1] + 1] for row in col] for col in subgrid_y]

    for i, layer in enumerate(subgrid):
        for j, row in enumerate(layer):
            for k, char in enumerate(row):
                cnt[char] += 1
    if grid[coor[0]][coor[1]][coor[2]] == '#':
        cnt['#'] -= 1
    return cnt



with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

grid_init = [[[char for char in line] for line in lines]]
grid = grid_init


for cycle in range(6):
    pad_grid(grid)
    new_grid = copy.deepcopy(grid)
    active_count = 0
    for i, layer in enumerate(grid):
        for j, col in enumerate(layer):
            for k, char in enumerate(col):
                if i == 1 and j == 1 and k == 2:
                    print('sdsa')
                    pass
                actives = count_neighbours((i, j, k), grid)['#']

                if char == '.':
                    if actives == 3:
                        new_grid[i][j][k] = '#'
                        active_count += 1
                elif char == '#':
                    if 2 <= actives <= 3:
                        active_count += 1
                    else:
                        new_grid[i][j][k] = '.'
    grid = new_grid
print(active_count)
print(grid)






pad_grid(grid_init)



