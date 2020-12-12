import copy
from collections import Counter

def flatten(t):
    return [item for sublist in t for item in sublist]


def getsubgrid(x1, y1, x2, y2, grid):
    sub = [item[x1:x2] for item in grid[y1:y2]]
    return sub


def get_counts(i, j, grid):
    cnt = Counter()
    if j < len(grid[i]):
        for k in range(j + 1, len(grid[i])):
            seat = grid[i][k]
            if seat != '.':
                cnt[seat] += 1
                break

    if j > 0:
        for k in range(j - 1, -1, -1):
            seat = grid[i][k]
            if seat != '.':
                cnt[seat] += 1
                break

    if i < len(grid):
        for k in range(i + 1, len(grid)):
            seat = grid[k][j]
            if seat != '.':
                cnt[seat] += 1
                break

    if i > 0:
        for k in range(i - 1, -1, -1):
            seat = grid[k][j]
            if seat != '.':
                cnt[seat] += 1
                break

    if i < len(grid) and j < len(grid[i]):
        for k in range(1, min([len(grid) - i, len(grid[i]) - j] )):
            seat = grid[i+k][j+k]
            if seat != '.':
                cnt[seat] += 1
                break

    if i < len(grid) and j > 0:
        for k in range(1, min([len(grid) - i, j + 1])):
            seat = grid[i+k][j-k]
            if seat != '.':
                cnt[seat] += 1
                break

    if j < len(grid[i]) and i > 0:
        for k in range(1, min([len(grid[i]) - j, i + 1])):
            seat = grid[i-k][j+k]
            if seat != '.':
                cnt[seat] += 1
                break

    if j > 0 and i > 0:
        for k in range(1, min([j + 1, i + 1])):
            seat = grid[i-k][j-k]
            if seat != '.':
                cnt[seat] += 1
                break
    return(cnt)







with open('input.txt', 'r') as f:
    rows = f.read().splitlines()

grid = [[char for char in row] for row in rows]
print(get_counts(3,3,grid))

has_changed = True
while has_changed:
    new = copy.deepcopy(grid)
    has_changed = False
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'L':


                cnt = get_counts(i,j,grid)
                if not cnt['#']:
                    new[i][j] = '#'
                    has_changed = True

            elif char == '#':


                cnt = get_counts(i,j,grid)

                if cnt['#'] >= 5:
                    new[i][j] = 'L'
                    has_changed = True
    grid = new

occ_count = 0
for el in flatten(grid):
    if el == '#':
        occ_count += 1
print(occ_count)
