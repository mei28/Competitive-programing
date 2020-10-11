from functools import reduce
import math
import math
N = int(input())
A = list(map(int, input().split()))
A = list(set(A))


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


print(gcd_list(A))