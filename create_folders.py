from os import mkdir

for i in range(25):
    try:
        mkdir(f"day {i + 1}")
    except e:
        pass