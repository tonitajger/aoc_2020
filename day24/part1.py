from collections import Counter
from math import sqrt
from typing import List, Tuple, Any
import numpy as np


poss_dirs = ['e', 'w', 'ne', 'nw', 'se', 'sw']
e_vec = np.array([1, -1, 0])
ne_vec = np.array([1, 0, -1])
se_vec = np.array([0, -1, 1])


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

    # while ne * se > 0:
    #     if ne > 0 and se > 0:
    #         ne -= 1
    #         se -= 1
    #         e += 1
    #     elif ne < 0 and se < 0:
    #         ne += 1
    #         se += 1
    #         e -= 1
    return e * e_vec + ne * ne_vec + se * se_vec


if __name__ == '__main__':
    with open('mock.txt', 'r') as f:
        lines = f.read().splitlines()
    flipped = {}
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

    cnt = Counter()
    for tile in flipped.values():
        cnt[tile] += 1
    print(cnt)