L, R = map(int, input().split())
if R - L + 1 >= 2020:
    ans = 0

else:
    List = [i % 2019 for i in range(L, R + 1)]
    # a = min(List)
    # List.remove(a)
    # ans = (a*(min(List))) % 2019
    # sorted(List)
    # ans = List[0]*List[1] % 2019
    if 0 in List:
        ans = 0
    else:
        m = float("inf")
        for i in range(len(List)):
            for j in range(i + 1, len(List)):
                if List[i] * List[j] % 2019 < m:
                    m = List[i] * List[j] % 2019
        ans = m


print(ans)
