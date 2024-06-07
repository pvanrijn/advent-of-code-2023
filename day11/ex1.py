from itertools import combinations

def expand_matrix(mat, expansion=2):

    # insert extra column if all characters in column are empty (.)
    mat_newcols = []
    for row in mat:
        newrow = ''
        for x, col in enumerate(row):
            if all(r[x] == '.' for r in mat):
                newrow += col * expansion
            else:
                newrow += col
        mat_newcols.append(newrow)

    # insert extra row if all characters in row are empty (.)
    mat_newrows = []
    for row in mat_newcols:
        if all(c == '.' for c in row):
            for _ in range(expansion):
                mat_newrows.append(row)
        else:
            mat_newrows.append(row)

    return mat_newrows


def route_length(coords):
    c1, c2 = coords

    # make sure we always need to take increasing steps
    xmin, xmax = min(c1[0], c2[0]), max(c1[0], c2[0])
    ymin, ymax = min(c1[1], c2[1]), max(c1[1], c2[1])

    return (xmax - xmin) + (ymax - ymin)



with open('input.txt', 'r') as f:
    mat = [[char for char in l.strip()] for l in f.readlines()]
    mat = expand_matrix(mat, expansion=2)

# print('\n'.join(mat))

coords = []

for x, row in enumerate(mat):
    for y, col in enumerate(row):
        if col == '#':
            coords.append((x, y))

pairs = list(combinations(coords, 2))

print(sum(route_length(pair) for pair in pairs))
