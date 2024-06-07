import re

def distance(pushtime, maxtime):
    return (maxtime - pushtime) * pushtime

with open('input.txt', 'r') as f:
    time   = int(''.join(re.findall(r'\d+', next(f))))
    record = int(''.join(re.findall(r'\d+', next(f))))

print(f'Time:   {time:>15}')
print(f'Record: {record:>15}\n')

opts = 0
for push in range(1, time):
    dist = distance(push, time)
    if dist > record:
        opts += 1

print('Number of ways:', opts)