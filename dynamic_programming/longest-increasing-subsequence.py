def longest_increasing_subsequence(a, n):
    LIS = [1] * n

    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    return max(LIS) if n > 0 else 0

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(longest_increasing_subsequence(a, n))
