def find_nth_sum_of_three_repunits(N):
    repunits = [int("1" * i) for i in range(1, 15)]  # 15 digits should be enough

    sum_of_three_repunits = set()

    for i in range(len(repunits)):
        for j in range(i, len(repunits)):
            for k in range(j, len(repunits)):
                sum_of_three_repunits.add(repunits[i] + repunits[j] + repunits[k])

    sorted_sums = sorted(list(sum_of_three_repunits))
    return sorted_sums[N - 1] if N <= len(sorted_sums) else "N is too large"


n = int(input())
print(find_nth_sum_of_three_repunits(n))
