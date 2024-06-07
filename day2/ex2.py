import math
import functools

limits = {'red': 12, 'green': 13, 'blue': 14}

total = 0

with open('input.txt', 'r') as f:
    for i, l in enumerate(f.readlines(), start=1):

        rounds = l.split(': ')[-1].split('; ')

        grabs = [tuple(g.split()) for r in rounds for g in r.split(', ')]

        grabdict = dict()
        for num, color in grabs:
            grabdict.setdefault(color, []).append(int(num))

        red   = max(grabdict['red'])
        green = max(grabdict['green'])
        blue  = max(grabdict['blue'])

        total += functools.reduce(lambda x, y: x * y, [red, green, blue])

print(total)
