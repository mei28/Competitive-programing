import heapq


class PriorityQueue:
    """
    優先度付きキュー
    """

    class Reverse:
        def __init__(self, val):
            self.val = val

        def __lt__(self, other):
            return self.val > other.val

        def __str__(self):
            return str(self.val)

        def __repr__(self):
            return repr(self.val)

    def __init__(self, a=None, desc=False):
        self.__container = []
        if a:
            self.__container = a[:]

        if desc:
            for i, item in enumerate(self.__container):
                self.__container[i] = self.Reverse(item)
            self.pop = self.__pop_desc
            self.push = self.__push_desc
            self.top = self.__top_desc
        else:
            self.pop = self.__pop_asc
            self.push = self.__push_asc
            self.top = self.__top_asc
        heapq.heapify(self.__container)

    def __pop_asc(self):
        return heapq.heappop(self.__container)

    def __pop_desc(self):
        return heapq.heappop(self.__container).val

    def __push_asc(self, item):
        heapq.heappush(self.__container, item)

    def __push_desc(self, item):
        heapq.heappush(self.__container, self.Reverse(item))

    def __top_asc(self):
        return self.__container[0]

    def __top_desc(self):
        return self.__container[0].val

    def sum(self):
        return sum(self.__container)

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        return str(sorted(self.__container))

    def __repr__(self):
        return self.__str__()


n, m = map(int, input().split())

G = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    cnt[b] += 1
    G[a].append(b)

ans = []

pq = PriorityQueue()
for i in range(1, n + 1):
    if cnt[i] == 0:
        pq.push(i)

while pq:
    u = pq.pop()
    ans.append(u)

    for v in G[u]:
        cnt[v] -= 1
        if cnt[v] == 0:
            pq.push(v)

if len(ans) == n:
    print(*ans)
else:
    print(-1)
