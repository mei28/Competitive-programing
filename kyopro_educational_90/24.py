if __name__ == "__main__":
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for a, b in zip(A, B):
        cnt += abs(a - b)

    if cnt > k:
        print("No")
    elif abs(cnt - k) % 2 == 0:
        print("Yes")
    else:
        print("No")
