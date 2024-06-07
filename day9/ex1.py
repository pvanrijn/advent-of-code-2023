import re

def predict_next(seq, verbose=False):

    if verbose:
        print(seq)

    if all(n == 0 for n in seq):
        return 0

    diff = [seq[i+1] - seq[i] for i in range(len(seq)) if i+1 < len(seq)]

    return seq[-1] + predict_next(diff, verbose=verbose)


with open('input.txt', 'r') as f:
    sequences = [re.findall(r'[0-9-]+', l.strip()) for l in f.readlines()]
    sequences = [list(map(int, s)) for s in sequences]

print(sum(predict_next(seq) for seq in sequences))

# Too high: 2075724809