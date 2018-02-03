def solve(s1, s2, n, m):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_substr_len = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_substr_len = max(max_substr_len, dp[i][j])

    return max_substr_len

# for each test case
for _ in range(int(input())):
    n, m = map(int, input().split())
    s1 = list(input())
    s2 = list(input())
    print(solve(s1, s2, n, m))
