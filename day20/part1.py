from __future__ import annotations
import numpy as np
from typing import Dict
import tqdm

class Tile(object):
    id: int
    grid: np.ndarray

    tested_tiles = set()
    rot = None
    flipped = (False, False)

    def __init__(self, tile_id: int, grid: np.ndarray) -> None:
        self.tile_id = tile_id
        self.grid = np.array([[char for char in line] for line in grid.splitlines()[1:]])
        self.neighbours = [None, None, None, None]

    def pair(self, other_tile: Tile) -> bool:
        self.tested_tiles.add(other_tile.tile_id)
        if self._pair_rot(other_tile):
            return True
        elif self._pair_rot(other_tile, flipped=True):
            return True
        elif self._pair_rot(other_tile, flipped=True, own_flipped=True):
            return True
        elif self._pair_rot(other_tile, own_flipped=True):
            return True
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
                    if self.tile_id == 1951:
                        pass
                    self.neighbours[j] = other_tile
                    other_tile.grid = np.flip(np.rot90(s, k=i), axis=0)
                    return True
        return False

    def __eq__(self, other):
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
    tile_dict = create_tiles('input.txt')
    tiles = list(tile_dict.values())
    tiles_queue = list(tile_dict.values())

    for t1 in tqdm.tqdm(tiles):
        for t2 in tiles:
            if t1 != t2:

                t1.pair(t2)

    prod = 1
    for t in tile_dict.values():
        if sum(x is not None for x in t.neighbours) == 2:
            prod *= t.tile_id
    print(prod)
