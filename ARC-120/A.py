if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    sus_a = []
    for i in range(1, N):
        A[i] += A[i - 1]
