limits = {'red': 12, 'green': 13, 'blue': 14}

total = 0

with open('input.txt', 'r') as f:

    for i, l in enumerate(f.readlines(), start=1):

        rounds = l.split(': ')[-1].split('; ')

        grabs = [tuple(g.split()) for r in rounds for g in r.split(', ')]
        grabs = sorted([(int(num), color) for num, color in grabs])

        for num, color in grabs[::-1]:
            if num > limits[color]:
                break
        else:
            total += i

print(total)
