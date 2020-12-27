from typing import Dict, List


def get_opposite_direction(direction: str) -> str:
    if direction == 'se':
        return 'nw'
    elif direction == 'sw':
        return 'ne'
    elif direction == 'nw':
        return 'se'
    elif direction == 'ne':
        return 'sw'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'


def parse_line(tile_str: str) -> List[str]:
    i = 0
    instrs = []
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
        instrs.append(instr)
    return instrs


class Tile:
    def __init__(self, tile_id: int) -> None:
        self.tile_id = tile_id
        self.flipped = False
        self.neighbours: Dict[str, Tile] = {'w': None, 'e': None, 'sw': None, 'se': None, 'nw': None, 'ne': None}


class TileGrid:
    def __init__(self) -> None:
        self.ref_tile = Tile(0)
        self.tiles = {0: self.ref_tile}
        self.curr = self.ref_tile
        self.next_id = 1

    def populate_grid(self, radius: int):


    def exec_instr(self, instr: str) -> None:
        instr_list = parse_line(instr)
        for instr in instr_list:
            self._go(instr)
        self._flip()
        self.curr = self.ref_tile

    def num_flipped(self) -> int:
        count = 0
        for tile in self.tiles.values():
            if tile.flipped:
                count += 1
        return count

    def _flip(self) -> None:
        if self.curr.flipped:
            print(f'{self.curr.tile_id} flipped to False')
            self.curr.flipped = False
        else:
            print(f'{self.curr.tile_id} flipped to True')
            self.curr.flipped = True

    def _go(self, direction: str) -> None:
        new_tile = self.curr.neighbours[direction]
        self.curr = new_tile


if __name__ == '__main__':
    with open('mock2.txt', 'r') as f:
        lines = f.read().splitlines()
    tg = TileGrid()
    for line in lines:
        tg.exec_instr(line)
    print(tg.num_flipped())