def LRS(S, n):
    memo = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            # if same char but not at same index
            if S[i-1] == S[j-1] and i != j:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[n][n]

for _ in range(int(input())):
    # read a strings S of length n
    n = int(input())
    S = input()
    # find the length of the longest repeated subsequence in S
    print(LRS(S, n))
