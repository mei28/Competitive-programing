from collections import Counter


def process_queries(queries):
    bag = Counter()
    result = []

    for query in queries:
        if query[0] == 1:
            x = query[1]
            bag[x] += 1
        elif query[0] == 2:
            x = query[1]
            if bag[x] == 1:
                del bag[x]
            else:
                bag[x] -= 1
        elif query[0] == 3:
            result.append(len(bag))

    return result


Q = int(input())
queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    queries.append(query)

results = process_queries(queries)
for res in results:
    print(res)
