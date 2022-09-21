# f(K) を求める関数
def f(N, K):
    count = 0
    for i in range(N):
        count += min(N, K // (i + 1))
    return count


N, X = map(int, input().split())

# 二分探索
left = 0
right = N * N
while left != right:  # 解が求まるまで
    # left と right の 中点 mid をとる
    mid = (left + right) // 2
    if f(N, mid) >= X:  # もし A[mid] >= B[i] ならば答えは left 以上 mid 以下
        right = mid
        # 範囲を狭める
    else:  # そうでなければ答えは mid+1 以上 right 以下
        left = mid + 1
        # 範囲を狭める

# 答えは left 以上 right 以下であることがわかっている。
# left = right なので、答えは left である。
ans = left
print(ans)
