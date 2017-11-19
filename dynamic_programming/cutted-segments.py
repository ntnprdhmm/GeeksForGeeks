def count_ways_to_cut(n, x, y, z):
    arr = [-1]*(n+1)
    # when length is 0, there is 0 way to cut it
    arr[0] = 0

    for i in range(1, n+1):
        a = -1 if (i - x < 0) else arr[i-x]
        b = -1 if (i - y < 0) else arr[i-y]
        c = -1 if (i - z < 0) else arr[i-z]
        if a >= 0 or b >= 0 or c >= 0:
            arr[i] = 1 + max(a, b, c)

    return arr[n]

for _ in range(int(input())):
    n = int(input())
    x, y, z = map(int, input().split())
    print(count_ways_to_cut(n, x, y, z))
