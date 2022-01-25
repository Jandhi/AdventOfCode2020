grid : list[list[bool]] = []

with open('day 3/input.txt', 'r') as file:
    line = file.readline()

    while line:
        row = []

        for i in range(len(line)):
            letter = line[i]
            row.append(letter == '#')

        grid.append(row)

        line = file.readline()

def has_tree(x : int, y : int) -> bool:
    return grid[y][x]

def print_grid():
    for row in grid:
        output = ''
        for has_tree in row:
            if has_tree:
                output += '#'
            else:
                output += '.'
        print(output)

print_grid()