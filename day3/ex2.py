import functools


def has_symbol_neighbor(coords, mat):

    # any character not in this list is a symbol neighbor
    not_symbols = ['1', '2', '3', '4', '5',
                   '6', '7', '8', '9', '0', '.']

    max_x = len(mat[0])
    max_y = len(mat)

    for x, y in coords:
        # all possible surrounding coords
        surrounding = [(x-1, y-1), (x-1, y-0), (x-1, y+1),
                       (x-0, y-1),             (x-0, y+1),
                       (x+1, y-1), (x+1, y+0), (x+1, y+1)]

        # remove out-of-bounds coordinates
        oob = lambda xy: 0 <= xy[0] < max_x and 0 <= xy[1] < max_y
        surrounding = list(filter(oob, surrounding))

        if any(mat[ny][nx] not in not_symbols for nx, ny in surrounding):
            return True

    return False


def gear_sum(x, y, mat, num_coords, coord_value):

    max_x = len(mat[0])
    max_y = len(mat)

    surrounding = [(x-1, y-1), (x-1, y-0), (x-1, y+1),
                   (x-0, y-1),             (x-0, y+1),
                   (x+1, y-1), (x+1, y+0), (x+1, y+1)]

    gear_nums = set()

    for coord in surrounding:
        if not 0 <= x < max_x and not 0 <= y < max_y:
            continue
        if coord in num_coords:
            gear_nums.add(num_coords[coord])

    if len(gear_nums) > 1:
        gear_nums = [coord_value[coord] for coord in gear_nums]
        return functools.reduce(lambda a, b: a * b, gear_nums)
    return 0


with open('input.txt', 'r') as f:
    matrix = [list(l.strip()) for l in f.readlines()]

numbers = ['1', '2', '3', '4', '5',
           '6', '7', '8', '9', '0']
numbers_dot = numbers + ['.']
number_coords = {}
value_coords = {}
gear_coords = []

for y, row in enumerate(matrix):

    number_found = False
    cur_number = ''
    cur_number_coord = []

    for x, char in enumerate(row):

        if char in numbers:
            cur_number += char
            cur_number_coord.append((x, y))
            number_found = True

        elif char == '*':
            gear_coords.append((x, y))

        if (char not in numbers or x+1 == len(row)) and number_found:

            # {(0, 1): ((0, 1), (1, 1), (2, 1))}
            cur_number_coord = tuple(cur_number_coord)
            for coord in cur_number_coord:
                number_coords[coord] = cur_number_coord

            # # store numbers with coordinates as keys: {((2, 1), (3, 1), (4, 1)): 987}
            value_coords[cur_number_coord] = int(cur_number)

            # reset
            cur_number = ''
            cur_number_coord = []
            number_found = False

total = 0
has_neighbor = []

for x, y in gear_coords:
    total += gear_sum(x, y, matrix, number_coords, value_coords)

print(total)