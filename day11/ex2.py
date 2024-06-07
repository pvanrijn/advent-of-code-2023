from itertools import combinations

# def expand_matrix(mat, expansion=2):

#     # insert extra column if all characters in column are empty (.)
#     mat_newcols = []
#     for row in mat:
#         newrow = ''
#         for x, col in enumerate(row):
#             if all(r[x] == '.' for r in mat):
#                 newrow += col * expansion
#             else:
#                 newrow += col
#         mat_newcols.append(newrow)

#     # insert extra row if all characters in row are empty (.)
#     mat_newrows = []
#     for row in mat_newcols:
#         if all(c == '.' for c in row):
#             for _ in range(expansion):
#                 mat_newrows.append(row)
#         else:
#             mat_newrows.append(row)

#     return mat_newrows


def empty_rows_cols(mat):
    rows = []
    cols = []
    for y, row in enumerate(mat):
        if all(c == '.' for c in row):
            rows.append(y)
    for x, _ in enumerate(mat[0]):
        if all(r[x] == '.' for r in mat):
            cols.append(x)
    return rows, cols


def route_length(coords, empty_rows, empty_cols, expand=1):
    c1, c2 = coords

    # make sure we always need to take increasing steps
    xmin, xmax = min(c1[0], c2[0]), max(c1[0], c2[0])
    ymin, ymax = min(c1[1], c2[1]), max(c1[1], c2[1])

    empty_cols_in_x = list(filter(lambda x: xmin <= x < xmax, empty_cols))
    empty_rows_in_y = list(filter(lambda y: ymin <= y < ymax, empty_rows))

    # print(coords, '| X:', empty_cols_in_x, '| Y:', empty_rows_in_y)

    xdist = (xmax - xmin) + (len(empty_cols_in_x) * expand) - len(empty_cols_in_x)
    ydist = (ymax - ymin) + (len(empty_rows_in_y) * expand) - len(empty_rows_in_y)

    return xdist + ydist


with open('input.txt', 'r') as f:
    mat = [[char for char in l.strip()] for l in f.readlines()]
    erows, ecols = empty_rows_cols(mat)

# print('\n'.join(mat))
# print('Empty X:', ecols)
# print('Empty Y:', erows)

coords = []

for y, row in enumerate(mat):
    for x, col in enumerate(row):
        if col == '#':
            coords.append((x, y))

pairs = list(combinations(coords, 2))

print(sum(route_length(pair, erows, ecols, expand=1_000_000) for pair in pairs))