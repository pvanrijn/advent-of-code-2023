import re

def has_symbol_neighbor(coords, mat):

    # any character not in this list is a symbol neighbor
    not_symbols = ['1', '2', '3', '4', '5',
                   '6', '7', '8', '9', '0', '.']

    max_x = len(mat[0])
    max_y = len(mat)

    for x, y in coords:

        surrounding = [(x-1, y-1), (x-1, y-0), (x-1, y+1),
                       (x-0, y-1),             (x-0, y+1),
                       (x+1, y-1), (x+1, y+0), (x+1, y+1)]

        # remove out-of-bounds coordinates
        oob = lambda xy: 0 <= xy[0] < max_x and 0 <= xy[1] < max_y
        surrounding = list(filter(oob, surrounding))

        # surrounding_coords = [(nx, ny) for nx, ny in surrounding if nx < max_x]
        if any(mat[ny][nx] not in not_symbols for nx, ny in surrounding):
            return True

    return False

with open('input.txt', 'r') as f:
    matrix = [list(l.strip()) for l in f.readlines()]

numbers = ['1', '2', '3', '4', '5',
           '6', '7', '8', '9', '0']

numbers_dot = numbers + ['.']

number_coords = {}

for y, row in enumerate(matrix):

    number_found = False
    cur_number = ''
    cur_number_coord = []

    for x, char in enumerate(row):
        if char in numbers:
            cur_number += char
            cur_number_coord.append((x, y))
            number_found = True
        if (char not in numbers or x+1 == len(row)) and number_found:
            # store numbers with coordinates as keys: {((2, 1), (3, 1), (4, 1)): 987}
            cur_number_coord = tuple(cur_number_coord)
            number_coords[cur_number_coord] = int(cur_number)
            # reset
            cur_number = ''
            cur_number_coord = []
            number_found = False

total = 0
has_neighbor = []

# print(number_coords.values())

for number_coord, number in number_coords.items():
    if has_symbol_neighbor(number_coord, matrix):
        total += number
        has_neighbor.append(number)

# print(has_neighbor, '\n')
print(sum(has_neighbor), '\n')
print(total)