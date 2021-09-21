if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    ans = 0
    for i in range(N):
        a, b = A[i], B[i]
        ans += abs(a - b)
    print(ans)
    pass
