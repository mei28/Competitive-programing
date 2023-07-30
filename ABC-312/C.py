from string import printable

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

low = 0
high = max(max(A), max(B)) + 1


def binary_search(low, high, sellers, buyers):
    while high - low > 1:
        mid = (low + high) // 2
        seller_count = len([s for s in sellers if s <= mid])
        buyer_count = len([b for b in buyers if b >= mid])

        if seller_count >= buyer_count:
            high = mid
        else:
            low = mid

    return high


print(binary_search(low, high, A, B))
