
def traverse(r, d):
    with open('input.txt', 'r') as f:
        grid = f.read().splitlines()
    coor = [0, 0]
    width = len(grid[0])
    height = len(grid)
    with open('input.txt', 'r') as f:
        grid = f.read().splitlines()

    tree_sum = 0
    while coor[1] < height:
        if grid[coor[1]][coor[0]] == '#':
            tree_sum += 1
        coor[1] += d
        coor[0] = (coor[0] + r) % width
    return tree_sum


def main():
    with open('slopes.txt', 'r') as f:
        slopes_str = f.read().splitlines()

    product = 1
    for line in slopes_str:
        r = int(line.split()[1][0])
        d = int(line.split()[3][0])
        product *= traverse(r, d)
    print(product)


if __name__ == '__main__':
    main()
