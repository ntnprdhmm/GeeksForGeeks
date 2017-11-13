def lscs(a, n):

    memo = [[0]*(n-i+1) for i in range(n+1)]

    # init first line
    for i in range(n):
        memo[1][i] = a[i]
    m = max(float('-Inf'), max(memo[1]))

    # for each line
    for i in range(2, n+1):
        for j in range(n-i+1):
            memo[i][j] = memo[i-1][j] + memo[i-1][j+1] - memo[i-2][j+1]
        m = max(m, max(memo[i]))

    return m


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(lscs(a, n))
