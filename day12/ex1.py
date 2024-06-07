import re
from itertools import product

def filler(word):
    options = [(c,) if c != '?' else ('?', '#') for c in word]
    return list(''.join(o) for o in product(*options))

def matcher(spring, sizes):
    while spring:
        spring2 = spring[:]

        spring = spring[1:]

with open('test.txt', 'r') as f:
    springlines_sizes = [tuple(l.strip().split()) for l in f.readlines()]
    springlines_sizes = [(s, tuple(p.split(','))) for s, p in springlines_sizes]

for springline, sizes in springlines_sizes:
    springs = filler(springline)
    springs = [[len(s) for s in re.findall(r'#+', spring)] for spring in springs]
    print(springs)

    for spring in springs:

        while spring:

            spring2 = spring[:]

            for size in sizes:

                if



    # for spring in springs:
    #     sprint_counts = [len(s) for s in re.findall(r'#+', spring)]
    #     print

    # while spring_counts:

    #     size = sizes.pop()