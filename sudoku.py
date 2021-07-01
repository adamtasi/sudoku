import random
import string
import time

size = int(input("Give the grid size. The smallest available size is 2 (4), the biggest is 5 (25): "))

def generate_caracter_set(size):
    #Generate the dynamic character set
    character_set = []
    if size in (2,3):
        for numb in range(size*size): character_set.append(numb + 1)
    elif size == 4:
        for numb in range(9): character_set.append(numb + 1)
        num2letter = dict(zip(range(9, 16), string.ascii_uppercase))
        for numb in range(9, 16): character_set.append(num2letter[numb])
    elif size == 5:
        num2letter = dict(zip(range(1, 27), string.ascii_uppercase))
        for numb in range(25): character_set.append(num2letter[numb + 1])
    else:
        raise ValueError("The given size is not available!")
    seconds = str(int(round(time.time())))
    return character_set if (int(seconds[-1]) % 2) == 0 else character_set[::-1]

def dynamic_grid(size):
    #Generate dynamic grid between 2x2 and 5x5 size
    grid = []
    c_set = generate_caracter_set(size)
    for i in range(int(size*size)):
        grid.append(c_set)
        c_set = c_set[(size*size)-size:size*size] + c_set[0:(size*size)-size]
    return grid

def shuffle_puzzle():
    new_grid = []
    full_size = size * size
    opposite_unit = size-1
    grid = dynamic_grid(size)

    for index, row in enumerate(grid):
        new_grid.append(row[(full_size)-size:full_size] + row[0:(full_size)-size])
        if (index % size) == opposite_unit:
            if size*size-1 < full_size:
                full_size += 1
    for col in new_grid:
        for i, r in enumerate(col):
            if (i % size) == opposite_unit:
                if col[i] != col[-1]:
                    col[i-opposite_unit], col[i] = col[i], col[i-opposite_unit]
    for i, row in enumerate(new_grid):
        if (i % size) == opposite_unit:
            if row[i] != row[-1]:
                new_grid[i-opposite_unit], new_grid[i] = new_grid[i], new_grid[i-opposite_unit]
    for asd in range(0, size**size):
        a_elem, b_elem = random.choice(new_grid[0]), random.choice(new_grid[0])
        for elem in new_grid:
            for i in range(0, size*size):
                if elem[i] == a_elem:
                    elem[i] = b_elem
                elif elem[i] == b_elem:
                    elem[i] = a_elem

    for i in new_grid:
        print(i)

shuffle_puzzle()








#   1   2   3
# #123 456 789
#   2   3   1
# #456 789 123
#   3   1   2
# #789 123 456
#   1   2   3
# #234 567 891 - elso es utolso szam eltolva
#   2   3   1
# #567 891 234
#   3   2   1
# #891 234 567
#   1   2   3
# #345 678 912 - elso es utolso szam eltolva
#   2   3   1
# #678 912 345
#   3   1   2
# #912 345 678
