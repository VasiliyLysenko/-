import itertools


def all_variants(text):
    for j in range(1, len(text) + 1):
        comb = list(itertools.combinations(text, j))
        for k in comb:
            yield ''.join(k)


a = all_variants("abc")
for i in a:
    print(i)