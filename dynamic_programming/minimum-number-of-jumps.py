def solve(n, arr):
    # if arr[0] = 0, we can't move
    if arr[0] == 0:
        return float("Inf")
    # by default all cells are unreachable
    jumps = [float("Inf") for _ in range(n)]
    # set arr[0] to 0 because we need 0 jumps to reach this cell
    jumps[0] = 0

    for i in range(1, n):
        # we know the min number of jumps required to reach previous cells
        # loop through these cells and get the cell with the minimum number of
        # jumps from which it is possible to jump to the current cell
        for j in range(i):
            if i <= j+arr[j]:
                jumps[i] = min(jumps[i], jumps[j]+1)
                # we found the min, we can stop here
                break

    return jumps[n-1]

# for each test case
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = solve(n, arr)
    print(-1 if ans == float("+Inf") else ans)
