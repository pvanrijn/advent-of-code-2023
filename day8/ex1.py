import re

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

base_directions = lines[0]
routelines = lines[1:]
re_pat     = re.compile(r'[A-Z]+')
routes     = {}

for route in routelines:
    location, left, right = tuple(re_pat.findall(route))
    routes[location] = {'L': left, 'R': right}

current_location = 'AAA'
end_reached = False
steps = 0
directions = ''

while not end_reached:

    # add extra set of directions if previous set failed
    directions += base_directions

    for direction in directions:

        if current_location == 'ZZZ':
            end_reached = True
            break

        current_location = routes[current_location][direction]
        steps += 1

        if steps % 100_000 == 0:
            print(f'{steps:>8} steps taken...')

print(steps)