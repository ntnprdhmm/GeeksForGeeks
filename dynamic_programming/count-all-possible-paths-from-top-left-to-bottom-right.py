def solve(n, m):
    # init the grid with 1
    # there is only one way to go to each cell of the first col or first row
    grid = [[1 for _ in range(n)]] * (m)
    # as we can go only to the bot or to the right, add the number of ways
    # the top and left cell can be reached
    for row in range(1, m):
        for col in range(1, n):
            grid[row][col] = (grid[row-1][col] + grid[row][col-1]) % (10**9+7) 

    return grid[m-1][n-1]


# for each test case
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(solve(n, m))
