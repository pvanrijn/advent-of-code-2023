import re

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

pat = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

mapper = {'one':   1, 'two':   2, 'three': 3,
          'four':  4, 'five':  5, 'six':   6,
          'seven': 7, 'eight': 8, 'nine':  9}

nums = []

for l in lines:
    matches = pat.findall(l)
    matches = [mapper.get(m, m) for m in matches]
    first, last = matches[0], matches[-1]
    nums.append(int(f'{first}{last}'))

print(sum(nums))
