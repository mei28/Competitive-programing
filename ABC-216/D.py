def main():
    from collections import deque

    def solve():
        que = deque()
        rem = N
        cnt = [0] * N
        for i in range(M):
            front = T[i][-1]
            cnt[front] += 1
            if cnt[front] == 2:
                que.append(front)

        while que:
            x = que.popleft()
            rem -= 1
            first, second = P[x]
            T[first].pop()
            T[second].pop()
            if T[first]:
                y = T[first][-1]
                cnt[y] += 1
                if cnt[y] == 2:
                    que.append(y)
            if T[second]:
                y = T[second][-1]
                cnt[y] += 1
                if cnt[y] == 2:
                    que.append(y)
        return rem == 0

    N, M = map(int, input().split())
    T = []
    P = [[] for _ in range(N)]
    for i in range(M):
        k = int(input())
        a = list(x - 1 for x in map(int, input().split()))
        for x in a:
            P[x].append(i)
        T.append(a[::-1])

    print("Yes" if solve() else "No")


if __name__ == "__main__":
    main()
