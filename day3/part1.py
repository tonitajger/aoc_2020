with open('input.txt', 'r') as f:
    grid = f.read().splitlines()

coor = [0, 0]
width = len(grid[0])
height = len(grid)

tree_sum = 0
while coor[1] < height:
    if grid[coor[1]][coor[0]] == '#':
        tree_sum += 1
    coor[1] += 1
    coor[0] = (coor[0] + 3) % width

print(tree_sum)
