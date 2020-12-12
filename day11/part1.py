import copy

def flatten(t):
    return [item for sublist in t for item in sublist]
def getsubgrid(x1, y1, x2, y2, grid):
    sub = [item[x1:x2] for item in grid[y1:y2]]
    return sub

with open('input.txt', 'r') as f:
    rows = f.read().splitlines()

grid = [[char for char in row] for row in rows]


has_changed = True
while has_changed:
    new = copy.deepcopy(grid)
    has_changed = False
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'L':
                lo_row = i-1
                hi_row = i+1
                lo_col = j-1
                hi_col = j+1
                if lo_row < 0:
                    lo_row = 0
                if lo_col < 0:
                    lo_col = 0
                if hi_row >= len(grid) - 1:
                    hi_row = len(grid) - 1
                if hi_col >= len(row) - 1:
                    hi_col = len(row) - 1

                neighbours = flatten(getsubgrid(lo_col,lo_row,hi_col+1,hi_row+1,grid))
                is_all_empty = True
                for n in neighbours:
                    if n == '#':
                        is_all_empty = False
                        break
                if is_all_empty:
                    new[i][j] = '#'
                    has_changed = True

            elif char == '#':
                lo_row = i - 1
                hi_row = i + 1
                lo_col = j - 1
                hi_col = j + 1
                if lo_row < 0:
                    lo_row = 0
                if lo_col < 0:
                    lo_col = 0
                if hi_row >= len(grid) - 1:
                    hi_row = len(grid) - 1
                if hi_col >= len(row) - 1:
                    hi_col = len(row) - 1


                neighbours = flatten(getsubgrid(lo_col,lo_row,hi_col+1,hi_row+1,grid))
                occ_count = -1
                for n in neighbours:
                    if n == '#':
                        occ_count += 1
                if occ_count >= 4:
                    new[i][j] = 'L'
                    has_changed = True
    grid = new

occ_count = 0
for el in flatten(grid):
    if el == '#':
        occ_count += 1
print(occ_count)
