x = input()
n = int(input())
S = [input() for _ in range(n)]

dct_a = {i + 1: k for i, k in enumerate(x)}
dct_b = {k: i + 1 for i, k in enumerate(x)}

m = 0
for s in S:
    m = max(m, len(s))


def radix_sort(S, m):
    bucket = list()

    for i in range(27):
        bucket.append(list())

    for d in range(m - 1, -1, -1):
        for s in S:
            try:
                key = dct_b[s[d]]
            except:
                key = 0

            bucket[key].append(s)

        i = 0
        _array = []
        for values in bucket:
            for val in values:
                _array.append(val)

        S = _array

        for j in range(len(bucket)):
            bucket[j] = list()

    return S


ans = radix_sort(S, 26)

for i in ans:
    print(i)
