def lscs(a, n):

    max_total = float('-Inf')
    max_local = 0

    # for each element in the array
    for i in range(n):
        # update the local max
        max_local += a[i]
        # update max total if max local is greater
        max_total = max(max_total, max_local)
        # if < 0, this local max will not help
        # to find the largest sum
        # so set max_local to 0
        if max_local < 0:
            max_local = 0

    return max_total


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(lscs(a, n))
