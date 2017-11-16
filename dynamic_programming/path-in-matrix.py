def largest_sum_path(a, n):
    # for each other rows until the end
    for i in range(1, n):
        # loop through each cell
        for j in range(n):
            # calcule the max sum path to each cell
            top_index = (i-1)*n + j
            from_top = a[top_index]
            from_top_left = 0 if j == 0 else a[top_index - 1]
            from_top_right = 0 if j == (n-1) else a[top_index + 1]
            a[i*n + j] += max(from_top_left, from_top, from_top_right)

    return max(a[(n*(n-1)):])

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(largest_sum_path(a, n))
