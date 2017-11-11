def LCS(X, Y, m, n):
    memo = [[None for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif X[i-1] == Y[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[m][n]

for _ in range(int(input())):
    # read 2 strings : X of length m and Y of length n
    m, n = map(int, input().split())
    X = input()
    Y = input()
    # find the length of the longest common subsequence
    print(LCS(X, Y, m, n))
