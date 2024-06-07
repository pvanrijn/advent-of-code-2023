import re

with open('input.txt', 'r') as f:
    games = [l.strip().split(':')[1] for l in f.readlines()]
    winning_nums = [g.split('|')[0] for g in games]
    winning_nums = [set(map(int, re.findall(r'\d+', wns))) for wns in winning_nums]
    play_nums = [g.split('|')[1] for g in games]
    play_nums = [set(map(int, re.findall(r'\d+', pns))) for pns in play_nums]


total = 0
for pns, wns in zip(play_nums, winning_nums):

    wns_found = wns & pns
    if not wns_found:
        continue

    tmp_total = 0
    for n in wns_found:
        if tmp_total == 0:
            tmp_total = 1
            continue
        tmp_total *= 2

    total += tmp_total

print(total)