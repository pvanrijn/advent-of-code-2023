import functools
import re

def distance(pushtime, maxtime):
    return (maxtime - pushtime) * pushtime

with open('input.txt', 'r') as f:
    times   = list(map(int, re.findall(r'\d+', next(f))))
    records = list(map(int, re.findall(r'\d+', next(f))))

winning_opts = []
for time, record in zip(times, records):
    opts = 0
    for push in range(1, time):
        dist = distance(push, time)
        if dist > record:
            opts += 1
    winning_opts.append(opts)

print(times)
print(records)
print(functools.reduce(lambda x, y: x * y, winning_opts))