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

height = len(grid)
width = len(grid[0])

# returns whether there is a tree at position x, y
def has_tree(x : int, y : int) -> bool:
    return grid[y][x]

count = 0
x = 0
y = 0

while y < height:
    if has_tree(x, y):
        count += 1
    
    #     #..
    #     ..#
    #     ...

    x += 3
    y += 1