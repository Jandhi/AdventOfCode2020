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
    return word.count(letter)

def is_valid(min_count, max_count, letter, password) -> bool:
    count = count_letter(letter, password)
    return min_count <= count <= max_count


def count_valid_passwords(input) -> int:
    count = 0 
    for entry in input:
        min_count, max_count, letter, password = entry
        if is_valid(min_count, max_count, letter, password):
            count += 1
    return count

def is_valid_two(pos1, pos2, letter, password):
    count = 0
    pos1_has_letter = password[pos1 - 1] == letter
    pos2_has_letter = password[pos2 - 1] == letter
    if pos1_has_letter:
        count += 1
    if pos2_has_letter:
        count += 1
    if count == 1:
        return True
    else:
        return False

def count_valid_passwords_two(input) -> int:
    count = 0 
    for entry in input:
        min_count, max_count, letter, password = entry
        if is_valid_two(min_count, max_count, letter, password):
            count += 1
    return count

print(
    count_valid_passwords(input),
    count_valid_passwords_two(input)

)