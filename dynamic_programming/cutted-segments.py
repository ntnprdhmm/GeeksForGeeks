def count_ways_to_cut(n, s):
    """ n: the length to cut
        s: segments lengths
    """
    if n < 0:
        return 0

    elif not n in memo:
        memo[n] = 1 + max(count_ways_to_cut(n-s[0], s), count_ways_to_cut(n-s[1], s), count_ways_to_cut(n-s[2], s))

    return memo[n]

for _ in range(int(input())):
    memo = {}
    n = int(input())
    s = list(map(int, input().split()))
    print(count_ways_to_cut(n, s) - 1)
