import re

re_map = re.compile(r'[a-z-]+')
re_num = re.compile(r'\d+')

maps = {}

with open('input.txt', 'r') as f:

    curmap = ''
    lines = f.readlines()

    for i, line in enumerate(lines):

        print('... line', i, 'of', len(lines), '...')
        line = line.strip()

        # get current map
        rmap = re_map.search(line)
        if rmap:
            curmap = rmap.group()
            maps[curmap] = []
            continue

        nums = list(re_num.findall(line))
        if nums:
            nums = tuple(map(int, nums))
            maps[curmap].append(nums)

        if not maps[curmap]:
            del maps[curmap]
            continue

print(maps)

lowest_loc = float('inf')
seeds = list(map(int, re_num.findall(lines[0])))
num_seeds = len(seeds)

print('\n\n# START')
print('# NUMBER OF SEEDS:', num_seeds)

for i, seed in enumerate(seeds, start=1):
    print(' * Seed', i, 'of', num_seeds)
    mapkeys = list(maps.keys())
    valkey = seed
    for curmap, numranges in maps.items():
        for dest, src, size in numranges:
            if src <= valkey < src+size:
                valkey = dest + (valkey - src)
                break
    if valkey < lowest_loc:
        lowest_loc = valkey

print(lowest_loc)
