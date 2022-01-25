input = []

with open('day 2/input.txt', 'r') as file:
    line = file.readline()

    while line:
        parts = line.split()
        range = parts[0].split('-')
        min_count = int(range[0])
        max_count = int(range[1])
        letter = parts[1][0]
        password = parts[2]
        
        input.append( (min_count, max_count, letter, password) )

        line = file.readline()

def count_letter(letter, word) -> int:
    pass

def is_valid(min_count, max_count, letter, password) -> bool:
    pass

def count_valid_passwords(input) -> int:
    pass

print(
    count_valid_passwords(input)
)