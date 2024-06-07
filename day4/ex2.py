import re
from queue import PriorityQueue

with open('input.txt', 'r') as f:
    lines = [l.strip().split(':')[1] for l in f.readlines()]
    winning_nums = [g.split('|')[0] for g in lines]
    winning_nums = [set(map(int, re.findall(r'\d+', wns))) for wns in winning_nums]
    play_nums = [g.split('|')[1] for g in lines]
    play_nums = [set(map(int, re.findall(r'\d+', pns))) for pns in play_nums]
    games = list(zip(winning_nums, play_nums))

queue = PriorityQueue()
for p, g in enumerate(games):
    queue.put((p, g))
total = 0

while not queue.empty():
    p, (wns, pns) = queue.get()

    matches = wns & pns
    num_matches = len(matches)

    for i in range(p, p+num_matches):
        next_game = i + 1
        queue.put((next_game, games[next_game]))

    total += 1

print(total)