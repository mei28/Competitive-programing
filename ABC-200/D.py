from itertools import combinations
from math import *
from typing import *

MOD = 200

if __name__ == "__main__":
    n = int(input())
    A = map(int, input().split())
    Bk = [[] for i in range(200)]
