import math
import re
from functools import reduce

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

# base_directions = lines[0]
directions = lines[0]
routelines = lines[1:]

# re_pat = re.compile(r'[A-Z]+')
re_pat = re.compile(r'[A-Z0-9]+')  # use with test3.txt
routes = {}

for route in routelines:
    location, left, right = tuple(re_pat.findall(route))
    routes[location] = {'L': left, 'R': right}

# start_locations   = [loc for loc in routes if loc.endswith('A')]
# current_locations = start_locations[:]
current_locations = [loc for loc in routes if loc.endswith('A')]
# location_patterns = {i: [] for i in range(len(current_locations))}
location_patterns = {loc: [] for loc in current_locations}

end_reached = False
steps = 0

for loc in current_locations:

    print(loc)
    curloc  = loc
    found_z = False

    while not found_z:
        for direction in directions:
            curloc = routes[curloc][direction]
            location_patterns[loc].append(curloc)
            if curloc.endswith('Z'):
                found_z = True
                break
        directions += directions

location_patterns = {loc: len(pattern) for loc, pattern in location_patterns.items()}
print(math.lcm(*location_patterns.values()))
