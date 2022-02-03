
fields = ['eyr', 'byr', 'iyr', 'hgt', 'hcl', 'ecl', 'pid']

has_field = {}

for field in fields:
    has_field[field] = False


valid_pass_count = 0  
with open("day 4/input.txt", "r") as file:     
    line = file.readline()      
    while line:         
        if line == "\n":             
            if all(has_field.values()):                 
                valid_pass_count += 1             
                for field in fields:
                    has_field[field] = False
        else:             
            parts = line.split()             
            for part in parts:                 
                for field in fields:
                    if part.startswith(field):
                        has_field[field] = True
        
        line = file.readline()
print(valid_pass_count)