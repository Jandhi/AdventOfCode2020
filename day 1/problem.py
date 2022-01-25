numbers = []

with open('input.txt', 'r') as file:
    line = file.readline()

    while line:
        numbers.append(int(line))

        line = file.readline()

for number in numbers:
    for other in numbers:
        if 2020 == number + other:
            print(number * other)