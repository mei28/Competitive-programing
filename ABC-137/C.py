N = int(input())
S = [input() for _ in range(N)]

_S = dict()

for s in S:
    _S[str(sorted(s))] = _S.setdefault(str(sorted(s)), 0) + 1


def nC2(n: int):
    return n * (n - 1) // 2


ans = 0
for k, v in _S.items():
    ans += nC2(v)

print(ans)
