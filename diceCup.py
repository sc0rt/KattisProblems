from collections import Counter

inp = input()

die1 = int(inp.split(' ')[0])
die2 = int(inp.split(' ')[1])

def highProbOut(die1, die2):
    sums = []
    max_keys = []

    for i in range(1, die1 + 1):
        for j in range(1, die2 + 1):
            sums.append(i + j)

    count = Counter(sums)

    for k,v in count.items():
        if v == max(count.values()):
            max_keys.append(k)

    return sorted(max_keys)

probs = highProbOut(die1, die2)

for i in probs:
    print(i)
