def count_triplets(N, A):
    pre_count = {}
    post_count = {}

    # 各要素のカウントをpost_countに保存
    for a in A:
        post_count[a] = post_count.get(a, 0) + 1

    # 全要素のカウントの合計
    total_post_count = N
    # A_jより前にあるA_iの要素の総数
    total_pre_count = 0

    ans = 0

    for j in range(N):
        post_count[A[j]] -= 1
        total_post_count -= 1

        if A[j] in pre_count:
            ans += total_pre_count * total_post_count
            ans -= pre_count[A[j]] * total_post_count
            ans -= post_count[A[j]] * total_pre_count

        # A[j]のカウントをpre_countで増やす
        pre_count[A[j]] = pre_count.get(A[j], 0) + 1
        total_pre_count += 1

    return ans


N = int(input())
A = list(map(int, input().split()))
print(count_triplets(N, A))
