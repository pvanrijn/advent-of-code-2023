


def next_coord(coord, previous_coord, mat):

    directions = {
        'S': {(-1,  0): ['-', 'L', 'F', 'S'],
              ( 1,  0): ['-', '7', 'J', 'S'],
              ( 0, -1): ['|', 'F', '7', 'S'],
              ( 0,  1): ['|', 'L', 'J', 'S']},
        '-': {(-1,  0): ['-', 'L', 'F', 'S'],
              ( 1,  0): ['-', '7', 'J', 'S']},
        '|': {( 0, -1): ['|', 'F', '7', 'S'],
              ( 0,  1): ['|', 'L', 'J', 'S']},
        'L': {( 1,  0): ['-', 'J', '7', 'S'],
              ( 0, -1): ['|', 'F', '7', 'S']},
        'F': {( 1,  0): ['-', 'J', '7', 'S'],
              ( 0,  1): ['|', 'J', 'L', 'S']},
        'J': {(-1,  0): ['-', 'F', 'L', 'S'],
              ( 0, -1): ['|', 'F', '7', 'S']},
        '7': {(-1,  0): ['-', 'L', 'F', 'S'],
              ( 0,  1): ['|', 'J', 'L', 'S']},
    }

    neighbors = [(-1,  0), ( 1,  0), ( 0, -1), ( 0,  1)]

    x, y = coord
    tile = mat[y][x]

    for direction in neighbors:

        lr, ud = direction
        new_coord = (x+lr, y+ud)
        nx, ny = new_coord

        if new_coord == previous_coord:
            continue

        if not (0 <= nx < len(mat[0]) and 0 <= ny < len(mat)):
            continue

        new_tile = mat[ny][nx]

        if direction in directions[tile]:
            if new_tile in directions[tile][direction]:
                return new_coord

    return tuple()


def shoelace(coords):
    A = 0
    coords_len = len(coords) - 1
    for i in range(coords_len + 1):
        if i == coords_len:
            c1, c2 = coords[i], coords[0]
        else:
            c1, c2 = coords[i], coords[i+1]
        A += abs(c1[0] * c2[1]) - abs(c1[1] * c2[0])
    return abs(A // 2)

with open('input.txt', 'r') as f:
    mat = [list(l.strip()) for l in f.readlines()]
    for y, row in enumerate(mat):
        if 'S' in row:
            x = row.index('S')
            start = (x, y)

coords = []
loop_closed = False
steps = 0
previous_coord = tuple()
coord = start

while not loop_closed:
    steps += 1
    new_coord = next_coord(coord, previous_coord, mat)

    if not new_coord:
        print('Dead end')
        break

    x, y = new_coord
    tile = mat[y][x]

    if tile == 'S':
        loop_closed = True
        break

    coords.append(coord)
    previous_coord = coord
    coord = new_coord

A = shoelace(coords)
b = steps
h = 0

print('A:', A)
print('b:', b)

i = A - (b // 2) - h + 1

print('i:', i)

# Too high: 590