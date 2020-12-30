from __future__ import annotations

import copy

import numpy as np
from typing import Dict
import tqdm
import pickle as pkl


class Tile(object):



    def __init__(self, tile_id: int, grid: np.ndarray) -> None:
        self.tile_id = tile_id
        self.grid = np.array([[char for char in line] for line in grid.splitlines()[1:]])
        self.neighbours = [None, None, None, None]
        self.flipped = []
        self.rot = []

    def pair(self, other_tile: Tile) -> bool:
        # self.tested_tiles.add(other_tile.tile_id)
        if self._pair_rot(other_tile):
            return True
        elif self._pair_rot(other_tile, flipped=True):
            return True
        # elif self._pair_rot(other_tile, flipped=True, own_flipped=True):
        #     return True
        # elif self._pair_rot(other_tile, own_flipped=True):
        #     return True
        return False

    def _pair_rot(self, other_tile: Tile, flipped: bool = False, own_flipped: bool = False) -> bool:
        for j in range(4):
            if own_flipped:
                f = np.flip(np.rot90(self.grid, k=j), axis=1)
            else:
                f = np.rot90(self.grid, k=j)

            if flipped:
                s = np.flip(other_tile.grid, axis=1)
            else:
                s = other_tile.grid
            for i in range(4):
                if np.array_equal(np.rot90(s, k=i)[0][:], f[0][:]):
                    if other_tile not in self.neighbours:
                        other_tile.flipped.append(flipped)
                        if flipped:
                            self.neighbours[j] = other_tile
                            other_tile.neighbours[(i + j) % 4] = self
                            other_tile.grid = np.rot90(s, k=i + j)
                            other_tile.rot.append(i + j)
                        else:
                            self.neighbours[j] = other_tile
                            other_tile.neighbours[(-i - j) % 4] = self
                            other_tile.grid = np.flip(np.rot90(s, k=i + j), axis=0)
                            other_tile.rot.append(i + j)

                        return True
                    else:
                        return False
        return False

    def __eq__(self, other):
        if other is None:
            return False
        return self.tile_id == other.tile_id


def create_tiles(inp_file: str) -> Dict[int, Tile]:
    with open(inp_file, 'r') as f:
        lines = f.read().split('\n\n')

    tile_dict = {}
    for line in lines:
        if line != '':
            tile_id, grid = line.split(':')
            tile_id = int(tile_id.split()[-1])
            tile = Tile(tile_id, grid)
            tile_dict[tile_id] = tile

    return tile_dict


if __name__ == '__main__':
    try:
        with open('tiles.pkl', 'rb') as f:
            tile_dict = pkl.load(f)
    except FileNotFoundError:
        pass
    tile_dict = create_tiles('mock.txt')
    tiles = list(tile_dict.values())
    tiles_queue = list(tile_dict.values())

    in_grid = {tiles[0].tile_id: tiles[0]}
    tiles_queue.pop(0)
    while tiles_queue:
        for tile in list(in_grid.values()):
            tmp = tiles_queue.pop(0)
            succeeded = tile.pair(tmp)
            if succeeded:

                print(tile.tile_id, tmp.tile_id)
                in_grid[tmp.tile_id] = tmp
            else:
                tiles_queue.append(tmp)

    changed = True
    while changed:
        changed = False
        for tile in tiles:
            for other in tiles:
                if tile.tile_id != other.tile_id:
                    succeeded = tile.pair(other)
                    if succeeded:
                        print(tile.tile_id, other.tile_id)
                        changed = True

    with open('tiles_mock.pkl', 'wb') as f:
        pkl.dump(tile_dict, f)

    print(tile_dict)
    prod = 1
    # for k, t in tile_dict.items():
    #     for i, flip in enumerate(t.flipped):
    #         if flip:
    #             t.rot[i] *= - 1
    #     offset = sum(t.rot) % 4
    #     t.neighbours = t.neighbours[offset:] + t.neighbours[:offset]
    #     if sum([1 for el in t.flipped if el]) % 2:
    #         tmp = copy.deepcopy(t.neighbours)
    #         t.neighbours[1] = tmp[3]
    #         t.neighbours[3] = tmp[1]


    print(tile_dict[1951].neighbours)
    print(tile_dict[1951].flipped)
    print(tile_dict[1951].rot)
    print(tile_dict[3079].neighbours)
    print(tile_dict[3079].flipped)
    print(tile_dict[3079].rot)

    print(tile_dict[2971].neighbours)
    print(tile_dict[2971].flipped)
    print(tile_dict[2971].rot)
    print(tile_dict[1171].neighbours)
    print(tile_dict[1171].flipped)
    print(tile_dict[1171].rot)

    # print(tile_dict[3557].neighbours)
    # print(tile_dict[3769].neighbours)
    # print(tile_dict[1019].neighbours)
    # print(tile_dict[1097].neighbours)
