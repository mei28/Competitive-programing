import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

cnter = Counter(A)

_all = n * (n - 1) // 2

for k, v in cnter.items():
    _all -= v * (v - 1) // 2

print(_all)
