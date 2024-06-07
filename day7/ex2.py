from collections import Counter


handmapper = {
    5: lambda n: '5-of-a-kind',
    4: lambda n: '4-of-a-kind',
    3: lambda c: 'full-house' if min(c.values()) == 2 else '3-of-a-kind',
    2: lambda c: 'two-pair' if Counter(c.values())[2] == 2 else 'one-pair',
    1: lambda n: 'high-card'
}

cards = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9':  9,
         '8':  8, '7':  7, '6':  6, '5':  5, '4':  4,
         '3':  3, '2':  2, 'J': 1}

hands = {'5-of-a-kind': [], '4-of-a-kind': [], 'full-house': [],
         '3-of-a-kind': [], 'two-pair':    [], 'one-pair':   [],
         'high-card':   []}

with open('input.txt', 'r') as f:
    hands_bids = [(l.split()[0], int(l.split()[1])) for l in f.readlines()]

for hand, bid in hands_bids:

    # count cards
    cardcount = Counter(hand)

    # add joker count to highest card count
    j_count = 0
    if 'J' in cardcount and hand != 'JJJJJ':
        j_count += cardcount['J']
        del cardcount['J']  # remove to exclude from hand mapping

    highest_play = max(cardcount, key=cardcount.get)
    cardcount[highest_play] += j_count

    # get hand type and add scores & bid to list of hand types
    maxcount = max(cardcount.values())
    handname = handmapper[maxcount](cardcount)
    hands[handname].append(([cards[card] for card in hand], bid))

allbids   = []

for handname, scores_bid in hands.items():

    scores_bid.sort(
        key=lambda x: tuple(x[0][i] for i in range(len(x[0]))),
        reverse=True
    )
    allbids   += [sb[1] for sb in scores_bid]

allbids   = allbids[::-1]

# get sum of all rank * bid, use enumerate to get rank
score = sum(map(lambda b: b[0] * b[1], enumerate(allbids, start=1)))

print(score)

# Too high: 251523375