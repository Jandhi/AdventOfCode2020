grid : list[str] = []

with open('day 3/input.txt', 'r') as file:
    line = file.readline()

    while line:
        grid.append(line)
        line = file.readline()

height = len(grid)
width = len(grid[0])

count = 0
y = 0

for row in grid:
    x = (3 * y) % width

    if grid[y][x] == '#':
        count += 1

    y += 1

print(count)