def nth_ugly_number(n):
    """ Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
        firsts 11 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15
    """
    ugly = [0] * n
    ugly[0] = 1

    i2 = i3 = i5 = 0
    next_multiple_2 = 2
    next_multiple_3 = 3
    next_multiple_5 = 5

    for i in range(1, n):
        m = min(next_multiple_5, next_multiple_3, next_multiple_2)

        ugly[i] = m

        if m == next_multiple_2:
            i2 += 1
            next_multiple_2 = ugly[i2] * 2
        if m == next_multiple_3:
            i3 += 1
            next_multiple_3 = ugly[i3] * 3
        if m == next_multiple_5:
            i5 += 1
            next_multiple_5 = ugly[i5] * 5

    return ugly[-1]

print(nth_ugly_number(int(input())))
