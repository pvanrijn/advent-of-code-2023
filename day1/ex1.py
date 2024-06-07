import re

pat = re.compile(r'\d')

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

nums = []

for l in lines:
    matches = pat.findall(l)
    first, last = matches[0], matches[-1]
    nums.append(int(first+last))

print(sum(nums))
