def count_ways_to_make_change(s, m, n):
    a = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        a[i][0] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] > j :
                a[i][j] = a[i-1][j]
            else:
                a[i][j] += a[i-1][j] + a[i][j - s[i-1]]

    return a[m][n]

for _ in range(int(input())):
    m = int(input())
    s = list(map(int, input().split()))
    n = int(input())
    print(count_ways_to_make_change(s, m, n))
