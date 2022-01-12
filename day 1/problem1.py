numbers = []

with open('input.txt', 'r') as file:
    line = file.readline()

    while line:
        numbers.append(int(line))

        line = file.readline()



for i in [0, 1, 2]:
    print(i)