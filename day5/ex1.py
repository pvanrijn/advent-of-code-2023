import re

re_map = re.compile(r'[a-z-]+')
re_num = re.compile(r'\d+')

maps = {}

with open('input.txt', 'r') as f:
    mapmax = 0
    curmap = ''
    lines = f.readlines()
    for i, line in enumerate(lines):

        print('... line', i, 'of', len(lines), '...')
        line = line.strip()

        # get current map
        rmap = re_map.search(line)
        if rmap:
            curmap = rmap.group()
            maps[curmap] = {}
            continue

        nums = list(re_num.findall(line))

        if nums:

            dest, src, step = map(int, nums)
            dest = list(range(dest, dest+step))
            src  = list(range( src,  src+step))
            maps[curmap].update(dict(zip(src, dest)))

        elif not maps[curmap]:
            del maps[curmap]
            continue


lowest_loc = float('inf')
seeds = list(map(int, re_num.findall(lines[0])))
num_seeds = len(seeds)

print('\n\n# START')
print('# NUMBER OF SEEDS:', num_seeds)

for i, seed in enumerate(seeds, start=1):

    print(' * Seed', i, 'of', num_seeds)
    mapkeys = list(maps.keys())
    valkey = seed

    while mapkeys:
        mapkey = mapkeys.pop(0)
        mapkeyvals = set(maps[mapkey].keys())
        if valkey not in mapkeyvals:
            continue
        valkey = maps[mapkey][valkey]

    if valkey < lowest_loc:
        lowest_loc = valkey


print(lowest_loc)
