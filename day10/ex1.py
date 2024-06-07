import statistics
from collections import deque


# def has_neighbors(pos):
#     neighbors =

# def find_loop():
#     pass


pipe_directions = {(-1,  0): ['-', 'F', 'L'],
                   ( 1,  0): ['-', '7', 'J'],
                   ( 0, -1): ['|', '7', 'F'],
                   ( 0,  1): ['|', 'L', 'J']}

# # -1 == left, 1 == right
# pipes_x = {-1: ['-', 'F', 'L'],
#             1: ['-', '7', 'J']}
# # -1 == up, 1 == down
# pipes_y = {-1: ['|', '7', 'F'],
#             1: ['|', 'L', 'J']}

def next_pipe(tile, direction):

    straights = ['-', '|']
    if tile in straights:
        return direction

    bends = {'F': ( 1, -1), 'L': (1,  1),
             'J': (-1,  1), '7': (1, -1)}
    return bends[tile]


with open('test.txt', 'r') as f:
    mat = [list(l.strip()) for l in f.readlines()]
    for y, row in enumerate(mat):
        if 'S' in row:
            x = row.index('S')
            start = (x, y)

# lrud: left right up down
lrud = [(-1, 0), (1, 0), (0, -1), (0, 1)]
loop_closed = False
# coords = [start]
# seen = set()
# previous_coords = [start]
steps = 0
previous_coord = tuple()
coord = start

while not loop_closed:
    steps += 1

    # if steps == 20:
    #     break

    cur_x, cur_y = coord

    print()
    print('Previous coord:', previous_coord)
    print('Coord:', coord)

    for lr, ud in lrud:

        x, y     = cur_x + lr, cur_y + ud
        neighbor = (x, y)
        tile     = mat[y][x]

        if not (0 <= x < len(mat[0]) and 0 <= y < len(mat)):
            continue

        if neighbor == previous_coord:
            continue

        if tile == 'S':
            loop_closed = True
            break

        if tile not in pipe_directions[(lr, ud)]:
            continue

        print('\tNeighbor:', neighbor)
        previous_coord = coord
        direction = (lr, ud)
        next_direction = next_pipe(tile, direction)
        coord = tuple(map(sum, zip(coord, next_direction)))

        # if lr:
        #     if tile in pipes_x[lr]:
        #         previous_coord = coord
        #         coord = neighbor
        # if ud:
        #     if tile in pipes_y[ud]:
        #         previous_coord = coord
        #         coord = neighbor

    # # filter out-of-bound neighbors
    # neighbors = [(x, y) for x, y in neighbors if 0 <= x < len(mat[0]) and 0 <= y < len(mat)]
    # # filter backtracking neighbors
    # neighbors = [n for n in neighbors if n != previous_coord]

    # # get directions associated with neighbors
    # directions = [(lr, ud) for lr, ud in lrud if (cur_x+lr, cur_y+ud) in neighbors]
    # # get actual tiles
    # tiles = [mat[y][x] for x, y in neighbors]



# while not loop_closed:

#     steps += 1
#     print('Coords:', coords)
#     for cur_x, cur_y in coords:

#         coords_to_add = []
#         new_coords = [(cur_x+lr, cur_y+ud) for lr, ud in lrud]
#         # new_coords = [nc for nc in new_coords if nc not in previous_coords]
#         print('New coords:', new_coords)
#         if any(nc == start for nc in new_coords):
#             print('Loop closed!')
#             loop_closed = True
#             break

#         new_coords = [nc for nc in new_coords if nc not in seen]
#         new_coords = [(x, y) for x, y in new_coords if 0 <= x < len(mat[0]) and 0 <= y < len(mat)]
#         print('Filtered new coords:', new_coords)
#         directions = [(lr, ud) for lr, ud in lrud if (cur_x+lr, cur_y+ud) in new_coords]
#         print('Directions:', directions)
#         # tiles = {(x, y): mat[y][x] for x, y in new_coords}
#         tiles = [mat[y][x] for x, y in new_coords]
#         print('Tiles:', tiles, '\n')
#         for (x, y), (dx, dy), tile in zip(new_coords, directions, tiles):
#             if dx in pipes_x:
#                 if tile in pipes_x[dx]:
#                     coords_to_add.append((x, y))
#             if dy in pipes_y:
#                 if tile in pipes_y[dy]:
#                     coords_to_add.append((x, y))
#             # if tile in pipes_x[dx] or tile in pipes_y[dy]:
#             #     coords_to_add.append((x, y))

#     coords = coords_to_add[:]
#     seen.update(coords_to_add)

#     if steps == 20:
#         print(seen)
#         break

print(steps)
print(statistics.median(list(range(1, steps+1))))