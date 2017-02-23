CHAIN_LENGTH = 4
grid = []

with open("grid.txt") as f:
    for line in f:
        grid.append([int(i) for i in line.strip().split(" ")])


def grid_val(x, y):
    if (x >= 20 or x < 0 or y >= 20 or y < 0):
        return 0
    return grid[y][x]


def left(x, y):
    res = 1
    for i in range(CHAIN_LENGTH):
        res *= grid_val(x, y)
        x += 1
    return res


def down(x, y):
    res = 1
    for i in range(CHAIN_LENGTH):
        res *= grid_val(x, y)
        y += 1
    return res


def right_diag(x, y):
    res = 1
    for i in range(CHAIN_LENGTH):
        res *= grid_val(x, y)
        y += 1
        x += 1
    return res


def left_diag(x, y):
    res = 1
    for i in range(CHAIN_LENGTH):
        res *= grid_val(x, y)
        y += 1
        x -= 1
    return res


i = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        prod = max([
            left(col, row),
            down(col, row),
            left_diag(col, row),
            right_diag(col, row)
        ])
        i = max(i, prod)


print "Answer:", i
