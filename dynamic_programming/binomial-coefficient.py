for _ in range(int(input())):

    n, k = map(int, input().split())

    def binomial_coefficient(n, k):
        memo = [[0 for i in range(k+1)] for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(k+1):
                if j == 0 or j == i:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i-1][j] + memo[i-1][j-1]

        return memo[n][k]


    print(binomial_coefficient(n, k) % (10**9 + 7))
