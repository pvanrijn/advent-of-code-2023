import re

def traverse(depth, seed_low, seed_high, maps):
    for src_low, src_high, dest in maps[depth]:
        if src_low <= seed_low < src_high:
            if seed_high < src_high:
                nseed_low  = seed_low  - src_low + dest
                nseed_high = seed_high - src_low + dest
                return nseed_low if depth == 6 else traverse(depth+1, nseed_low, nseed_high, maps)
            else:
                return min(traverse(depth, seed_low,   src_high-1, maps),
                           traverse(depth,  src_high, seed_high,   maps))

    return seed_low if depth == 6 else traverse(depth+1, seed_low, seed_high, maps)


with open('input.txt', 'r') as f:
    lines = f.readlines()

re_map = re.compile(r'[a-z-]+')
re_num = re.compile(r'\d+')

maps = {}
depth = None

for i, line in enumerate(lines):
    print('... line', i, 'of', len(lines), '...')
    line = line.strip()

    # get current map
    rmap = re_map.search(line)
    if rmap:
        res = rmap.group()
        if res == 'seeds':
            continue
        depth = 0 if depth is None else depth+1
        maps[depth] = []
        continue

    nums = list(re_num.findall(line))
    if nums:
        dest, src, length = tuple(map(int, nums))
        maps[depth].append((src, src+length, dest))

seeds = list(map(int, re_num.findall(lines[0])))
num_seeds = len(seeds)
seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, num_seeds, 2)]

results = []
for s_low, s_high in seeds:
    results.append(traverse(0, s_low, s_high, maps))
print(min(results))
